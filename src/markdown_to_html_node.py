from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from textnode import TextType, TextNode, text_node_to_html_node
import re

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  html_nodes = []

  for block in blocks:
    block_type = block_to_block_type(block)
    html_node = None
    
    if block_type == BlockType.HEADING:
      # Count # symbols to determine heading level
      heading_level = 0
      temp_block = block
      while temp_block.startswith("#"):
        heading_level += 1
        temp_block = temp_block[1:]
      
      content = temp_block.lstrip()
      children = text_to_children(content)
      html_node = HTMLNode(f"h{heading_level}", None, children)
      
    elif block_type == BlockType.PARAGRAPH:
      children = text_to_children(block)
      html_node = HTMLNode("p", None, children)
      
    elif block_type == BlockType.CODE:
      lines = block.splitlines()
      code_content = "\n".join(lines[1:-1])
      code_node = HTMLNode("code", None, text_to_children(code_content))
      html_node = HTMLNode("pre", None, [code_node])
      
    elif block_type == BlockType.QUOTE:
      lines = block.splitlines()
      quote_content = "\n".join([line[2:] for line in lines])  # Remove "> " prefix
      children = text_to_children(quote_content)
      html_node = HTMLNode("blockquote", None, children)
      
    elif block_type == BlockType.UNORDERED_LIST:
      lines = block.splitlines()
      list_items = []
      for line in lines:
        item_content = line[2:]  # Remove "- " prefix
        children = text_to_children(item_content)
        list_items.append(HTMLNode("li", None, children))
      html_node = HTMLNode("ul", None, list_items)
      
    elif block_type == BlockType.ORDERED_LIST:
      lines = block.splitlines()
      list_items = []
      for line in lines:
        # Remove "1.", "2.", etc. prefix using regex
        item_content = re.sub(r'^\d+\.\s', '', line)
        children = text_to_children(item_content)
        list_items.append(HTMLNode("li", None, children))
      html_node = HTMLNode("ol", None, list_items)

    if html_node is not None:
      html_nodes.append(html_node)

  parent_div = HTMLNode("div", None, html_nodes)
  return parent_div


def text_to_children(text) -> list[HTMLNode]:
  children = []
  text_nodes = text_to_textnodes(text)
  for text_node in text_nodes:
    if text_node.text_type == TextType.TEXT:
      children.append(text_node_to_html_node(text_node))
    elif text_node.text_type == TextType.BOLD:
      children.append(text_node_to_html_node(text_node))
    elif text_node.text_type == TextType.ITALIC:
      children.append(text_node_to_html_node(text_node))
    elif text_node.text_type == TextType.CODE:
      children.append(text_node_to_html_node(text_node))
    elif text_node.text_type == TextType.LINK:
      children.append(text_node_to_html_node(text_node))
    elif text_node.text_type == TextType.IMAGE:
      children.append(text_node_to_html_node(text_node))

  return children

