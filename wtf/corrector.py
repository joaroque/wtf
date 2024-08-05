import os

import typer


def corrector(command):
    try:
        cmd = command.command
        run = typer.confirm(f"{cmd}", abort=True)
        execute_command(cmd)

    except Exception as e:
        typer.Exit(1)


def execute_command(command):
    os.system(command)
