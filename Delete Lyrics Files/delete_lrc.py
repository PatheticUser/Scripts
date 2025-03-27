import os

def delete_lrc_files():
    current_dir = os.getcwd()
    deleted_files = []
    
    for file in os.listdir(current_dir):
        if file.endswith(".lrc"):
            file_path = os.path.join(current_dir, file)
            try:
                os.remove(file_path)
                deleted_files.append(file)
            except Exception as e:
                print(f"Error deleting {file}: {e}")

    if deleted_files:
        print("Deleted LRC files:")
        for file in deleted_files:
            print(f"- {file}")
    else:
        print("No LRC files found.")

if __name__ == "__main__":
    delete_lrc_files()
