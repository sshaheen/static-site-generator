import os
import sys

from .generatepage import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    os.makedirs(dest_dir_path, exist_ok=True)
    for name in os.listdir(dir_path_content):
        next_content = os.path.join(dir_path_content, name)
        next_dest = os.path.join(dest_dir_path, name)
        if os.path.isdir(next_content):
            generate_pages_recursive(next_content, template_path, next_dest)
        elif name.endswith(".md"):
            root, _ = os.path.splitext(next_dest)
            dest_html = root + ".html"
            os.makedirs(os.path.dirname(dest_html), exist_ok=True)
            generate_page(next_content, template_path, dest_html)
