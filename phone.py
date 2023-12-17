from field import Field
from error_handler import PhoneValueError


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise PhoneValueError
        super().__init__(value)

    def __getvalue__(self):
        return self.value
