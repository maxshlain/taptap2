import unittest
from unittest.mock import Mock, patch
from pynput.keyboard import Key
from taptap2.keyboard_handler import KeyboardHandler


class TestKeyboardHandler(unittest.TestCase):
    def setUp(self):
        self.handler = KeyboardHandler()

    def test_caps_lock_pressed(self):
        self.handler.caps_lock_pressed()
        self.assertEqual(self.handler.caps_lock_count, 1)

    def test_should_switch_language(self):
        self.handler.caps_lock_pressed()
        self.handler.caps_lock_pressed()
        self.assertTrue(self.handler.should_switch_language())

    def test_key_pressed(self):
        mock_key = Mock()
        mock_key.char = 'a'
        self.handler.key_pressed(mock_key)
        self.assertEqual(self.handler.buffer, ['a'])

    @patch('taptap2.keyboard_handler.keyboard.Controller')
    def test_switch_language(self, mock_controller):
        self.handler.buffer = ['a', 'b', 'c']
        self.handler.switch_language('ru')
        self.assertEqual(mock_controller().press.call_count, 3)
        self.assertEqual(mock_controller().release.call_count, 3)
        self.assertEqual(mock_controller().type.call_count, 3)
        self.assertEqual(self.handler.buffer, [])
        self.assertEqual(self.handler.caps_lock_count, 0)

if __name__ == '__main__':
    unittest.main()