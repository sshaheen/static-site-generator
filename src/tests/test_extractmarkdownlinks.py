import unittest

from src.helpers.extractmarkdownlinks import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Start learning on Bootdev [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_many_links(self):
        matches = extract_markdown_links(
            "Start learning on Bootdev [to boot dev](https://www.boot.dev). Checkout their YouTube [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )
