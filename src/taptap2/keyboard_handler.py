import time
from pynput import keyboard

class KeyboardHandler:
    def __init__(self):
        self.last_caps_lock_press = 0
        self.caps_lock_count = 0
        self.buffer = []
        self.controller = keyboard.Controller()

    def caps_lock_pressed(self):
        current_time = time.time()
        if current_time - self.last_caps_lock_press < 0.5:
            self.caps_lock_count += 1
        else:
            self.caps_lock_count = 1
        self.last_caps_lock_press = current_time

    def should_switch_language(self):
        return self.caps_lock_count == 2

    def key_pressed(self, key):
        if key == keyboard.Key.space:
            self.buffer = []
        elif hasattr(key, 'char'):
            self.buffer.append(key.char)

    def switch_language(self, new_language):
        # Simulate backspace for each character in the buffer
        for _ in self.buffer:
            self.controller.press(keyboard.Key.backspace)
            self.controller.release(keyboard.Key.backspace)

        # Simulate typing the buffer in the new language
        for char in self.buffer:
            # Here you would implement the logic to convert the character to the new language
            # For simplicity, we'll just type the original character
            self.controller.type(char)

        self.buffer = []
        self.caps_lock_count = 0
        print(f"Switched to {new_language}")