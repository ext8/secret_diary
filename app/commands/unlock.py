"""secd unlock :: command"""

import click

from utils import SQLog, TimeUtil, ZipUtil


class Context:
    """add:
    ```py
    ctx.object = Context(file)
    ```"""

    def __init__(self, file) -> None:
        self.file = file


@click.command()
@click.option(
    "-f",
    "--file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
    ),
)
@click.option("-p", "--password", prompt=True, hide_input=True, type=str)
@click.pass_context
def main(ctx, file: str, password: str):
    """
    unlocks diary

    secd unlock -f {file} -p {password}
    """
    """
    Args:
        ctx : Context
        file (str): name of archive
        password (str): password of archive
    """

    ctx.object = Context(file)

    ZipUtil.extract(password, file)

    with SQLog("./diary//.sec.d//logs//time-stamp.db") as cur:
        cur.execute(
            "INSERT INTO time_stamp VALUES(?,?,?)",
            (2, TimeUtil.date_now(), TimeUtil.time_now()),
        )
