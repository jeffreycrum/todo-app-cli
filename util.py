def read_todos(filepath='todos.txt'):
    """Read a text file and return the list of text items"""
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content


def write_todos(content, filepath='todos.txt'):
    """Write a list of text items to a file"""
    with open(filepath, 'w') as file:
        file.writelines(content)
