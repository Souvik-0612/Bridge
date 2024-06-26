import re

# Define the replacements with colored HTML
replacements = {
    "!s": '<span style="color:black;">♠</span>',
    "!h": '<span style="color:red;">♥</span>',
    "!c": '<span style="color:black;">♣</span>',
    "!d": '<span style="color:red;">♦</span>'
}

# Read the README template
with open('System note.md', 'r') as file:
    content = file.read()

# Replace the shortcuts with the corresponding HTML
for shortcut, entity in replacements.items():
    content = re.sub(re.escape(shortcut), entity, content)

# Write the updated content to a new README file
with open('README.md', 'w') as file:
    file.write(content)
