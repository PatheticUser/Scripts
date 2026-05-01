import os
import subprocess
import requests
import shutil

def check_git_installed():
    """Checks if git is available in the system PATH."""
    if not shutil.which("git"):
        print("Error: 'git' is not installed.")
        return False
    return True

def get_interactive_inputs():
    """Prompts the user for necessary configuration."""
    username = input("Enter the GitHub username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return None, None

    default_dir = os.path.join(os.getcwd(), f"{username}_repos")
    target_dir = input(f"Enter target directory (default: {default_dir}): ").strip()
    
    if not target_dir:
        target_dir = default_dir
        
    return username, target_dir

def sync_repos():
    if not check_git_installed():
        return

    username, target_dir = get_interactive_inputs()
    if not username:
        return

    if not os.path.exists(target_dir):
        try:
            os.makedirs(target_dir)
            print(f"Created workspace: {target_dir}")
        except OSError as e:
            print(f"Directory creation failed: {e}")
            return

    # API Request - Using pagination to ensure all repos are caught
    api_url = f"https://api.github.com/users/{username}/repos"
    params = {"per_page": 100}
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        repos = response.json()

        if not repos:
            print(f"No public repositories found for {username}.")
            return

        print(f"\nFound {len(repos)} repositories. Proceed with sync? (y/n)")
        if input("> ").lower() != 'y':
            return

        for repo in repos:
            name = repo["name"]
            url = repo["clone_url"]
            path = os.path.join(target_dir, name)

            if os.path.exists(path):
                print(f"[*] Repository '{name}' exists. Checking for updates...")
                try:
                    # Run git pull inside the repo directory
                    subprocess.run(
                        ["git", "-C", path, "pull"], 
                        check=True, 
                        capture_output=True, 
                        text=True
                    )
                    print(f"    - '{name}' is now up to date.")
                except subprocess.CalledProcessError as e:
                    print(f"    [!] Update failed for {name}: {e.stderr.strip()}")
            else:
                print(f"[+] Cloning new repository '{name}'...")
                try:
                    subprocess.run(
                        ["git", "clone", url, path], 
                        check=True, 
                        capture_output=True
                    )
                except subprocess.CalledProcessError as e:
                    print(f"    [!] Clone failed for {name}.")

        print("\nAll repositories processed successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    sync_repos()