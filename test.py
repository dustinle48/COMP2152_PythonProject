import os
PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = "calendar.txt"


def command_help():
    """
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 : 
            start : 08:00, 
			end : 09:00,
			title : Eye doctor

            start : 12:30,
			end : 13:00,
			title : lunch with sid

			start : 18:00,
			end : 19:00, 
			title : dinner with jane
        2018-10-29 : 
            start : 10:00,
			end : 11:00,
			title : Change oil in blue car

            start : 12:00,
			end : 14:00,
			title : Fix tree near front walkway

            start : 18:00,
			end : 19:00,
			title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 : 
            start : 18:00,
			end : 22:00,
			title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me


def command_add(date, start_time, end_time, title, calendar):
    if date in calendar:
        return False
    else:
        calendar[date] = {'start': start_time, 'end': end_time, 'title': title}
        save_calendar(calendar)
        print("Event added!")
        return True


def command_show(calendar):
    for x, y in calendar.items():
        print(x, ":")
        for z in y:
            print("\t" + z + " :", y[z])


def command_delete(date, start_time, calendar):
    if date in calendar:
        for x in calendar[date].copy():
            if calendar[date][x] == start_time:
                del calendar[date]
                save_calendar(calendar)
                print("Event deleted!")
                return True
            else:
                return "There is no event with start time of " + start_time + " on date " + date + " in the calendar"
    else:
        return date + " is not a date in the calendar"


def save_calendar(calendar):
    os.remove(FILENAME)
    for x, y in calendar.items():
        input = x
        for z in y:
            input += " " + y[z]
        with open(FILENAME, "a") as file:
            file.write(input)
            file.write("\n")
    print("Calendar saved!")


def load_calendar():
    calendar_temp = {}
    with open(FILENAME, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split(" ", 1)
            detail = line[1].split(" ", 2)
            calendar_temp[line[0]] = {'start': detail[0], 'end': detail[1], 'title': detail[2]}
    return calendar_temp

# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    string = command.split()
    cmd = string[0]
    if cmd in ['add', 'delete', 'quit', 'help', 'show']:
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
            if (int(month) in [1, 3, 5, 7, 8, 10, 12] and (1 <= int(day) <= 31)) or (int(month) in [2, 4, 6, 9, 11] and (1 <= int(day) <= 30)):
                return True
    return False


def is_natural_number(str):
    char = list(str)
    for i in char:
        if 48 <= ord(i) <= 57:
            continue
        else:
            return False
    return True


def parse_command(line):
    string = line.split(" ", 4)
    command = string[0]
    check = is_command(command)

    if check is True:
        if command == "add":
            if len(string) == 5:
                date = string[1]
                start_time = string[2]
                end_time = string[3]
                title = string[4]
                date_check = is_calendar_date(date)
                start_check = is_natural_number(start_time)
                end_check = is_natural_number(end_time)
                if date_check is True:
                    if (0 <= int(start_time) <= 24) and (0 <= int(end_time) <= 24) and (int(start_time) <= int(end_time)) and (start_check and end_check) is True:
                        return ['add', date, start_time, end_time, title]
                    else:
                        return ['error', 'not a valid event start time']
                else:
                    return ['error', 'not a valid calendar date']
            else:
                return ['error', 'add DATE START_TIME END_TIME DETAILS']
        elif command == "delete":
            if len(string) == 3:
                date = string[1]
                start_time = string[2]
                date_check = is_calendar_date(date)
                start_check = is_natural_number(start_time)
                if date_check is True:
                    if 0 <= int(start_time) <= 24 and start_check is True:
                        return ['delete', date, start_time]
                    else:
                        return ['error', 'not a valid event start time']
                else:
                    return ['error', 'not a valid calendar date']
            else:
                return ['error', 'delete DATE START_TIME']
        elif command == "quit":
            if len(string) == 1:
                return ['quit']
            else:
                return ['error', 'show']
        elif command == "help":
            if len(string) == 1:
                return ['help']
            else:
                return ['error', 'help']
        elif command == "show":
            if len(string) == 1:
                return ['show']
            else:
                return ['error', 'show']
    else:
        return ['help']


if __name__ == "__main__":
    import doctest
    doctest.testmod()