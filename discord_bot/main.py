import discord
from shell_restart import shell_restart
from show_log import show_log
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

    # 疎通確認
    if message.content.startswith("$hello"):
        log(f"Send hello world message in response to {message.author}", level="info")
        await message.channel.send("Hello world!")

    # シェル実行
    if message.content.startswith("$sh"):
        log(f"Execute shell command from {message.author}: {message.content}", level="info")
        await shell_exec(message)

    # ログ表示
    if message.content.startswith("$log"):
        await show_log(message)

    # 再起動（あんまり意味ない）
    if message.content.startswith("$restart"):
        log(f"Restart command issued by {message.author}", level="info")
        await shell_restart(message)


def run_bot():
    client.run(TOKEN)


if __name__ == "__main__":
    run_bot()
