import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode("a", "Boot.dev", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(html_node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_eq(self):
        html_node = HTMLNode("a", "Boot.dev", None, {"href": "https://www.google.com", "target": "_blank"})
        html_node2 = HTMLNode("a", "Boot.dev", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(html_node, html_node2)

    def test_not_eq(self):
        html_node = HTMLNode("a", "Boot.dev", None, {"href": "https://www.google.com", "target": "_blank"})
        html_node2 = HTMLNode("a", "Boot1.dev", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(html_node, html_node2)