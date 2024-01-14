import shutil


def is_command_available(command):
    return shutil.which(command) is not None
