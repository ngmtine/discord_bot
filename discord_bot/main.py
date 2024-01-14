import discord
from shell_restart import shell_restart
from util.log import log

from discord_bot.shell_exec import shell_exec
from env import TOKEN

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    log(f"Logged in as {client.user}", level="info")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        log(f"Send hello world message in response to {message.author}", level="info")
        await message.channel.send("Hello world!")

    if message.content.startswith("$sh"):
        log(f"Execute shell command from {message.author}: {message.content}", level="info")
        await shell_exec(message)

    if message.content.startswith("$restart"):
        log(f"Restart command issued by {message.author}", level="info")
        await shell_restart(message)


client.run(TOKEN)
