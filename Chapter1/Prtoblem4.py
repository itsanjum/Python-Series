import os

# Set the path (use '.' for current directory)
path = '.'

try:
    # Get list of entries in the directory
    contents = os.listdir(path)

    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory {path} does not exist.")
except PermissionError:
    print(f"Permission denied to access {path}.")
