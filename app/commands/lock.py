"""sced lock :: command"""


import click

from utils import ConfigExists, SQLog, TimeUtil, ZipUtil


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
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        resolve_path=True,
    ),
)
@click.option("-p", "--password", prompt=True, hide_input=True, type=str)
@click.pass_context
def main(ctx, directory: str, password: str):
    """
    locks diary

    secd lock -d {directory} -p {password}
    """
    """
    Args:
        ctx : Context
        directory (str): directory to archive
        password (str): password to archived directory
    """
    ctx.object = Context(directory)

    if ConfigExists.verify(directory):

        with SQLog(f"{directory}//.sec.d//logs//time-stamp.db") as cur:
            cur.execute(
                "INSERT INTO time_stamp VALUES(?,?,?)",
                (1, TimeUtil.date_now(), TimeUtil.time_now()),
            )

        ZipUtil.compress(directory=directory, password=password)

    else:
        raise ConfigMissing(directory)
