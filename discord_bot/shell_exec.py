import os
import subprocess


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
        os.chdir(output_dir)

        # 実行コマンドを出力
        # await message.channel.send(f"```$ {' '.join(map(str, args))}```")

        # 実行（shell=Falseの場合）
        # args = shlex.split(command_text)
        # result = subprocess.run(args, shell=False, text=True, capture_output=True)

        # 実行（shell=Trueの場合）
        result = subprocess.run(command_text, shell=True, text=True, capture_output=True)
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stdout:
            response += f"```STDOUT:\n{stdout}```"
        if stderr:
            # markdownではcss使用できないため、シンタックスハイライトでfixを指定する（これはdiscordでは文字色が青になる） 実行時エラーも同様
            response += f"```fix\nSTDERR:\n{stderr}```"

    # 実行時エラー
    except Exception as e:
        response += f"```fix\nEXECUTE ERROR:\n{e}```"

    # discordにメッセージ送信
    if not response or response.isspace():
        response = "```Execution completed successfully, but the result is empty```"
    await message.channel.send(response)
