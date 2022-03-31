"""`CmdUtil` class object for loading and listing all *.py files in app/commands"""

import os


class CmdUtil:
    """`get()` loads all commands files \n
    `list()` lists all command files"""

    @staticmethod
    def get(command_item: str) -> None:
        """
        loads click commands from app/commands
        """
        try:
            mod = __import__(
                name=f"app.commands.{command_item}",
                locals=None,
                globals=None,
                fromlist=["main"],
            )
        except ImportError:
            return
        return mod.main

    @staticmethod
    def list(folder: str) -> list:
        """
        lists all files in app/commands
        """
        command_items = []
        command_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f"../../app/{folder}")
        )

        for file in os.listdir(f"{command_dir}"):
            if file.endswith(".py") and not file.startswith("__"):
                command_items.append(file[:-3])
            command_items.sort()
        return command_items
