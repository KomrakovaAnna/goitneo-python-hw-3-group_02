from datetime import datetime
from error_handler import BirthdayValueError


class Birthday:
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise BirthdayValueError

    def __getvalue__(self):
        return self.value
