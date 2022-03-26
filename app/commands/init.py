import click
import time
from utils import NewDiary, SQLog

diary = NewDiary()


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

    CONFIG_DIR, CONFIG_SUBDIR = diary.make(directory=directory)

    UNIX_TIME_FILE = f"{CONFIG_DIR}//{CONFIG_SUBDIR[0]}//time-stamp.db"

    UNIX_TIME = int(time.time())

    """
    timestamps for opening / closing diary

    sqlite> | SrNo 	| LogType 	| UnixTime 	|
            |------	|--------	|----------	|
            | 1.   	| Open   	| 83451751 	|
    """
    with SQLog(UNIX_TIME_FILE) as c:

        c.execute("CREATE TABLE time_stamp ( SrNo int,LogType text,UnixTime int)")
        c.execute("INSERT INTO time_stamp VALUES (?, ?)", (1, "Open", UNIX_TIME))
