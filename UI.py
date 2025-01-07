import tkinter as tk
import sys  # To exit the program

# Global variables to manage the window and widgets
root = None
label = None
toggle_button = None
is_transparent = True
is_done = False

def toggle_window_state():
    """Toggle between transparent/immovable and opaque/movable window states."""
    global is_transparent
    if is_transparent:
        # Make the window opaque and movable
        root.attributes("-alpha", 1)  # Fully opaque (1.0)
        root.overrideredirect(False)  # Allow moving and resizing
    else:
        # Make the window transparent and immovable
        root.attributes("-alpha", 0.7)  # Partially transparent
        root.overrideredirect(True)  # Remove title bar and disable moving
    is_transparent = not is_transparent  # Toggle the state

def update_text(new_text):
    """Update the text displayed in the window."""
    if label:
        label.config(text=new_text)
        # Make the label fully transparent if the text is empty
        if new_text == "":
            label.config(bg="gray")  # Set background to match transparent color
            label.config(fg="gray")  # Make text color match the transparent background
        else:
            label.config(bg="white")  # Set background to opaque when there's text
            label.config(fg="black")  # Make the text black when it's visible

def on_window_close():
    """Handler for the window close event to exit the program."""
    root.quit()  # Stop the main loop
    root.destroy()  # Close the window
    sys.exit()  # Exit the program

def create_window():
    """Create and display the transparent toggle window."""
    global root, label, toggle_button, is_transparent, is_done

    # Initialize the main window
    root = tk.Tk()
    root.title("Transparent Toggle Window")
    root.geometry("300x200")
    root.wm_attributes("-transparentcolor", "gray")  # Set transparent color
    root.config(bg="gray")  # Match transparent color
    root.attributes("-topmost", True)  # Disable always-on-top

    # Bind the window close event to our custom function
    root.protocol("WM_DELETE_WINDOW", on_window_close)

    # Add a label
    label = tk.Label(root, text="Initializing...", font=("Arial", 14), bg="white", fg="black")
    label.pack(pady=20)

    # Add a toggle button
    toggle_button = tk.Button(root, text="📌", command=toggle_window_state, bg="white", fg="black")
    toggle_button.pack(pady=10)
    is_done = True
    # Start the application
    root.mainloop()