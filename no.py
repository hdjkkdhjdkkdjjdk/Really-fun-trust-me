import time
import threading
from pynput import keyboard

# Flag to control the listener
stop_listener = False

def on_press(key):
    if stop_listener:
        return False  # Stop the listener if the flag is set
    return False  # This prevents the key press from being processed

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Function to simulate input capture and prevent it from processing
def fake_input(prompt):
    print(prompt, end="", flush=True)
    while True:
        time.sleep(1)  # Keep the loop running to simulate waiting for input
    return ""  # Return an empty string to simulate no input

def main():
    # Start the listener in a separate thread
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()

    # Use the fake_input function to simulate input
    user_input = fake_input("Enter something: ")
    print(f"You entered: {user_input}")

    # Stop the listener
    global stop_listener
    stop_listener = True

    listener_thread.join()

if __name__ == "__main__":
    main()
