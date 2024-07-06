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
    # Regular expression to match markdown headers
    header_regex = re.compile(r'^(#{1,6})\s*(.+)$', re.MULTILINE)
    sections = header_regex.split(markdown_text)
    
    new_content = []
    for i in range(1, len(sections), 3):
        header = sections[i]
        title = sections[i+1]
        content = sections[i+2]
        
        new_content.append(f"{header} {title}\n{content.strip()}\n\n[Back to Table of Contents](#table-of-contents)\n")
    
    return sections[0] + "".join(new_content)

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
