import unittest
from src.models.enum_blocktype import BlockType
from src.helpers.blocktoblocktype import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# Heading One"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.HEADING)

    def test_code(self):
        block = "```This is code```"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.CODE)

    def test_quote(self):
        block = "> Henlo I am a quote\n> Another quote\n> A third quote"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- This is a list\n- with items"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. Hi I am an ordered list\n2. This is the second item in the list.\n3. Third item"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is just a paragraph.\n I am adding some text here to test it.\n"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.PARAGRAPH)
