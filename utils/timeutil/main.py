""" """
from datetime import date, datetime

__all__ = ["DateNow", "TimeNow"]


class TimeUtil:
    """ """

    @staticmethod
    def DateNow() -> str:
        """ """
        return date.today()

    @staticmethod
    def TimeNow() -> str:
        """ """
        return datetime.now().strftime("%H:%M:%S")

    def TimeTable() -> str:
        """ """
        # in progress
        pass
