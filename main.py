from address_book import AddressBook
from record import Record
from error_handler import NotFoundError
from command_handler import CommandHandler


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    command_handler = CommandHandler()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print("Enter a command: ")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            command_handler.add(args, book)

        elif command == "all":
            command_handler.all(book)

        elif command == "phone":
            command_handler.phone(args, book)

        elif command == "change":
            command_handler.change(args, book)

        elif command == "add-birthday":
            command_handler.add_birthday(args, book)

        elif command == "show-birthday":
            command_handler.show_birthday(args, book)

        elif command == "birthdays":
            command_handler.birthdays(book)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
