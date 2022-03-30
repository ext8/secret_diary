import os


class ConfigCheck:
    @staticmethod
    def verify(path: str):
        return os.path.exists(f"{path}/.sec.d")
