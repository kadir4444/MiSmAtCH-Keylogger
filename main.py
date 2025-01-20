# This is a sample Python script.
import datetime
import time

import keyboard
import pygame
from exceptiongroup import catch

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Time counter value
    addedTime = 30

    # Get Current time
    my_init_time = datetime.datetime.now()
    print("Time and Date right Now: " + str(my_init_time))

    # Adds added time to the current time to create new time
    time_change = datetime.timedelta(seconds=addedTime)
    new_time = my_init_time + time_change

    # Prints out the new time
    print("New time: " + new_time.time().isoformat(timespec="seconds"))

    '''
    # Time counter test
    i = datetime.datetime.now()
    j = 0

    while i.now() < new_time:
        j += 1
        print(j)
        print(i.now())
        time.sleep(1)
    '''

    print("KeyLogger Started............")

    # exit = False
    # Variable for setting exit key for keylogger
    exit_key = 'esc'

    # Array used to store keys clicked
    keyed_input = []

    # Initiates keyboard listener, it then records keys until exit criteria is met
    rec_mode = keyboard.record(until=exit_key)

    # An alternative way to exit keyboard listener via Event Method
    # keyboard.wait('esc')

    # pygame.init()



    # pygame.K_ESCAPE:
    print("Escape")


    # keyboard._keyboard_event.KEY_DOWN('esc')

    # Message to display that keyboard listener is finished
    print("KeyLogger Closed.")

    # Displays the keys clicked in long format
    print("Keys Entered: " + str(rec_mode))

    # Records the keyboard inputs into the keyed_input array
    for k in rec_mode:
        keyed_input.append(k.name)

    '''
    for keys in rec_mode:
        while not exit:
            keyed_input.append(keys.name)
    print(rec_mode)
    '''

    # Prints out the elements in the keyed_inputs arrays
    print(keyed_input)

    # Prints out the elements in the keyed_inputs arrays horizontally
    j = 0
    while j < len(keyed_input):
        print(keyed_input[j])
        j += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
