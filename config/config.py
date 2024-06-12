
def update_file(file_path, content):
    """Update the content of a file."""
    with open(file_path, 'w') as file:
        file.write(content)
