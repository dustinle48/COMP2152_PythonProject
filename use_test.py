import os
import test as calendar
from test import *

def main():
    while True:
        x = input("Cac :")
        print(is_calendar_date(x))
    '''
    # load calendar from txt file
    load_calendar()
    # enter a loop
    while True:
        cmd = input("Please enter a command: ")

        string = cmd.split(" ", 4)
        command = string[0]

        # run is_command function
        check = is_command(command)

        if check is True:
            parse_command(cmd)
        else:
            print("Invalid command")

    print("------------------------------")
    print("Bye!")
    '''
if __name__ == "__main__":
    main()