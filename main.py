import discord
import os
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

client = discord.Client()
start_game = False


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global start_game
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        if message.content == '!start':
            start_game = True
            print("Starting Game")
            await message.channel.send('Starting')
            return

        if start_game:
            if message.content == '!end':
                start_game = False
                await message.channel.send('Ending')
                return
        else:
            await message.channel.send('Game not Started')
            return

    if start_game:
        if message.content.lower() == "right":
            time.sleep(1)
            keyboard.press(Key.right)
        if message.content.lower() == "left":
            time.sleep(1)
            keyboard.press(Key.left)
        if message.content.lower() == "up":
            time.sleep(1)
            keyboard.press(Key.up)
        if message.content.lower() == "down":
            time.sleep(1)
            keyboard.press(Key.down)

        if message.content.lower() == "a":
            time.sleep(1)
            keyboard.press(Key.space)
            time.sleep(0.1)
            keyboard.release(Key.space)
        if message.content.lower() == "b":
            time.sleep(1)
            keyboard.press(Key.tab)
            time.sleep(0.1)
            keyboard.release(Key.tab)
        if message.content.lower() == "x":
            time.sleep(1)
            keyboard.press(Key.insert)
            time.sleep(0.1)
            keyboard.release(Key.insert)
        if message.content.lower() == "y":
            time.sleep(1)
            keyboard.press(Key.backspace)
            time.sleep(0.1)
            keyboard.release(Key.backspace)

        if "stop" in message.content.lower():
            if "right" in message.content.lower():
                keyboard.release(Key.right)
            if "left" in message.content.lower():
                keyboard.release(Key.left)
            if "up" in message.content.lower():
                keyboard.release(Key.up)
            if "down" in message.content.lower():
                keyboard.release(Key.down)

    else:
        await message.channel.send('Game not Started')
        return


client.run('TOKEN') # BOTS TOKEN IN STRING FORMAT

