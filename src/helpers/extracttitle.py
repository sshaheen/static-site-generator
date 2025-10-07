def extract_title(markdown):
    if not markdown.startswith("#"):
        raise Exception("Markdown should start with # Title")
    first_line = markdown.split("\n", 1)[0]
    title = first_line.strip("# ")
    return title
