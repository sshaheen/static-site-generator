class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Base class doesn't implement to_html method")

    def props_to_html(self):
        prop_str = ""
        for prop_type, prop_val in self.props.items():
            prop_str += f' {prop_type}="{prop_val}"'
        return prop_str

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props_to_html()}"
