import unittest
from taptap2.language_switcher import LanguageSwitcher

class TestLanguageSwitcher(unittest.TestCase):
    def setUp(self):
        self.switcher = LanguageSwitcher()

    def test_switch_language(self):
        initial_language = self.switcher.languages[self.switcher.current_language]
        new_language = self.switcher.switch_language()
        self.assertNotEqual(initial_language, new_language)
        self.assertEqual(new_language, self.switcher.languages[1])

    def test_cycle_through_languages(self):
        languages = self.switcher.languages
        for i in range(len(languages) * 2):
            self.assertEqual(self.switcher.switch_language(), languages[(i + 1) % len(languages)])

if __name__ == '__main__':
    unittest.main()