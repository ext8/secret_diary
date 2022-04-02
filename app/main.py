#!/usr/bin/env python

"""
SecretDiary or secd , your private diary
"""


__author__ = "ext8"
__version__ = "0.1.0"
__license__ = "MIT"


import click

from utils import CmdUtil

Command = CmdUtil()


class SecretDiary(click.MultiCommand):
    """Base class for secret-diary"""

    def list_commands(self, ctx):
        return Command.list(folder="commands")

    def get_command(self, ctx, name):
        return Command.get(command_item=name)


@click.command(cls=SecretDiary)
def main():
    """lorem ipsum dolar sit amet."""
    pass


if __name__ == "__main__":
    main()
