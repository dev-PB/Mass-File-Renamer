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
    
def get_naming_convention():
    print("Enter the naming convention: ")
    naming_conv = input()
    return naming_conv

path = get_path()
files = sorted(os.listdir(path))
new_name_root = get_naming_convention()
ignore = []

for i, file in enumerate(files, 1):
    type = os.path.splitext(file)[1]
    new_name = new_name_root + str(i) + type

    while new_name in files:
        i += 1
        ignore.append(new_name)
        new_name = new_name_root + str(i) + type

    if file not in ignore:
        os.rename(path + "\\" + file, path + "\\" + new_name)
    