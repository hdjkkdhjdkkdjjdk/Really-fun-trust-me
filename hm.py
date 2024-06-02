import tkinter as tk
from tkinter import messagebox
import pygame


# Function to create the initial tkinter dialog
def show_initial_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    response = messagebox.askyesno("Warning", "Installing malware now... Do you want to proceed?(click no(PLEASE(if no minimize the code editor)))")
    root.destroy()  # Destroy the tkinter root window
    return response


# Function to show the final dialog after the game
def show_final_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    response = messagebox.askyesno("Final Question", "What about now? Do you want to download?")
    root.destroy()  # Destroy the tkinter root window
    return response


# Function to show the "you are an idiot" window
def show_idiot_window():
    root = tk.Tk()
    root.title("Warning")
    root.geometry("400x200")
    label = tk.Label(root, text="YOU ARE AN IDIOT", font=("Arial", 36), fg="white", bg="red")
    label.pack(padx=20, pady=20)
    root.mainloop()


# Function to run the simple pygame game
def run_pygame_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Click the blocks to color them")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Game variables
    block_size = 40
    grid = [[WHITE for _ in range(16)] for _ in range(12)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // block_size
                col = x // block_size
                if grid[row][col] == WHITE:
                    grid[row][col] = RED
                else:
                    grid[row][col] = WHITE

        screen.fill(BLACK)

        for row in range(12):
            for col in range(16):
                color = grid[row][col]
                pygame.draw.rect(screen, color, (col * block_size, row * block_size, block_size, block_size))

        pygame.display.flip()

    pygame.quit()


# Main function
def main():
    response = show_initial_dialog()
    if not response:
        run_pygame_game()
        final_response = show_final_dialog()
        if not final_response:
            show_idiot_window()  # Show the "you are an idiot" window
            print("Well DOWNLOADING")
    else:
        # Perform the loop and print the message (for demonstration purposes, the loop is very small)
        # Note: Using the full range will make the script impractical to run.
        try:
            for i in range(1):  # Reduced range for demonstration
                print('M')
        except OverflowError:
            print("Loop size is too large to handle!")

        messagebox.showinfo("Just kidding", "Just kidding!")


if __name__ == "__main__":
    main()
