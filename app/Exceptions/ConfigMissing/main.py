class ConfigMissing(Exception):
    def __init__(self, path) -> None:
        """
        Args:
            path (str): path to diary
        """
        self.path = path

    def __str__(self) -> str:
        return f""" configuration not found on path: {self.path}
    Run `secd init` to generate configurations."""
