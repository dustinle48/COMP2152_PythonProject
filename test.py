import os
import Calendar as calendar
PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = "calendar.txt"

def command_add(date, start_time, end_time, title, calendar):
    input = date + " " + start_time + " " + end_time + " " + title
    with open(FILENAME, "a") as file:
        file.write(input)
        file.write("\n")
    print("Event added!")

def command_show(calendar):
    for x, y in calendar.items():
        detail = y.split(" ", 2)
        start = detail[0]
        end = detail[1]
        title = detail[2]
        print(x,":")
        print("\tstart :",start+":00")
        print("\tend :", end+":00")
        print("\ttitle :", title)

def command_delete(date, calendar):
    calendar.pop(date)
    print("Event deleted!")

def save_calendar(calendar):
    os.remove(FILENAME)
    for x, y in calendar.items():
        detail = y.split(" ", 2)
        start_time = detail[0]
        end_time = detail[1]
        title = detail[2]
        input = x + " " + start_time + " " + end_time + " " + title
        with open(FILENAME, "a") as file:
            file.write(input)
            file.write("\n")
    print("Calendar saved!")

def load_calendar():
    calendar = {}
    with open(FILENAME, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split(" ", 1)
            calendar[line[0]] = line[1]

def is_command(command):
    string = command.split(" ", 4)
    cmd = ""
    date = ""
    start_time = ""
    end_time = ""
    title = ""

    if len(string) == 1:
        cmd = string[0]
    elif len(string) == 2:
        cmd = string[0]
        date = string[1]
    elif len(string) > 2:
        cmd = string[0]
        date = string[1]
        start_time = string[2]
        end_time = string[3]
        title = string[4]

    if cmd == "add" or cmd == "show" or cmd == "delete" or cmd == "quit":
        return True
    else:
        return False

def is_calendar_date(date):
    date_data = date.split("-", 3)
    year = date_data[0]
    month = date_data[1]
    day = date_data[2]
    year_check = is_natural_number(year)
    month_check = is_natural_number(month)
    day_check = is_natural_number(day)
    if (year_check and month_check and day_check) is True:
        if len(list(year)) == 4 and len(list(month)) == 2 and len(list(day)) == 2:
            if (int(month) in [1,3,5,7,8,10,12] and (1 <= int(day) <= 31)) or (int(month) in [2,4,6,9,11] and (1 <= int(day) <= 30)):
                return True
    return False

def is_natural_number(str):
    char = list(str)
    for i in char:
        if 48 <= ord(i) <= 56:
            continue
        else:
            return False
    return True

def parse_command(line):
    string = line.split(" ", 4)
    command = ""
    date = ""
    start_time = ""
    end_time = ""
    title = ""

    if len(string) == 1:
        command = string[0]
        if command == "show":
            return ['show']
        elif command == "help":
            return ['help']
        elif command == "quit":
            return ['quit']
        else:
            return ['help']
    elif len(string) == 3:
        command = string[0]
        date = string[1]
        start_time = string[2]
        if command == "delete":
            return ['delete',date,start_time]
        else:
            return ['help']
    elif len(string) == 5:
        command = string[0]
        date = string[1]
        start_time = string[2]
        end_time = string[3]
        title = string[4]
        if command == "add":
            return ['add', date, start_time, end_time, title]
        else:
            return ['help']
    else:
        return ['help']

if __name__ == "__main__":
    import doctest
    doctest.testmod()