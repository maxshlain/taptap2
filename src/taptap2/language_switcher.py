class LanguageSwitcher:
    def __init__(self):
        self.languages = ["en", "ru"]  # Example languages
        self.current_language = 0

    def switch_language(self):
        self.current_language = (self.current_language + 1) % len(self.languages)
        return self.languages[self.current_language]