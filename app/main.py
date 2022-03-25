#!/usr/bin/env python

"""
SecretDiary or secd , your private diary
"""


__author__ = "ext8"
__version__ = "0.1.0"
__license__ = "MIT"


import click

from utils import util_get_command, util_list_command


class SecretDiary(click.MultiCommand):
    """Base class for secret-diary"""

    def list_commands(self, ctx):
        return util_list_command("commands")

    def get_command(self, ctx, name):
        return util_get_command(name)


@click.command(cls=SecretDiary)
def main():
    """lorem ipsum dolar sit amet."""
    pass
