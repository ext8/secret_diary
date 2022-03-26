import os

class CmdUtil():

    def get(self,command_item: str) -> None:
        """
        get :: loads click commands from /app/commands
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


    def list(self,folder: str) -> list:
        """
        list :: lists all files in app/commands
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
