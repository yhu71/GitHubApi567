"""
Author: Ying Hu
This is for Homework 04a - Develop with the Perspective of the Tester in mind
"""

import requests
import json


def check_repo_and_commits(github_user_id):
    # Use a dictionary to store the result, key = repo name, value = number of commits
    repository = {}
    # Retrieving a user's repositories:
    try:
        user_repos = requests.get(f'https://api.github.com/users/{github_user_id}/repos')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    parsed_user_repos = json.loads(user_repos.text)

    # Retrieving the commits of a repository:
    for repo in parsed_user_repos:
        if "name" in repo:
            repo_name = repo["name"]

            try:
                repo_commits = requests.get(f'https://api.github.com/repos/{github_user_id}/{repo_name}/commits')
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)

            repo_commit = json.loads(repo_commits.text)

            repository[repo_name] = len(repo_commit)
            print(f'Repo: {repo_name} Number of commits: {len(repo_commit)}')
        else:
            raise SystemExit("Invalid input!")

    return repository


if __name__ == '__main__':
    check_repo_and_commits('richkempinski')
