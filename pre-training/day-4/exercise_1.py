import requests
import sys

def fetch_github_profile(username):
  base_url = f"https://api.github.com/users/{username}"
    
  try:
    response = requests.get(base_url)
        
    if response.status_code == 404:
      print(f"Error: User '{username}' not found.")
      return
    elif response.status_code == 403:
      print("Error: GitHub Rate limit hit. Try again in an hour.")
      return
        
    response.raise_for_status()
    data = response.json()

    print(f"\n--- Profile: {data.get('login')} ---")
    print(f"Bio: {data.get('bio') or 'No bio provided'}")
    print(f"Public Repos: {data.get('public_repos')}")
    print(f"Followers: {data.get('followers')}")

    repo_response = requests.get(f"{base_url}/repos?sort=stars&per_page=5")
    repos = repo_response.json()
        
    print("\nTop 5 Repos by Stars:")
    for repo in repos:
      print(f"- {repo['name']}: ⭐ {repo['stargazers_count']} | Language: {repo['language']}")

  except requests.exceptions.ConnectionError:
    print("Error: Network issue. Check your internet connection.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
  user = sys.argv[1] if len(sys.argv) > 1 else "devsam0"
  fetch_github_profile(user)