def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped = list(map(str.strip, blocks))
    final = list(filter(lambda x: x != "", stripped))
    return final
