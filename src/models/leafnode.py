from .htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return f"{self.value}"

        attrs = ""
        if getattr(self, "props", None):
            parts = [f'{k}="{v}"' for k, v in self.props.items()]
            attrs = " " + " ".join(parts)

        # Void elements
        if self.tag in {"img", "br", "hr", "meta", "link", "input"}:
            return f"<{self.tag}{attrs}>"

        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
