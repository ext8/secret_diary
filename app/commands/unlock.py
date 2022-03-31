"""secd unlock :: command"""
import time

import click

from utils import SQLog, ZipUtil

_zip = ZipUtil()


class Context:
    """add:
    ```py
    ctx.object = Context(file)
    ```"""

    def __init__(self, file) -> None:
        """
        secd unlock -f {file}

        Args:
            file (str): name of archive
        """
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
        help="unlock archive",
    ),
)
@click.option("-p", "--password", prompt=True, hide_input=True, type=str)
@click.pass_context
def main(ctx, file: str, password: str) -> None:
    """```

    secd unlock -f {file} -p {password}
    ```
    Args:
        ctx : Context
        file (str): name of archive
        password (str): password of archive
    """

    unix_time_file = "./diary//.sec.d//logs//time-stamp.db"

    unix_time = int(time.time())

    ctx.object = Context(file)

    _zip.extract(password, file)

    with SQLog(unix_time_file) as cur:
        cur.execute("INSERT INTO time_stamp VALUES(?,?,?)", (3, "unlock", unix_time))
