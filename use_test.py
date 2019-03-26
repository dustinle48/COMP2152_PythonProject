import test as calendar
from test import *


def main():
    # load calendar from txt file
    calendar = load_calendar()

    # enter a loop
    while True:
        cmd = input("Please enter a command: ")

        # run is_command function
        check = is_command(cmd)

        if check is True:
            # run parse_command function
            command = parse_command(cmd)
            action = command[0]
            print(command)
            if action == "add":
                command_add(command[1], command[2], command[3], command[4], calendar)
            elif action == "delete":
                command_delete(command[1], command[2], calendar)
            elif action == "help":
                command_help()
            elif action == "show":
                command_show(calendar)
            elif action == "quit":
                break
        else:
            print("Invalid command")
    print("------------------------------")
    print("Bye!")


if __name__ == "__main__":
    main()