class InvalidData(Exception):
    def __init__(self, path) -> None:
        self.path = path

    def __str__(self) -> str:
        return f"""stats or data is either invalid or corrupted.
              run "secd init" after deleting the contents of "{self.path}/.sec.d/" """
