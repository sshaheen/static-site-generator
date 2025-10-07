from ..models.textnode import TextNode, TextType
from .extractmarkdownimages import extract_markdown_images


def split_nodes_image(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            results.extend(get_image_nodes_helper(node.text))
        else:
            results.append(node)
    return results


def get_image_nodes_helper(text):
    if text == "":
        return []
    matches = extract_markdown_images(text)
    if not matches:
        return [TextNode(text, TextType.TEXT)]
    alt_text, image_url = matches[0]
    full = f"![{alt_text}]({image_url})"
    before, after = text.split(full, 1)
    nodes = []
    if before:
        nodes.append(TextNode(before, TextType.TEXT))
    nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
    nodes.extend(get_image_nodes_helper(after))
    return nodes
