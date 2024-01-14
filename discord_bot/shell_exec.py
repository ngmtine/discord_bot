import os
import subprocess

from util.log import log
from util.split_message import split_message


# シェル実行
async def shell_exec(message):
    command_text = message.content[len("$sh ") :]
    responses = []
    original_dir = os.getcwd()
    output_dir = os.path.join(original_dir, "output")

    try:
        # ディレクトリ作成
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log(f"Created directory: {output_dir}", level="info")

        # 実行
        log(f"Executing command: {command_text}", level="info")
        result = subprocess.run(command_text, shell=True, text=True, capture_output=True, cwd=output_dir)
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stdout:
            stdouts = split_message(f"STDOUT:\n{stdout}")
            responses.extend(f"```{i}```" for i in stdouts)
            log(f"STDOUT: {stdout}", level="info")
        if stderr:
            # markdownではcss使用できないため、シンタックスハイライトでfixを指定する（これはdiscordでは文字色が青になる） 実行時エラーも同様
            stderrs = split_message(f"STDERR:\n{stderr}")
            responses.extend(f"```fix\n{i}```" for i in stderrs)
            log(f"STDERR: {stderr}", level="error")

    # 実行時エラー
    except Exception as e:
        errorstrs = split_message(f"EXECUTE ERROR:\n{str(e)}")
        responses.extend(f"```fix\n{i}```" for i in errorstrs)
        log(f"Execution error: {e}", level="error")

    # レスポンス空の場合
    if not responses or all(res.isspace() for res in responses):
        responses.extend(["```Execution completed successfully, but the result is empty```"])

    # discordにメッセージ送信
    for res in responses:
        await message.channel.send(res)
    log("Message sent to Discord", level="info")
