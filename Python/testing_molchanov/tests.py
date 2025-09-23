import unittest
from unittest.mock import MagicMock, patch

from main import add, len_joke

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

    @patch("main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)

    @patch("main.requests")
    def test_get_joke2(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": "Goog joke"}
        mock_requests.get.return_value = mock_response
        self.assertEqual(len_joke(), len("Goog joke"))

if __name__ == "__main__":
    unittest.main()