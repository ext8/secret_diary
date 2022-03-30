"""sced lock :: command"""
import click
from Exceptions import ConfigMissing

from utils import ConfigCheck
from utils import SQLog
from utils import ZipUtil

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
    help="lock your private diary",
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

    if ConfigCheck.verify(directory):

        _zip.compress(directory=directory, password=password)

        with SQLog() as cur:
            cur

    else:
        raise ConfigMissing(directory)
