import os

def replace_suits_and_convert(input_filepath, output_filepath):
    with open(input_filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace placeholders with suit symbols and color
    content = content.replace('!s', '<span style="color:black;">♠</span>')
    content = content.replace('!h', '<span style="color:red;">♥</span>')
    content = content.replace('!d', '<span style="color:red;">♦</span>')
    content = content.replace('!c', '<span style="color:black;">♣</span>')

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

    with open(output_filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    input_filepath = 'system_notes.md'  # Adjust this path as needed
    output_filepath = 'docs\index.md'  # Adjust this path as needed
    replace_suits_and_convert(input_filepath, output_filepath)

if __name__ == "__main__":
    main()
