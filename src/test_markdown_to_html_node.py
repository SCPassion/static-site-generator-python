import unittest
from block_markdown import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading_blocks(self):
        """Test heading blocks with different levels"""
        # Test h1
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        
        # Test h2
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        
        # Test h3
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        
        # Test h4
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        
        # Test h5
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        
        # Test h6
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        
        # Test heading with text after space
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)
        
        # Test heading with multiple spaces after #
        self.assertEqual(block_to_block_type("##   Multiple spaces"), BlockType.HEADING)
    
    def test_code_blocks(self):
        """Test code blocks"""
        # Test simple code block
        code_block = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)
        
        # Test code block with language
        code_block_lang = "```python\ndef hello():\n    print('hello')\n```"
        self.assertEqual(block_to_block_type(code_block_lang), BlockType.CODE)
        
        # Test multi-line code block
        multi_line_code = "```\nline 1\nline 2\nline 3\n```"
        self.assertEqual(block_to_block_type(multi_line_code), BlockType.CODE)
        
        # Test code block with empty lines
        empty_line_code = "```\n\ncode here\n\n```"
        self.assertEqual(block_to_block_type(empty_line_code), BlockType.CODE)
    
    def test_quote_blocks(self):
        """Test quote blocks"""
        # Test single line quote
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        
        # Test multi-line quote
        multi_quote = "> Line 1\n> Line 2\n> Line 3"
        self.assertEqual(block_to_block_type(multi_quote), BlockType.QUOTE)
        
        # Test quote with space after >
        self.assertEqual(block_to_block_type(">   Multiple spaces"), BlockType.QUOTE)
        
        # Test quote with empty lines (should still be quote if all lines start with >)
        empty_quote = "> Line 1\n>\n> Line 3"
        self.assertEqual(block_to_block_type(empty_quote), BlockType.QUOTE)
    
    def test_unordered_list_blocks(self):
        """Test unordered list blocks"""
        # Test single item list
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.UNORDERED_LIST)
        
        # Test multi-item list
        multi_list = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(multi_list), BlockType.UNORDERED_LIST)
        
        # Test list with space after -
        self.assertEqual(block_to_block_type("-   Multiple spaces"), BlockType.UNORDERED_LIST)
        
        # Test list with empty lines (should still be list if all lines start with -)
        empty_list = "- Item 1\n-\n- Item 3"
        self.assertEqual(block_to_block_type(empty_list), BlockType.UNORDERED_LIST)
    
    def test_ordered_list_blocks(self):
        """Test ordered list blocks"""
        # Test single item list
        self.assertEqual(block_to_block_type("1. Item 1"), BlockType.ORDERED_LIST)
        
        # Test multi-item list starting at 1
        multi_list = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(multi_list), BlockType.ORDERED_LIST)
        
        # Test list with space after number.
        self.assertEqual(block_to_block_type("1.   Multiple spaces"), BlockType.ORDERED_LIST)
        
        # Test list with double digits
        double_digit_list = "1. Item 1\n2. Item 2\n10. Item 10\n11. Item 11"
        self.assertEqual(block_to_block_type(double_digit_list), BlockType.PARAGRAPH)
    
    def test_paragraph_blocks(self):
        """Test paragraph blocks (default case)"""
        # Test simple text
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        
        # Test multi-line text
        multi_text = "Line 1\nLine 2\nLine 3"
        self.assertEqual(block_to_block_type(multi_text), BlockType.PARAGRAPH)
        
        # Test text that looks like heading but no space
        self.assertEqual(block_to_block_type("#No space"), BlockType.PARAGRAPH)
        
        # Test text that looks like list but no space
        self.assertEqual(block_to_block_type("-No space"), BlockType.PARAGRAPH)
        
        # Test text that looks like quote but no space
        self.assertEqual(block_to_block_type(">No space"), BlockType.PARAGRAPH)
        
        # Test text that looks like ordered list but no space
        self.assertEqual(block_to_block_type("1.No space"), BlockType.PARAGRAPH)
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Test empty string
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
        
        # Test single character
        self.assertEqual(block_to_block_type("a"), BlockType.PARAGRAPH)
        
        # Test single #
        self.assertEqual(block_to_block_type("#"), BlockType.PARAGRAPH)
        
        # Test single -
        self.assertEqual(block_to_block_type("-"), BlockType.PARAGRAPH)
        
        # Test single >
        self.assertEqual(block_to_block_type(">"), BlockType.PARAGRAPH)
        
        # Test single 1.
        self.assertEqual(block_to_block_type("1."), BlockType.PARAGRAPH)
        
        # Test heading with no text after space
        self.assertEqual(block_to_block_type("# "), BlockType.HEADING)
        
        # Test code block with only ```
        self.assertEqual(block_to_block_type("```\n```"), BlockType.CODE)
    
    def test_invalid_ordered_lists(self):
        """Test ordered lists that don't start at 1 or don't increment properly"""
        # Test list starting at 2
        self.assertEqual(block_to_block_type("2. Item 1\n3. Item 2"), BlockType.PARAGRAPH)
        
        # Test list with gaps
        self.assertEqual(block_to_block_type("1. Item 1\n3. Item 2"), BlockType.PARAGRAPH)
        
        # Test list with non-sequential numbers
        self.assertEqual(block_to_block_type("1. Item 1\n5. Item 2"), BlockType.PARAGRAPH)
        
        # Test list with repeated numbers
        self.assertEqual(block_to_block_type("1. Item 1\n1. Item 2"), BlockType.PARAGRAPH)
        
        # Test list with zero
        self.assertEqual(block_to_block_type("0. Item 1\n1. Item 2"), BlockType.PARAGRAPH)
    
    def test_mixed_content(self):
        """Test blocks that don't fit clean patterns"""
        # Test mixed list types
        mixed_list = "- Item 1\n1. Item 2"
        self.assertEqual(block_to_block_type(mixed_list), BlockType.PARAGRAPH)
        
        # Test mixed quote and list
        mixed_quote = "> Quote line\n- List line"
        self.assertEqual(block_to_block_type(mixed_quote), BlockType.PARAGRAPH)
        
        # Test text with some list-like elements
        mixed_text = "Some text\n- But not all lines\nMore text"
        self.assertEqual(block_to_block_type(mixed_text), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()