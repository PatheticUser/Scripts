import os

def rename_files(directory, start, end):
    files = sorted(os.listdir(directory))  # Sort files to rename in order
    num_files = min(len(files), end - start + 1)  # Ensure we don't exceed available files
    
    for index, filename in enumerate(files[:num_files], start):
        old_path = os.path.join(directory, filename)
        new_name = f"{index}{os.path.splitext(filename)[1]}"  # Keep the original extension
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

# Example usage
directory_path = "/storage/emulated/0/Shows/Regular Show" #Change this to your directory
start_num = 14  # Change to your desired starting number
end_num = 37  # Change to your desired ending number

rename_files(directory_path, start_num, end_num)
