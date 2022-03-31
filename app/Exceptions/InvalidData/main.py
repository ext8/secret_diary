"""Error Class to raise when *.db files are corrupted or missing"""


class InvalidData(Exception):
    """
    Corrupted or missing data.

    Args:
        Exception (class)
    """

    def __init__(self, path) -> None:
        self.path = path

    def __str__(self) -> str:
        return f"""stats or data is either invalid or corrupted.
              run "secd init" after deleting the contents of "{self.path}/.sec.d/" """
