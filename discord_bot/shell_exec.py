import os
import subprocess

from util.log import log


# シェル実行
async def shell_exec(message):
    command_text = message.content[len("$sh ") :]
    response = ""
    original_dir = os.getcwd()
    output_dir = os.path.join(original_dir, "output")

    try:
        # 移動
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log(f"Created directory: {output_dir}", level="info")
        os.chdir(output_dir)

        # 実行コマンドを出力
        # await message.channel.send(f"```$ {' '.join(map(str, args))}```")

        # 実行（shell=Falseの場合）
        # args = shlex.split(command_text)
        # result = subprocess.run(args, shell=False, text=True, capture_output=True)

        # 実行（shell=Trueの場合）
        log(f"Executing command: {command_text}", level="info")
        result = subprocess.run(command_text, shell=True, text=True, capture_output=True)
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stdout:
            response += f"```STDOUT:\n{stdout}```"
            log(f"STDOUT: {stdout}", level="info")
        if stderr:
            # markdownではcss使用できないため、シンタックスハイライトでfixを指定する（これはdiscordでは文字色が青になる） 実行時エラーも同様
            response += f"```fix\nSTDERR:\n{stderr}```"
            log(f"STDERR: {stderr}", level="error")

    # 実行時エラー
    except Exception as e:
        response += f"```fix\nEXECUTE ERROR:\n{e}```"
        log(f"Execution error: {e}", level="error")

    # discordにメッセージ送信
    if not response or response.isspace():
        response = "```Execution completed successfully, but the result is empty```"
    await message.channel.send(response)
    log("Message sent to Discord", level="info")
