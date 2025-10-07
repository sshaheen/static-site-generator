import unittest

from src.helpers.splitnodesdelimiter import split_nodes_delimiter
from src.models.textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_string(self):
        node = TextNode(
            "My name **TEST BOLD TEXT** is Salem. Nice to **MORE BOLD TEXT** meet you!",
            TextType.TEXT,
        )
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("My name ", TextType.TEXT),
            TextNode("TEST BOLD TEXT", TextType.BOLD),
            TextNode(" is Salem. Nice to ", TextType.TEXT),
            TextNode("MORE BOLD TEXT", TextType.BOLD),
            TextNode(" meet you!", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)

    def test_no_list(self):
        with self.assertRaises(Exception) as exec:
            split_nodes_delimiter([], "_", TextType.ITALIC)
        self.assertEqual("Please pass in a valid list of nodes", str(exec.exception))

    def test_no_delimiter(self):
        node = TextNode(
            "My name **TEST BOLD TEXT** is Salem. Nice to **MORE BOLD TEXT** meet you!",
            TextType.TEXT,
        )
        with self.assertRaises(Exception) as exec:
            split_nodes_delimiter([node], "", TextType.ITALIC)
        self.assertEqual("Please enter a valid delimiter", str(exec.exception))

    def test_split_string(self):
        node1 = TextNode(
            "My name **TEST BOLD TEXT** is Salem.",
            TextType.TEXT,
        )
        node2 = TextNode("Nice to **MORE BOLD TEXT** meet you!", TextType.TEXT)
        actual = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        expected = [
            TextNode("My name ", TextType.TEXT),
            TextNode("TEST BOLD TEXT", TextType.BOLD),
            TextNode(" is Salem.", TextType.TEXT),
            TextNode("Nice to ", TextType.TEXT),
            TextNode("MORE BOLD TEXT", TextType.BOLD),
            TextNode(" meet you!", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)
