import os
import shutil
from src.copysrcdest import copy_src_dest
from src.helpers.generatepagesrecrusive import generate_pages_recursive

public = "public"
static = "static"
content = "content"
template = "template.html"


def main():
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_src_dest(static, public)
    generate_pages_recursive(content, template, public)


main()
