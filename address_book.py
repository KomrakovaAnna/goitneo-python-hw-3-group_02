from collections import UserDict
from record import Record
from error_handler import NotFoundError, NoBirthdayError
from datetime import datetime, timedelta
from collections import defaultdict
import calendar


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return f"{record.name.value} added"

    def find(self, name):
        if name in self.data:
            return self.data[name]
        raise NotFoundError

    def show_all(self):
        line = ""
        for name in self.data:
            line += name + ": " + self.data[name].phone.value + "\n"
        return line

    def get_birthdays_per_week(self):
        birthdays_list = defaultdict(list)

        for name in self.data:
            if self.data[name].birthday == None:
                continue

            today = datetime.now()
            current_day_of_week = today.weekday()
            monday_of_current_week = today - timedelta(days=current_day_of_week)
            monday_of_current_week = monday_of_current_week.date()
            birthday = self.data[name].birthday.value

            birthday_this_year = birthday.replace(year=monday_of_current_week.year)

            if birthday_this_year < monday_of_current_week:
                (birthday.replace(year=monday_of_current_week.year + 1))
            delta_days = (birthday_this_year - monday_of_current_week).days
            delta_days_with_week_days = delta_days
            if delta_days == -1 or delta_days == -2:
                delta_days_with_week_days = 0
            if 0 <= delta_days < 5:
                if calendar.day_name[delta_days_with_week_days] in birthdays_list:
                    birthdays_list[calendar.day_name[delta_days_with_week_days]].append(
                        name
                    )
                else:
                    birthdays_list[calendar.day_name[delta_days_with_week_days]] = [
                        name
                    ]
        if len(birthdays_list) == 0:
            print("No birthdays this week")
        else:
            for key, value in dict(birthdays_list).items():
                print("{}: {}".format(key, ", ".join(value)))
