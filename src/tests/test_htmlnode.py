import unittest

from src.models.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.tag, "div")

    def test_value(self):
        node = HTMLNode(value="Henlo Fren")
        self.assertEqual(node.value, "Henlo Fren")

    def test_children(self):
        node = HTMLNode(children=["h3", "p"])
        self.assertEqual(node.children, ["h3", "p"])

    def test_props_to_html(self):
        node = HTMLNode(
            "h1",
            "My Silly TestCase",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        return_str = node.props_to_html()
        self.assertEqual(' href="https://www.google.com" target="_blank"', return_str)

    def test_print(self):
        node = HTMLNode(
            "div",
            "I love Hollow Knight!",
            ["h1", "p"],
            {"id": "blue-text", "class": "bg-red"},
        )
        self.assertEqual(
            repr(node),
            "Tag: div, Value: I love Hollow Knight!, Children: ['h1', 'p'], Props:  id=\"blue-text\" class=\"bg-red\"",
        )
