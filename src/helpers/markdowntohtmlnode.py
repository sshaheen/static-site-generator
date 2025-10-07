from .textnodetohtmlnode import text_node_to_html_node
from .texttotextnodes import text_to_text_nodes
from .markdowntoblocks import markdown_to_blocks
from .blocktoblocktype import block_to_block_type
from src.models.parentnode import ParentNode
from src.models.enum_blocktype import BlockType
from src.models.textnode import TextNode, TextType


def markdown_to_html_node(markdown):
    inner_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.PARAGRAPH:
                block = block.replace("\n", " ")
                children = text_to_children(block)
                node = ParentNode("p", children)
                inner_nodes.append(node)
            case BlockType.HEADING:
                block = block.replace("\n", " ")
                stripped_hash = block.lstrip("#")
                num_hashes = len(block) - len(stripped_hash)
                heading = f"h{num_hashes}"
                cleaned_input = stripped_hash.lstrip(" ")
                children = text_to_children(cleaned_input)
                node = ParentNode(heading, children)
                inner_nodes.append(node)
            case BlockType.UNORDERED_LIST:
                li_nodes = []
                list_items = block.split("\n")
                for item in list_items:
                    content = item.lstrip("-")
                    content = content.lstrip(" ")
                    children = text_to_children(content)
                    li_node = ParentNode("li", children)
                    li_nodes.append(li_node)
                node = ParentNode("ul", li_nodes)
                inner_nodes.append(node)
            case BlockType.ORDERED_LIST:
                li_nodes = []
                list_items = block.split("\n")
                for item in list_items:
                    _, content = item.split(".", 1)
                    content = content.lstrip(" ")
                    children = text_to_children(content)
                    li_node = ParentNode("li", children)
                    li_nodes.append(li_node)
                node = ParentNode("ol", li_nodes)
                inner_nodes.append(node)
            case BlockType.QUOTE:
                quote_lines = []
                quote_content = block.split("\n")
                for quote in quote_content:
                    quote = quote.lstrip(">")
                    quote = quote.lstrip(" ")
                    quote_lines.append(quote)
                processed_quote = " ".join(quote_lines)
                children = text_to_children(processed_quote)
                node = ParentNode("blockquote", children)
                inner_nodes.append(node)
            case BlockType.CODE:
                code_text = block.strip("```")
                code_text = code_text.lstrip("\n")
                text_node = TextNode(code_text, TextType.CODE)
                html_node = text_node_to_html_node(text_node)
                node = ParentNode("pre", [html_node])
                inner_nodes.append(node)
    outer_div = ParentNode("div", inner_nodes)
    return outer_div


def text_to_children(text):
    children = []
    text_nodes = text_to_text_nodes(text)
    for text_node in text_nodes:
        child = text_node_to_html_node(text_node)
        children.append(child)
    return children
