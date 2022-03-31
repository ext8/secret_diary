"""secd stats :: command"""
import click

from utils import SQLog  # , TimeUtils


class Context:
    """add:
    ```py
    ctx.object = Context(directory)
    ```"""

    def __init__(self, directory) -> None:
        self.directory = directory


@click.command()
@click.option(
    "-d",
    "--directory",
    default=".",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    help="displays statistcs",
)
@click.pass_context
def main(ctx, directory: str):
    """
    gives statistcs on diary

    Args:
        ctx : Context
        directory (str): diary directory
    """
    ctx.object = Context(directory)

    with SQLog(f"{directory}//.sec.d//logs//time-stamp.db") as cur:
        cur.execute()
    # print(list(list(zip(*data))[0]))
