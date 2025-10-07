from .htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None or tag == "":
            raise ValueError("All parent nodes must have a tag")
        if children is None or len(children) == 0:
            raise ValueError("All parent nodes must have children")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        attrs = ""
        if getattr(self, "props", None):
            parts = [f'{k}="{v}"' for k, v in self.props.items()]
            attrs = " " + " ".join(parts)

        inner = "".join(child.to_html() for child in self.children or [])
        return f"<{self.tag}{attrs}>{inner}</{self.tag}>"
