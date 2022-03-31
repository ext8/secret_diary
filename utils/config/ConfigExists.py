import os


class ConfigExists:
    @staticmethod
    def verify(path: str):
        return os.path.exists(f"{path}/.sec.d")
