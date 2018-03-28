#!/usr/bin/env python3
"""

Title:
Number of Days

Description:
Your program should take two string inputs from the user
in the format (dd/mm/yyyy)
and calculate the number of days between those two dates.
Submitted by Kanishk
"""


def number_of_days(date1: str, date2: str) -> int:
    """Return the number of days between two dates."""
    if date1 == date2:
        return 0
    days_between = 0
    month_dictionary = {1: 31,
                        2: 28,
                        3: 31,
                        4: 30,
                        5: 31,
                        6: 30,
                        7: 31,
                        8: 31,
                        9: 30,
                        10: 31,
                        11: 30,
                        12: 31}
    date1_split = date1.split("/")
    date2_split = date2.split("/")
    day1 = int(date1_split[0])
    day2 = int(date2_split[0])
    month1 = int(date1_split[1])
    month2 = int(date2_split[1])
    year1 = int(date1_split[2])
    year2 = int(date2_split[2])

    if year1 > year2:
        year = year2
        while year < year1:
            # check for leap years
            if year % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    days_between += 365
                else:
                    days_between += 366
            else:
                days_between += 365
            year += 1
        if month1 > month2:
            months_between = [month for month in range(0, 13)
                              if month1 > month >= month2]
            days_between += sum([month_dictionary[month]
                                 for month in months_between])
        elif month2 > month1:
            months_between = [month for month in range(0, 13)
                              if month2 > month >= month1]
            days_between -= sum([month_dictionary[month]
                                 for month in months_between])
        days_between += day1 - day2
    elif year2 > year1:
        year = year1
        while year < year2:
            # check for leap years
            if year % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    days_between += 365
                else:
                    days_between += 366
            else:
                days_between += 365
            year += 1
        if month2 > month1:
            months_between = [month for month in range(0, 13)
                              if month2 > month >= month1]
            days_between += sum([month_dictionary[month]
                                 for month in months_between])
        elif month1 > month2:
            months_between = [month for month in range(0, 13)
                              if month1 > month >= month2]
            days_between -= sum([month_dictionary[month]
                                 for month in months_between])
        days_between += day2 - day1
    else:
        if month1 > month2:
            months_between = [month for month in range(0, 13)
                              if month1 > month >= month2]
            days_between += sum([month_dictionary[month]
                                 for month in months_between])
            days_between += day1 - day2
        elif month2 > month1:
            months_between = [month for month in range(0, 13)
                              if month2 > month >= month1]
            days_between += sum([month_dictionary[month]
                                 for month in months_between])
            days_between += day2 - day1
        else:
            days_between += max(day1, day2) - min(day1, day2)

    return days_between


def _start():
    """Start program interactively."""
    date1 = input("Please type in the first date: ")
    date2 = input("Please type in the second date: ")

    print(f"The number of days between {date1} and {date2} "
          f"is {number_of_days(date1, date2)}.")


if __name__ == "__main__":
    _start()
