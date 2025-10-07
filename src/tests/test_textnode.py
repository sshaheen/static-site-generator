import unittest

from src.models.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("My name is mud", TextType.BOLD)
        node2 = TextNode("Vredesbyrd", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_type_prop(self):
        node = TextNode("Let's Play Hollow Knight!", TextType.ITALIC)
        self.assertEqual(node.text_type, TextType.ITALIC)

    def test_no_url(self):
        node = TextNode("Sample Value", TextType.CODE)
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
