import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def rename_songs_from_metadata(directory):
    """
    Renames MP3 files in the specified directory using their 'Title' metadata field.
    If the title is not available, it skips the file.
    
    Args:
        directory (str): Path to the directory containing MP3 files.
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(".mp3"):
            old_path = os.path.join(directory, filename)
            
            try:
                # Load MP3 file metadata
                audio = MP3(old_path, ID3=EasyID3)
                title = audio.get("title", [None])[0]  # Get the Title field
                
                if title:
                    # Generate the new filename using the title
                    new_name = f"{title}.mp3"
                    new_path = os.path.join(directory, new_name)
                    
                    # Rename the file
                    if old_path != new_path:
                        os.rename(old_path, new_path)
                        print(f"Renamed: {filename} -> {new_name}")
                else:
                    print(f"No title metadata found for: {filename}")
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example Usage
if __name__ == "__main__":
    # Use the current directory by default
    directory_path = os.path.dirname(os.path.abspath(__file__))  # Current folder with the script
    rename_songs_from_metadata(directory_path)
