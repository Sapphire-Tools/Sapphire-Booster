import unittest

from pystyle import Colorate, Colors
from unittest.mock import patch

from src.helpers.colors import ColorHelper

print("\nRunning tests for colors.py:")

class TestColorHelper(unittest.TestCase):
    def test_default_color(self):
        text = "Hello, World!"
        expected = Colorate.Horizontal(Colors.cyan_to_green, text, 1)
        result = ColorHelper.color(text)
        self.assertEqual(result, expected)

    def test_custom_color(self):
        text = "Hello, World!"
        color = Colors.red_to_yellow
        expected = Colorate.Horizontal(color, text, 1)
        result = ColorHelper.color(text, color)
        self.assertEqual(result, expected)

    @patch('pystyle.Colorate.Horizontal', return_value="mocked color")
    def test_color_function_call(self, mock_colorate):
        text = "Hello, World!"
        color = Colors.blue_to_purple
        result = ColorHelper.color(text, color)
        mock_colorate.assert_called_once_with(color, text, 1)
        self.assertEqual(result, "mocked color")

if __name__ == "__main__":
    unittest.main()
