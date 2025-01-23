import os
import re

folder_path = 'C:\\Users\\anowa\\Desktop\\scriptpractice\\obsidianimagefix'

def replace_image_path(file_name):
    # Read the content of the old file
    print(f"Reading {file_name}...")
    try:
        with open(file_name, 'r', encoding="utf8") as file:
            content = file.read()
    except UnicodeDecodeError:
        print(f"Failed to read {file_name} with UTF-8 encoding. Trying 'windows-1252' encoding.")
        with open(file_name, 'r', encoding="windows-1252") as file:
            content = file.read()

    # First substitution
    content = re.sub(r'\[Pasted image ', r'](../Images/Pasted%20image%20', content)

    # Second substitution
    content = re.sub(r'\]\]', r')', content)

    # Write the updated content to the new file
    with open(file_name, 'w') as file:
        file.write(content)

def get_markdown_files(folder_path):
    markdown_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def main():
    markdown_files = get_markdown_files(folder_path)
    for markdown_file in markdown_files:
        replace_image_path(markdown_file)

if __name__ == "__main__":
    main()