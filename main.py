# This is a sample Python script.
import datetime
import time

import keyboard
import pyautogui
import pygame
import win32com.client as comctl
from exceptiongroup import catch

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Time counter value
    addedTime = 5
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

    # An alternative way to exit keyboard listener via Event Method
    # keyboard.wait('esc')

    # pygame.init()

    # pygame.K_ESCAPE:
    #keyboard.write('A', delay=1A)
    # pyautogui.press('escape')
    # pyautogui.write('escape')
    # pyautogui.press("alt")
    # pyautogui.keyDown("escA")
    # wsh = comctl.Dispatch("WScript.Shell")
    #
    # wsh.AppActivate("icanhazip.com")
    # wsh.SendKeys("{escape}")

    print('New: ' + str(new_time))

    CONST_TIME_NOW = datetime.datetime.now()
    CONST_TIME_FUTURE = CONST_TIME_NOW + time_change

    '''
    print("New timeo: ")
    print(CONST_TIME_FUTURE.isoformat(timespec="seconds"))
    print("Now timeo: ")
    print(CONST_TIME_NOW.isoformat(timespec="seconds"))
    '''

    # while datetime.datetime.now().isoformat(timespec="seconds") != CONST_TIME_FUTURE.isoformat(timespec="seconds"):
    # Initiates keyboard listener, it then records keys until exit criteria is met
    # rec_mode = keyboard.record(until='esc')
    # keyboard.wait()

    rc = ''
    if rc != '':
        print("Ello")
    else:
        print("sa")
        rc = keyboard.read_key()

    rc = keyboard.read_key()
    keyed_input.append(rc)
    print(rc)

    # Prints out the elements in the keyed_inputs arrays horizontally
    j = 0
    while j < len(keyed_input):
        print(keyed_input[j])
        j += 1

    print("Array: " + str(keyed_input))


    keyboard.stop_recording()
    print("Array2: " + str(keyed_input))



    # d = keyboard.on_press_key('esc', 'esc', )

    # print("not yet")
    # print(datetime.datetime.now().isoformat(timespec="seconds"))
    # time.sleep(10)

    print("yay it's time")
    #keyboard.wait()

    '''
    while my_init_time == new_time:
        print("Not Yet")
        print('Now: ' + str(datetime.datetime.now()))
        time.sleep(10)
    '''

    print("Done")

    print("Escape")

    # keyboard._keyboard_event.KEY_DOWN('esc')

    # Message to display that keyboard listener is finished
    print("KeyLogger Closed.")

    # Displays the keys clicked in long format
    #print("Keys Entered: " + str(rec_mode))

    # Records the keyboard inputs into the keyed_input array
    # for k in rec_mode:
    #    keyed_input.append(k.name)

    # Prints out the elements in the keyed_inputs arrays
    print(keyed_input)

    # Prints out the elements in the keyed_inputs arrays horizontally
    j = 0
    while j < len(keyed_input):
        print(keyed_input[j])
        j += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
