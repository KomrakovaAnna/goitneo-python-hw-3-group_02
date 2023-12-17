from error_handler import (
    NotFoundError,
    PhoneValueError,
    BirthdayValueError,
    NoBirthdayError,
)
from record import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundError:
            print("Contact was not found")
        except ValueError:
            print("Incorrect input. Add name and value")
        except IndexError:
            print("Incorrect data. Input name")
        except KeyError:
            print("Incorrect key")
        except PhoneValueError:
            print("Enter correct phone number")
        except BirthdayValueError:
            print("Incorrect data format, should be DD.MM.YYYY")
        except NoBirthdayError:
            print("Contact has not saved bithday")

    return inner


class CommandHandler:
    @input_error
    def add(self, args, book):
        name, phone = args
        record = Record(name, phone)
        print(book.add_record(record))

    @input_error
    def all(self, book):
        print(book.show_all())

    @input_error
    def phone(self, args, book):
        name = args[0]
        print(book.find(name).phone.value)

    @input_error
    def change(self, args, book):
        name, phone = args
        record = book.find(name)
        record.edit_phone(phone)
        print("Phone has been edited")

    @input_error
    def add_birthday(self, args, book):
        name, birthday = args
        record = book.find(name)
        record.add_birthday(birthday)
        print("Birthday has been added")

    @input_error
    def show_birthday(self, args, book):
        name = args[0]
        record = book.find(name)
        if record.birthday == None:
            raise NoBirthdayError
        print(record.show_birthday())
        
        

    @input_error
    def birthdays(self, book):
        book.get_birthdays_per_week()
