from src.models.enum_blocktype import BlockType


def block_to_block_type(md_block):
    if md_block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    elif md_block.startswith("```") and md_block.endswith("```"):
        return BlockType.CODE
    elif check_special_block(md_block, ">"):
        return BlockType.QUOTE
    elif check_special_block(md_block, "-"):
        return BlockType.UNORDERED_LIST
    elif check_special_block(md_block, 1):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def check_special_block(md_block, delim):
    lines = md_block.split("\n")
    if isinstance(delim, int):
        count = 1
        for line in lines:
            if line.startswith(f"{count}.") is False:
                return False
            count += 1
    else:
        for line in lines:
            if line.startswith(delim) is False:
                return False
    return True
