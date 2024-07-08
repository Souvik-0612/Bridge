import re

# Define the replacements with colored HTML
replacements = {
    "!s": '<span style="color:black;">♠</span>',
    "!h": '<span style="color:red;">♥</span>',
    "!c": '<span style="color:black;">♣</span>',
    "!d": '<span style="color:red;">♦</span>'
}
def generate_toc(markdown_text):
    # Regular expression to match markdown headers
    header_regex = re.compile(r'^(#{1,6})\s*(.+)$', re.MULTILINE)
    matches = header_regex.findall(markdown_text)
    
    toc_lines = ["# Bridge System Notes \n", "## Table of Contents\n"]
    for match in matches:
        level = len(match[0])
        title = match[1]
        link=title.lower()
        link=re.sub(r'[^a-zA-Z0-9\s]','',link)
        link=re.sub(r'\s+$','',link)
        link = re.sub(r'\s+', '-', link)  # Create anchor link
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
        link=title.lower()
        link=re.sub(r'[^a-zA-Z0-9\s]','',link)
        link=re.sub(r'\s+$','',link)
        link = re.sub(r'\s+', '-', link)  # Create anchor link
        anchor="<a id=\"%s\"></a>"%(link)
        #new_content.append(f"{header} {title}\n{content.strip()}\n\n[Back☝️](#table-of-contents)\n")
        new_content.append(f"{header} {anchor}{title}\n{content.strip()}\n\n[🔙](#table-of-contents)\n")
    
    return sections[0] + "".join(new_content)

def insert_toc_into_markdown(file_path,file_path2):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    toc = generate_toc(content)
    new_content = f"{toc}\n\n{add_back_to_toc_links(content)}"
    
    # Replace the shortcuts with the corresponding HTML
    for shortcut, entity in replacements.items():
        new_content = re.sub(re.escape(shortcut), entity, new_content)
    

    #write
    with open(file_path2, 'w', encoding='utf-8') as file2:
        file2.write(new_content)


# Example usage: insert TOC into README.md
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python generate_toc.py <markdown_file> newfile")
    else:
        insert_toc_into_markdown(sys.argv[1],sys.argv[2])
