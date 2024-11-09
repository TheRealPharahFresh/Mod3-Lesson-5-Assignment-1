# Task 1: Directory Inspector:

# Problem Statement: 
# Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

import os

def list_directory_contents(path):
    try:
        items = os.listdir(path)

    

        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                print(f"File: {item}")
            elif os.path.isdir(item_path):
                print(f"Directory {item}")
    
    except FileNotFoundError:
        print(f"Error: This path {path} does not exist")
    except PermissionError:
        print(f"Error: Permission denied to access {path}")

directory = input("Enter Directory")
list_directory_contents(directory)
    




    