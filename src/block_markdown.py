from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    new_blocks = markdown.split("\n\n")
    new_blocks = map(lambda block: block.strip(), new_blocks)
    new_blocks = map(lambda block: '\n'.join([line.strip() for line in block.splitlines()]), new_blocks)
    new_blocks = list(filter(lambda block: block != "", new_blocks))
    return new_blocks

def block_to_block_type(block):
    # Handle empty blocks
    if not block.strip():
        return BlockType.PARAGRAPH
    
    lines = block.splitlines()

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    # Code blocks: Check if first and last lines start with ```
    if len(lines) >= 2 and lines[0].strip().startswith("```") and lines[-1].strip().startswith("```"):
        return BlockType.CODE
    
    # Quotes: Check if every line starts with > (with or without space)
    # But only if it's a multi-line block or has content
    if len(lines) > 1 and all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif len(lines) == 1 and block.startswith("> "):
        return BlockType.QUOTE
    
    # Unordered lists: Check if every line starts with - followed by a space or is just -
    # But only if it's a multi-line block or has content
    if len(lines) > 1 and all(line.startswith("-") and (len(line) == 1 or line[1] == " ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif len(lines) == 1 and block.startswith("- "):
        return BlockType.UNORDERED_LIST
    
    # Ordered lists: Check if every line starts with number. and numbers increment from 1
    if all(re.match(r'^\d+\.\s', line) for line in lines):
        # Extract numbers and check if they start at 1 and increment
        numbers = []
        for line in lines:
            match = re.match(r'^(\d+)\.', line)
            if match:
                numbers.append(int(match.group(1)))
        
        # Check if numbers start at 1 and are consecutive
        if numbers and numbers == list(range(1, len(numbers) + 1)):
            return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH