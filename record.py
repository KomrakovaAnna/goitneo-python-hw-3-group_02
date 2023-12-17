from name import Name
from phone import Phone
from birthday import Birthday


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = None

    def edit_phone(self, phone):
        self.phone = Phone(phone)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        return self.birthday.value

    def __getname__(self):
        return self.name

    def __getphone__(self):
        return self.phone

    def __getbirthday__(self):
        return self.birthday

    def __str__(self):
        return f"Contact name: {self.name.value}, phone: {self.phone.value}"
