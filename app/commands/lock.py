"""sced lock :: command"""
import time

import click
from Exceptions import ConfigMissing

from utils import ConfigCheck, SQLog, ZipUtil

_zip = ZipUtil()


class Context:
    """add:
    ```py
    ctx.object = Context(directory)
    ```"""

    def __init__(self, directory) -> None:
        """```\n
        secd lock -d {directory}\n```

        Args:
            directory (str): directory to archive
        """
        self.directory = directory


@click.command()
@click.option(
    "-d",
    "--directory",
    default="",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        resolve_path=True,
    ),
    help="lock archive",
)
@click.option("-p", "--password", prompt=True, hide_input=True, type=str)
@click.pass_context
def main(ctx, directory: str, password: str) -> None:
    """```\n
    secd lock -d {directory} -p {password}\n```

    Args:
        ctx : Context
        directory (str): directory to archive
        password (str): password to archived directory
    """
    ctx.object = Context(directory)

    unix_time_file = f"{directory}//.sec.d//logs//time-stamp.db"

    unix_time = int(time.time())

    if ConfigCheck.verify(directory):

        with SQLog(unix_time_file) as cur:
            cur.execute("INSERT INTO time_stamp VALUES(?,?,?)", (2, "lock", unix_time))

        _zip.compress(directory=directory, password=password)

    else:
        raise ConfigMissing(directory)
