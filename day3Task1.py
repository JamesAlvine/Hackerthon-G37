import datetime


def door_lock_system():
    passw = "open"
    condition = "execute"
    date_time = []
    state = 'close'
    status = 'close'
    # functions

    def open_lock():
        nonlocal state
        if (status_cheking_cmd() == 'open' and state == 'close'):
            print('The door is now open')
            state = 'open'
            date_and_time = datetime.datetime.now()
            date_time.append(date_and_time)
            if len(date_time) == 1:
                print(f"Door Last open at {date_time[0]}")
            else:
                print(f"Door Last open at {date_time[len(date_time)-2]}")
        else:
            print('the door is already open')

    def close_lock():
        if (status_cheking_cmd() == 'open'):
            print('The door is now locked')
            if len(date_time) == 1:
                print(f"Door Last open at {date_time[0]}")
            else:
                print(f"Door Last open at {date_time[len(date_time)-2]}")
        else:
            print('the door is already locked')

    def check_lock_status():
        nonlocal status
        if (status == 'open'):
            return(status)
        if (inp == passw):
            status = 'open'
        else:
            status = 'close'
        return(status)

    def invalid_inpt():
        if (inp != 'open' and inp != 'close' and inp != 'quit'):
            print('invalid input please enter your password again!')

    def quit_app():
        if (inp == 'quit'):
            # assigning functions to variables
            print('the process is being terminated!')
    opening_cmd = open_lock
    closing_cmd = close_lock
    status_cheking_cmd = check_lock_status
    quiting_cmd = quit_app
    invalid_key_cmd = invalid_inpt
    while (condition == 'execute'):
        inp = input(
            'Please enter your input in small letters only to open or close the lock!')
        if (inp == passw):
            opening_cmd()
        elif (inp == 'close'):
            closing_cmd()
        elif (inp == 'quit'):
            quiting_cmd()
            condition = 'stop'
        else:
            invalid_key_cmd()


door_lock_system()
