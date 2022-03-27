"""sced init :: command"""
import time

import click

from utils import NewDiary
from utils import SQLog

diary = NewDiary()


class Context:
    """sced init -d DIRECTORY :: context"""

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

    config_dir, config_subdir = diary.make(directory=directory)

    unix_time_file = f"{config_dir}//{config_subdir[0]}//time-stamp.db"

    unix_time = int(time.time())

    with SQLog(unix_time_file) as cur:

        """timestamps for opening / closing diary

        sqlite> | SrNo 	| LogType 	| UnixTime 	|
                |------	|--------	|----------	|
                | 1.   	| Open   	| 83451751 	|
        """

        cur.execute("CREATE TABLE time_stamp ( SrNo int,LogType text,UnixTime int)")
        cur.execute("INSERT INTO time_stamp VALUES (?, ?, ?)", (1, "Open", unix_time))
