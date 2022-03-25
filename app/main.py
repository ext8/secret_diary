#!/usr/bin/env python

import os
import sys

import click

from utils import util_list_command, util_get_command


class SecretDiary(click.MultiCommand):
    def list_commands(self, ctx):
        return util_list_command("commands")

    def get_command(self, ctx, name):
        return util_get_command(name)


@click.command(cls=SecretDiary)
def main():
    """lorem ipsum dolar sit amet."""
    pass
