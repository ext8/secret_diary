"""sced init :: command"""
import click

from utils import NewDiary, SQLog, TimeUtil


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
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    help="creates a diary at given directory",
)
@click.pass_context
def main(ctx, directory: str) -> None:
    """
    creates config files

    Args:
        ctx : Context
        directory (str): directory to gen config files
    """
    ctx.object = Context(directory)

    NewDiary.make(directory)

    with SQLog(f"{directory}//.sec.d//logs//time-stamp.db") as cur:

        """timestamps for opening / closing diary


        sqlite3> | LogType 	 | DateNow 	 | TimeNow 	|
                 | --------- | --------- | -------- |
                 | 0   	     | 1-11-2022 | 11:51 	|
        """

        cur.execute("CREATE TABLE time_stamp (LogType text,DateNow int,TimeNow int)")
        cur.execute(
            "INSERT INTO time_stamp VALUES (?, ?, ?)",
            (0, TimeUtil.date_now(), TimeUtil.time_now()),
        )
