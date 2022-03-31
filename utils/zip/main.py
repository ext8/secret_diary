"""compress and extract 7z file class for secd"""
import os

import py7zr


class ZipUtil:
    """add:
    ```py
    from Utils import ZipUtil
    ```"""

    @staticmethod
    def compress(password: str, directory=".", file="archive.7z"):
        """
        Util to make archives

        Args:
            password (str): password to newly made archive
            directory (str, optional): dir to archive. Default -> "."
            file (str, optional): name of new archive. Default -> "archive.7z"
        """
        with py7zr.SevenZipFile(file, "w", password=password) as _7zip:
            _7zip.writeall(directory)

    @staticmethod
    def extract(password: str, file="archive.7z"):
        """
        Util to extract archives

        Args:
            password (str): password to unlock archive
            file (str, optional): file-name of archive. Default -> "archive.7z"
        """
        with py7zr.SevenZipFile(file, "r", password=password) as _7zip:
            os.mkdir("diary")
            _7zip.extractall(path="diary")
