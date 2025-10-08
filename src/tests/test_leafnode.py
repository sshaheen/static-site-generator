import unittest

from src.models.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("h1", "Level 1 Heading")
        self.assertEqual(node.to_html(), "<h1>Level 1 Heading</h1>")

    def test_leaf_to_html(self):
        node = LeafNode("br", "")
        self.assertEqual(node.to_html(), "<br>")
