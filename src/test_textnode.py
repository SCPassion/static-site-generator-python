import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text2 node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node.url, node2.url)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node.url, None)

    

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_texttype_is_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text_type, TextType.BOLD)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def text_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()