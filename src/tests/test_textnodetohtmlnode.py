import unittest

from src.models.textnode import TextNode, TextType
from src.models.leafnode import LeafNode
from src.helpers.textnodetohtmlnode import text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode(
            "You should play Hollow Knight!",
            TextType.LINK,
            "https://www.hollowknight.com/",
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "You should play Hollow Knight!")
        self.assertEqual(html_node.props, {"href": "https://www.hollowknight.com/"})

    def test_bold(self):
        node = TextNode("I'm bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "I'm bold")

    def test_italic(self):
        node = TextNode("I'm italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "I'm italic")

    def test_code(self):
        node = TextNode("# I'm code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "# I'm code")

    def test_image(self):
        node = TextNode(
            "It's me, Hollow Knight",
            TextType.IMAGE,
            "https://images.squarespace-cdn.com/content/v1/606d159a953867291018f801/1619987722169-VV6ZASHHZNRBJW9X0PLK/Key_Art_02_layeredjpg.jpg?format=1500w",
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {
                "src": "https://images.squarespace-cdn.com/content/v1/606d159a953867291018f801/1619987722169-VV6ZASHHZNRBJW9X0PLK/Key_Art_02_layeredjpg.jpg?format=1500w",
                "alt": "It's me, Hollow Knight",
            },
        )
