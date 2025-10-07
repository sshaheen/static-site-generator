from ..models.textnode import TextNode, TextType
from .splitnodesdelimiter import split_nodes_delimiter
from .splitnodeslink import split_nodes_link
from .splitnodesimage import split_nodes_image


def text_to_text_nodes(text):
    start = TextNode(text, TextType.TEXT)
    step_one = split_nodes_delimiter([start], "**", TextType.BOLD)
    step_two = split_nodes_delimiter(step_one, "_", TextType.ITALIC)
    step_three = split_nodes_delimiter(step_two, "`", TextType.CODE)
    step_four = split_nodes_image(step_three)
    final = split_nodes_link(step_four)
    return final
