import requests
import json

# URL setup for the GitHub API
base_url = "https://api.github.com/users/"

# Gets GitHub events for a user
def get_github_events(user):
    url = f"{base_url}{user}/events"
    response = requests.get(url)
    
    # Check if the request was successful and return data
    if response.status_code == 200:
        user_data = response.json()
    else:
        print("failed to fetch data")
        print(response)
    return user_data

def main():
    # Prompt user for a GitHub username
    print("Please enter a username: ")
    username = input()
    user_info = get_github_events(username)
    commits = 0

    # Check if user_info is not empty
    if user_info:
        print(f"Recent github events for {username}:")
        # Count the number of commits
        for event in user_info:
            if event['type'] == 'CommitCommentEvent':
                commits += 1
        # Print event occured in {repo} {name} at {created at}
        for event in user_info:
            if event['type'] == 'CommitCommentEvent':
                print(f"--  {username} commented on a commit at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'CreateEvent':
                print(f"--  {username} created a repository at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'DeleteEvent':
                print(f"--  {username} deleted a repository at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'ForkEvent':
                print(f"--  {username} forked a repository at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'IssuesCommentEvent':
                print(f"--  {username} commented on an issue at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'IssuesEvent':
                print(f"--  {username} opened an issue at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'MemberEvent':
                print(f"--  {username} added a member at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'PublicEvent':
                print(f"--  {username} made a repository public at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'PullRequestEvent':
                print(f"--  {username} created a pull request at {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'PushEvent':
                print(f"--  {username} pushed to {event['repo']['name']} at {event['created_at']}")
            elif event['type'] == 'WatchEvent':
                print(f"--  {username} starred a repository at {event['repo']['name']} at {event['created_at']}")
            else:
                print(f"--  {username} performed an unknown action at {event['repo']['name']} at {event['created_at']}")

# Hopefully works :D
main()
