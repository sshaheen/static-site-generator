import unittest
from src.helpers.extracttitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        md = "# This is the title!"
        title = extract_title(md)
        self.assertEqual(title, "This is the title!")

    def test_no_title(self):
        md = "No title here boi."
        with self.assertRaises(Exception) as exec:
            extract_title(md)
        self.assertEqual(str(exec.exception), "Markdown should start with # Title")

    def test_title_linebr(self):
        md = "# This is the title!\nThis is some content"
        title = extract_title(md)
        self.assertEqual(title, "This is the title!")

    def test_title_trailing_space(self):
        md = "# This is the title!    "
        title = extract_title(md)
        self.assertEqual(title, "This is the title!")
