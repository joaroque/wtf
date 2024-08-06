from os import path

import huepy as hue
import typer
from dotenv import load_dotenv

from wtf.corrector import corrector
from wtf.llms.openai import OpenaiLLM
from wtf.shell.get_command import get_previous_command
from wtf.shell.get_error import get_error
from wtf.utils.models import ConsoleCommand, ErrorMessage
from wtf.utils.prompt import EXPLAINER_PROMPT, RERUN_PROMPT

load_dotenv()

USER_LANGUAGE = "pt-PT"
RESPONSE_FORMAT = "plain/text"

home_directory = path.expanduser("~")
ZSH_HISTORY = path.join(home_directory, ".zsh_history")
ERROR_FILE = path.join(home_directory, "zsh_error_log.txt")

app = typer.Typer(
    help="A powerful app that uses AI to provide human-readable terminal errors.",
)
app.pretty_exceptions_enable = False


@app.command(help="Explain the previous terminal error")
def wtf():
    try:
        last_error = get_error(ERROR_FILE)
    except Exception as e:
        print(hue.bad(f"{e}"))
        raise typer.Abort()

    wtf = OpenaiLLM(
        prompt=EXPLAINER_PROMPT,
        output_model=ErrorMessage,
        language=USER_LANGUAGE,
    )

    explainer = wtf(last_error)
    ohhh = OpenaiLLM.format_output(explainer)
    print(ohhh)


@app.command(name="f ", help="Rerun the last command")
@app.command(name="fuck", help="Rerun the last command")
def rerun():
    try:
        last_command = get_previous_command(ZSH_HISTORY)
    except Exception as e:
        print(hue.bad(f"{e}"))
        raise typer.Abort()

    wtf = OpenaiLLM(
        prompt=RERUN_PROMPT,
        output_model=ConsoleCommand,
        language=USER_LANGUAGE,
        response_format=RESPONSE_FORMAT,
    )

    command = wtf(last_command)
    corrector(command)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        ctx.invoke(wtf)


if __name__ == "__main__":
    app()
