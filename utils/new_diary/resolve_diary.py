import os


def util_new_diary(directory: str):

    # config dir -> .sec.d
    config_dir = f"{directory}//.sec.d"
    os.mkdir(config_dir)

    config_subdir = ["logs", "meta-data", "stats"]

    for file in config_subdir:
        os.mkdir(f"{config_dir}//{file}")

    return str(config_dir),list(config_subdir)