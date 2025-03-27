import os

def rename_files(start, end):
    directory = os.getcwd()  # Get the current directory where the script is running
    files = sorted(os.listdir(directory))  # Sort files to rename in order
    num_files = min(len(files), end - start + 1)  # Ensure we don't exceed available files
    
    for index, filename in enumerate(files[:num_files], start):
        old_path = os.path.join(directory, filename)
        new_name = f"{index}{os.path.splitext(filename)[1]}"  # Keep the original extension
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

# Get user input for start and end numbers
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

rename_files(start_num, end_num)
