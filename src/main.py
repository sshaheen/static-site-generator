import os
import shutil
import sys
from .copystatic import copy_static
from .helpers.generatepagesrecrusive import generate_pages_recursive

public = "public"
static = "static"
content = "content"
template = "template.html"
docs_dir = "docs"


def main():
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    copy_static(static, docs_dir)
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    generate_pages_recursive(content, template, docs_dir, base_path)


main()
