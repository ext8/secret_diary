import click
from utils import util_new_diary,SQLog


class Context:
    def __init__(self, directory) -> None:
        self.directory = directory


@click.command()
@click.option(
    "-d",
    "--directory",
    default=".",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    help="creates a diary at given directory",
)
@click.pass_context
def main(ctx, directory: str) -> None:
    """create or reinitialize sec.d repo"""
    ctx.object = Context(directory)

    config_dir , config_subdir = util_new_diary(directory=directory)
