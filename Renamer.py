import os

def get_path():

    while True:
        print("Enter the folder path: ")
        path = input() 

        if os.path.isdir(path) and os.path.exists(path):
            break
        else:
            print("Invalid path, please enter a path to a folder.")

    print("Selected path: " + path)
    return path

path = get_path()