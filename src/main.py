from htmlnode import HTMLNode
from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)

    html_node = HTMLNode("a", "Boot.dev", [text_node], {
    "href": "https://www.google.com",
    "target": "_blank",
})
    print(html_node)

    node = LeafNode("p", "Hello, world!", {"class": "text-red-500"})
    print(node.to_html())

if __name__ == "__main__":
    main()