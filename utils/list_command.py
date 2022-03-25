import os


def util_list_command(folder: str):

    command_items = []
    command_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../app/{folder}"))

    for file in os.listdir(f"{command_dir}"):
        if file.endswith(".py") and not file.startswith("__"):
            command_items.append(file[:-3])
        command_items.sort()
    return command_items
