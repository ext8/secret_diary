"""TimeUtil Class to format time,date in text and table"""

from datetime import date, datetime


class TimeUtil:
    """Format time,date in text & table"""

    __all__ = ["date_now", "time_now"]

    @staticmethod
    def date_now() -> str:
        """gives date.today"""
        return date.today()

    @staticmethod
    def time_now() -> str:
        """gives datetime.now()"""
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def time_table() -> str:
        """Note: not implemented yet\n
        gives ascii table with timestamps"""
        # in progress
        return
