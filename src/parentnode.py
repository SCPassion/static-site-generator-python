from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is required")

        if not self.children:
            raise ValueError("children is required")

        html_children = ""
        for child in self.children:
            html_children += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>"


    def __eq__(self, other):
        return super().__eq__(other) and self.children == other.children

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
