MAX_LENGTH = 2000 - 20  # 文字列最大長（これを超えるとmessage.channel.sendがエラー起こす）


def split_message(message, max_length=MAX_LENGTH):
    """文字列を指定された最大長で分割"""
    return [message[i : i + max_length] for i in range(0, len(message), max_length)]
