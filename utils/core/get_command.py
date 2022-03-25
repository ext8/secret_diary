"""
utils.util_get_command :: loads click commands from /app/commands
"""


def util_get_command(command_item: str) -> None:
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
