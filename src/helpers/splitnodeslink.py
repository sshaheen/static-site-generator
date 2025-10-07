from src.models.textnode import TextNode, TextType
from .extractmarkdownlinks import extract_markdown_links


def split_nodes_link(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            results.extend(get_link_nodes_helper(node.text))
        else:
            results.append(node)
    return results


def get_link_nodes_helper(text):
    if text == "":
        return []
    matches = extract_markdown_links(text)
    if not matches:
        return [TextNode(text, TextType.TEXT)]
    link_text, link_url = matches[0]
    full = f"[{link_text}]({link_url})"
    before, after = text.split(full, 1)
    nodes = []
    if before:
        nodes.append(TextNode(before, TextType.TEXT))
    nodes.append(TextNode(link_text, TextType.LINK, link_url))
    nodes.extend(get_link_nodes_helper(after))
    return nodes
