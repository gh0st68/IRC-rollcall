##Roll call bot##
##Join it to a channel and simply type !rollcall
##It should provide a list of all nicks in the channel and send it to the channel to wake the users up!##
##by gh0st##
#stay salty!##


import ssl
import irc.bot
import irc.connection
import textwrap
import time


class MyBot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        irc.bot.SingleServerIRCBot.__init__(self,
                                            [("irc.twistednet.org", 6697, "mypassword")],
                                            # 6697 is commonly used for SSL connections
                                            "fawkk",
                                            "fuckme",
                                            connect_factory=irc.connection.Factory(wrapper=ssl.wrap_socket))

        self.channel = "#dev"
        self.channel_users = []  # Add an attribute to store the list of users in the channel
        self.send_user_list = False  # Add an attribute to control whether to send the user list

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        if e.arguments[0] == "!rollcall":
            for i in range(0, 101, 10):  # Incrementing by 10 from 0 to 100
                time.sleep(1)  # Delay to simulate loadingb
                color_code = '\x0304' if i < 100 else '\x0303'  # Red color for loaded part, green for 100%
                loading_bar = '|' + color_code + '=' * int(i / 10) + '\x0315' + ' ' * (10 - int(
                    i / 10)) + '|'  # Use the appropriate color for the loaded part and white for unloaded
                c.privmsg(self.channel, f"Loading: {loading_bar} {i}%")  # Send loading bar to the channel

            # Add message when loading reaches 100%
            c.privmsg(self.channel, "Hide your wives, Milkman's in town!")

            # Set send_user_list to True and request a list of nicknames in the channel
            self.send_user_list = True
            c.send_raw(f"NAMES {self.channel}")

    def on_namreply(self, c, e):
        names_list = e.arguments[2].split()  # Get the names list from the event
        cleaned_names = [name.lstrip('@~&+') for name in names_list]  # Remove special characters from names
        self.channel_users.extend(cleaned_names)  # Add cleaned names to the channel_users list

    def on_endofnames(self, c, e):
        if self.send_user_list:
            cleaned_names_str = ', '.join(self.channel_users)  # Join cleaned names as a string
            max_message_length = 400  # To avoid hitting the 512-byte limit, adjust this value if needed
            for chunk in textwrap.wrap(cleaned_names_str, max_message_length):
                c.privmsg(self.channel, f"Users in the channel: {chunk}")  # Send the cleaned names list to the channel
            self.channel_users.clear()  # Clear the channel_users list for future use
            self.send_user_list = False  # Reset send_user_list to False


if __name__ == "__main__":
    MyBot().start()

