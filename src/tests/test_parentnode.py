import unittest

from src.models.parentnode import ParentNode
from src.models.leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_nochildren(self):
        with self.assertRaises(ValueError) as exec:
            ParentNode("div", [])
        self.assertEqual("All parent nodes must have children", str(exec.exception))

    def test_nonechildren(self):
        with self.assertRaises(ValueError) as exec:
            ParentNode("div", None)
        self.assertEqual("All parent nodes must have children", str(exec.exception))

    def test_nonetag(self):
        with self.assertRaises(ValueError) as exec:
            ParentNode(None, [])
        self.assertEqual("All parent nodes must have a tag", str(exec.exception))

    def test_emptytag(self):
        with self.assertRaises(ValueError) as exec:
            ParentNode("", [])
        self.assertEqual("All parent nodes must have a tag", str(exec.exception))
