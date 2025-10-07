import unittest

from src.helpers.splitnodeslink import split_nodes_link
from src.models.textnode import TextNode, TextType


class TestSplitNodesLink(unittest.TestCase):
    def test_one_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        expected = [
            TextNode(
                "This is text with a link ",
                TextType.TEXT,
            ),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        actual = split_nodes_link([node])

        self.assertEqual(expected, actual)

    def test_two_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        expected = [
            TextNode(
                "This is text with a link ",
                TextType.TEXT,
            ),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        actual = split_nodes_link([node])

        self.assertEqual(expected, actual)

    def test_three_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [hollow knight](https://www.hollowknight.com)",
            TextType.TEXT,
        )
        expected = [
            TextNode(
                "This is text with a link ",
                TextType.TEXT,
            ),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode(" and ", TextType.TEXT),
            TextNode("hollow knight", TextType.LINK, "https://www.hollowknight.com"),
        ]
        actual = split_nodes_link([node])

        self.assertEqual(expected, actual)
