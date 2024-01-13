import shlex
import subprocess

import discord

from env import TOKEN

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("$sh"):
        command_text = message.content[len("$sh ") :]
        try:
            args = shlex.split(command_text)
            print(args)
            output = subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = f"Error: {e.output}"

        # 結果の送信
        await message.channel.send(f"```\n{output}\n```")


client.run(TOKEN)
