from htmlnode import HTMLNode
from inline_markdown import split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import extract_markdown_images, extract_markdown_links
from inline_markdown import text_to_textnodes
from block_markdown import markdown_to_blocks

def main():
#     text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
#     print(text_node)

#     html_node = HTMLNode("a", "Boot.dev", [text_node], {
#     "href": "https://www.google.com",
#     "target": "_blank",
# })
#     print(html_node)

#     leadnode = LeafNode("p", "Hello, world!", {"class": "text-red-500"})
#     print(leadnode.to_html())

#     parent_node = ParentNode("div", [leadnode])
#     print(parent_node.to_html())

    #node = TextNode("This is text with a `code block` word", TextType.CODE)
    #new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    #node1 = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
    #new_nodes2 = split_nodes_delimiter([node1], "**", TextType.BOLD)

    #text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #print(extract_markdown_images(text))
    
    #text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #print(extract_markdown_links(text))

    # node = TextNode(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #     TextType.TEXT,
    # )
    # new_nodes = split_nodes_image([node])

    # text = """This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"""
    # nodes = text_to_textnodes(text)
    # print(nodes)

    md = """
                This is **bolded** paragraph

                This is another paragraph with _italic_ text and `code` here
                This is the same paragraph on a new line

                - This is a list
                - with items
                """
    markdown_to_blocks(md)


if __name__ == "__main__":
    main()