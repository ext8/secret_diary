import sqlite3


class SQLog(object):
    """SecretDiary :: sqlite3 context manager"""

    # credits :: https://gist.github.com/miku/6522074

    def __init__(self, path) -> None:
        self.path = path

    def __enter__(self) -> None:
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback) -> None:
        self.conn.commit()
        self.conn.close()
