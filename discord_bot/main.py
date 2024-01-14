import discord
from shell_restart import shell_restart

from discord_bot.shell_exec import shell_exec
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
        await message.channel.send("Hello world!")

    if message.content.startswith("$sh"):
        await shell_exec(message)

    if message.content.startswith("$restart"):
        await shell_restart(message)


client.run(TOKEN)
