import os


class NewDiary:
    """Generates new diary file structure"""

    @staticmethod
    def make(directory: str):

        config_dir = f"{directory}//.sec.d"

        config_subdir = ["logs", "meta-data", "stats"]

        os.mkdir(config_dir)

        for file in config_subdir:
            os.mkdir(f"{config_dir}//{file}")

        return str(config_dir), list(config_subdir)
