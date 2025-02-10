import os

folder_path = "C:/Users/Ash/Documents/Code/C#"

for root, dirs, files in os.walk(folder_path):
    print(f"Folder: {root}")
    for file in files:
        print(f"  File: {file}")
