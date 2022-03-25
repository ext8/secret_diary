def util_get_command(command_item):
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
