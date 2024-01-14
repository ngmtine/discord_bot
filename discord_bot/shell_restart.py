import subprocess

from util.log import log

from env import REPOSITORY_PATH


# シェル実行スクリプト再起動（本当に死んでたら受け取れないので意味ない）
async def shell_restart(message):
    message.content[len("$restart ") :]
    response = ""

    try:
        # コマンド文字列生成
        command = f"cd {REPOSITORY_PATH} && bash ./restart.sh"
        log(f"Executing restart command: {command}", level="info")

        # 実行
        result = await subprocess.run(command, shell=True, text=True, capture_output=True)

        # main.pyが再起動されdiscordにメッセージが送信されないので以降は意味のない記述！！
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stdout:
            response += f"```bot restarted successfully:\n{stdout}```"
            log(f"Bot restarted successfully: {stdout}", level="info")
        if stderr:
            response += f"```fix\nerror restarting bot:\n{stderr}```"
            log(f"Error restarting bot: {stderr}", level="error")

    # 実行時エラー
    except Exception as e:
        response = f"```fix\nan error occurred: {str(e)}```"
        log(f"Error occurred while restarting: {e}", level="error")

    # discordにメッセージ送信
    if not response or response.isspace():
        response = "```Execution completed successfully, but the result is empty```"
    await message.channel.send(response)
