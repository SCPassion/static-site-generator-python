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
    lines = block.splitlines()

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
     # Code blocks: Check if first and last lines are only ```
    if len(lines) >= 2 and lines[0].strip() == "```" and lines[-1].strip() == "```":
        return BlockType.CODE
    
    # Quotes: Check if every line starts with >
    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE
    
    # Unordered lists: Check if every line starts with -
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Ordered lists: Check if every line starts with number. and numbers increment from 1
    if all(re.match(r'^\d+\.\s', line) for line in lines):
        # Extract numbers and check if they start at 1 and increment by 1
        numbers = []
        for line in lines:
            match = re.match(r'^(\d+)\.', line)
            if match:
                numbers.append(int(match.group(1)))
        
        if numbers == list(range(1, len(numbers) + 1)):
            return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH