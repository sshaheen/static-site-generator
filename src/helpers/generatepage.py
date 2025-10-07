import os
import sys
from .extracttitle import extract_title
from .markdowntohtmlnode import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_content, template_content = "", ""

    with open(from_path, "r") as markdown_file:
        md_content = markdown_file.read()

    with open(template_path, "r") as html_template:
        template_content = html_template.read()

    md_as_html_node = markdown_to_html_node(md_content)
    html_content = md_as_html_node.to_html()

    try:
        title = extract_title(md_content)
    except Exception as e:
        print(f"Exception {e}")
        sys.exit(1)

    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    dir_name = os.path.dirname(dest_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    with open(dest_path, "w") as output_file:
        output_file.write(final_html)
