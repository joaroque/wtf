import os


def get_previous_command(history_file_file):
    with open(os.path.expanduser(history_file_file), "r") as file:
        lines = file.readlines()

    if len(lines) < 2:
        raise ValueError("Empyt history file")

    last_command = lines[-2].strip().split(";")[-1]

    return last_command
