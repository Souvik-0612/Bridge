import re

def generate_toc(markdown_text):
    # Regular expression to match markdown headers
    header_regex = re.compile(r'^(#{1,6})\s*(.+)$', re.MULTILINE)
    matches = header_regex.findall(markdown_text)
    
    toc_lines = ["## Table of Contents\n"]
    for match in matches:
        level = len(match[0])
        title = match[1]
        link = re.sub(r'\s+', '-', title.lower())  # Create anchor link
        toc_lines.append(f"{'  ' * (level - 1)}- [{title}](#{link})")
    
    return "\n".join(toc_lines)

def add_back_to_toc_links(markdown_text):
    # Regular expression to match top-level headers only
    header_regex = re.compile(r'^(#)\s*(.+)$', re.MULTILINE)
    sections = header_regex.split(markdown_text)
    
    new_content = [sections[0]]  # Initial content before the first header
    for i in range(1, len(sections), 3):
        if sections[i].startswith('#'):
            header = sections[i]
            title = sections[i+1].strip()
            content = sections[i+2].strip()
            new_content.append(f"{header} {title}\n\n{content}\n\n[Back☝️](#table-of-contents)\n")
        else:
            new_content.append(sections[i] + sections[i+1])
    
    return "".join(new_content)

def insert_toc_into_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    toc = generate_toc(content)
    new_content = f"{toc}\n\n{add_back_to_toc_links(content)}"
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Example usage: insert TOC into README.md
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_toc.py <markdown_file>")
    else:
        insert_toc_into_markdown(sys.argv[1])
