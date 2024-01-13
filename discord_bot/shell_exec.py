import shlex
import subprocess


# シェル実行
async def shell_exec(message):
    command_text = message.content[len("$sh ") :]
    try:
        args = shlex.split(command_text)
        print(args)
        output = subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.output}"

    # 結果の送信
    await message.channel.send(f"```\n{output}\n```")
