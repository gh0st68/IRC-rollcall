# Roll Call Bot

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Running the Bot](#running-the-bot)
7. [Credits](#credits)

## Introduction
Roll Call Bot is an IRC bot designed to list all nicknames in a channel when the command `!rollcall` is issued. It sends the list of users to the channel to wake them up. 

## Features
- Joins specified IRC channel and listens for the `!rollcall` command.
- Provides a loading bar animation to indicate processing.
- Lists all nicknames in the channel and sends the list to the channel.

## Requirements
- Python 3.x
- `irc` library for Python

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/rollcall-bot.git
    cd rollcall-bot
    ```

2. **Install required packages using pip:**
    ```sh
    pip3 install irc
    ```

## Usage
- **Join the bot to the IRC channel:**
  Configure the server, port, channel, and bot nickname in the `MyBot` class initialization.

- **Issue the `!rollcall` command:**
  Type `!rollcall` in the channel to trigger the bot.

## Running the Bot
To run the bot using `screen`:

1. **Start a new screen session:**
    ```sh
    screen -S rollcall-bot
    ```

2. **Run the bot:**
    ```sh
    python3 rollcall1.0.py
    ```

3. **Detach from the screen session:**
    Press `Ctrl-A` then `D`

4. **To reattach to the screen session:**
    ```sh
    screen -r rollcall-bot
    ```

## Credits
Created by gh0st

Stay salty!

Join us at IRC.TWISTEDNET.ORG #DEV
