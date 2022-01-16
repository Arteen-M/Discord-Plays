import discord
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

client = discord.Client()
start_game = False

@client.event
async def on_ready():
    print("Commencing Discord Plays Pokemon. Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    global start_game
    if message.author == client.user:
        return

    if message.content.startswith("!"):
        if message.content == "!":
            start_game = True
            print("Starting Game")
            await message.channel.send("Starting")
            return

        if start_game:
            if message.content == "!end":
                start_game = False
                print("Ending Game")
                await message.channel.send("Ending")
                return

    def specmove(direction, n):
        for j in range(n):
            if direction == "r":
                keyboard.press(Key.right)
                time.sleep(0.2)
                keyboard.release(Key.right)
                time.sleep(0.2)
            if direction == "l":
                keyboard.press(Key.left)
                time.sleep(0.2)
                keyboard.release(Key.left)
                time.sleep(0.2)
            if direction == "u":
                keyboard.press(Key.up)
                time.sleep(0.2)
                keyboard.release(Key.up)
                time.sleep(0.2)
            if direction == "d":
                keyboard.press(Key.down)
                time.sleep(0.2)
                keyboard.release(Key.down)
                time.sleep(0.2)

        keyboard.release(Key.left)
        keyboard.release(Key.down)
        keyboard.release(Key.up)


    if start_game:
        specs = [1, 2, 3, 4, 5]

        if "r" in message.content.lower():
            if message.content.lower() == "r":
                keyboard.press(Key.right)

            else:
                for i in range(len(specs)):
                    if str(specs[i]) in message.content.lower():
                        specmove("r", (i+1))
                        break

        if "l" in message.content.lower():
            if message.content.lower() == "l":
                keyboard.press(Key.left)

            else:
                for i in range(len(specs)):
                    if str(specs[i]) in message.content.lower():
                        specmove("l", (i+1))
                        break

        if "d" in message.content.lower():
            if message.content.lower() == "d":
                keyboard.press(Key.down)

            else:
                for i in range(len(specs)):
                    if str(specs[i]) in message.content.lower():
                        specmove("d", (i+1))
                        break

        if "u" in message.content.lower():
            if message.content.lower() == "u":
                keyboard.press(Key.up)

            else:
                for i in range(len(specs)):
                    if str(specs[i]) in message.content.lower():
                        specmove("u", (i+1))
                        break

        if message.content.lower() == "a":
            keyboard.press(Key.space)
            time.sleep(0.1)
            keyboard.release(Key.space)
        if message.content.lower() == "b":
            keyboard.press(Key.tab)
            time.sleep(0.1)
            keyboard.release(Key.tab)
        if message.content.lower() == "x":
            keyboard.press(Key.insert)
            time.sleep(0.1)
            keyboard.release(Key.insert)
        if message.content.lower() == "y":
            keyboard.press(Key.backspace)
            time.sleep(0.1)
            keyboard.release(Key.backspace)

        if message.content.lower() == "c":
            keyboard.release(Key.right)
            keyboard.release(Key.left)
            keyboard.release(Key.down)
            keyboard.release(Key.up)

        if message.content.lower() == "run":
            keyboard.press(Key.tab)
            time.sleep(10)
            keyboard.release(Key.tab)

    else:
        await message.channel.send("Game not Started bruh")
        return

client.run("OTI1ODMwNjM4OTg3MjY0MDIw.Ycy0-Q.iIPEvOmfcRL6FxTqe8h0-BroknY")