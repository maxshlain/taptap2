from pynput import keyboard
from keyboard_handler import KeyboardHandler
from language_switcher import LanguageSwitcher

def main():
    keyboard_handler = KeyboardHandler()
    language_switcher = LanguageSwitcher()
    
    def on_press(key):
        if key == keyboard.Key.caps_lock:
            keyboard_handler.caps_lock_pressed()
        else:
            keyboard_handler.key_pressed(key)

    def on_release(key):
        if key == keyboard.Key.caps_lock:
            if keyboard_handler.should_switch_language():
                new_language = language_switcher.switch_language()
                keyboard_handler.switch_language(new_language)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()