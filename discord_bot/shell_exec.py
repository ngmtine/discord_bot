import shlex
import subprocess


# シェル実行
async def shell_exec(message):
    command_text = message.content[len("$sh ") :]

    try:
        # 入力を分割
        args = shlex.split(command_text)

        # 実行コマンドを出力
        print(args)
        await message.channel.send(f"```$ {' '.join(map(str, args))}```")

        # 実行
        result = subprocess.run(args, shell=False, text=True, capture_output=True)
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

    # 実行時エラー
    except Exception as e:
        # markdownではcss使用できないため、シンタックスハイライトでfixを指定する（これはdiscordでは文字色が青になる） 標準エラー出力も同様
        await message.channel.send(f"```fix\nEXECUTE ERROR:\n{e}```")

    # 標準出力
    if stdout:
        await message.channel.send(f"```STDOUT:\n{stdout}```")

    # 標準エラー出力
    if stderr:
        await message.channel.send(f"```fix\nSTDERR:\n{stderr}```")
