import os
import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Spotify API credentials
SPOTIFY_CLIENT_ID = "your_client_id_here"  # Replace with your Spotify Client ID
SPOTIFY_CLIENT_SECRET = "your_client_secret_here"  # Replace with your Spotify Client Secret

# Initialize Spotify API client
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

def search_song_on_spotify(query):
    """
    Search for a song on Spotify using the query string.
    
    Args:
        query (str): Song name or filename to search for.
    
    Returns:
        str: The verified song name from Spotify, or None if not found.
    """
    try:
        results = spotify.search(q=query, type="track", limit=1)
        if results["tracks"]["items"]:
            return results["tracks"]["items"][0]["name"]  # Return the song title
    except Exception as e:
        print(f"Error while searching on Spotify: {e}")
    return None

def rename_songs_with_ai(directory):
    """
    Renames songs in the specified directory by verifying their names using Spotify API.
    
    Args:
        directory (str): Path to the directory containing the songs.
    """
    for filename in os.listdir(directory):
        # Skip if it's not a file
        if not os.path.isfile(os.path.join(directory, filename)):
            continue

        # Extract the file extension
        file_ext = os.path.splitext(filename)[1]
        
        # Clean the filename to use as a query
        query = re.sub(r"[-_]", " ", os.path.splitext(filename)[0]).strip()
        
        # Search for the song on Spotify
        verified_name = search_song_on_spotify(query)
        if verified_name:
            # Rename the file with the verified name
            new_name = f"{verified_name}{file_ext}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
        else:
            print(f"Could not verify song name for: {filename}")

# Example Usage
directory_path = "path/to/your/songs"  # Replace with your music folder path
rename_songs_with_ai(directory_path)
