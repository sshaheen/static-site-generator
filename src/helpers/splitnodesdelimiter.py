from src.models.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None or not isinstance(old_nodes, list) or len(old_nodes) == 0:
        raise Exception("Please pass in a valid list of nodes")
    if delimiter is None or delimiter == "":
        raise Exception("Please enter a valid delimiter")
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            if delimiter not in node.text:
                result.append(node)
            else:
                old_strs = node.text.split(delimiter)
                if len(old_strs) % 2 == 0:
                    raise Exception(f"Unmatched delimiter: {delimiter}")
                for i in range(len(old_strs)):
                    if i == 0 or i % 2 == 0:
                        result.append(TextNode(old_strs[i], TextType.TEXT))
                    else:
                        result.append(TextNode(old_strs[i], text_type))
    return result
