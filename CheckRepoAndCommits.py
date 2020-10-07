"""
Author: Ying Hu
This is for Homework 04a - Develop with the Perspective of the Tester in mind
"""

import requests
import json


def get_repos(github_user_id):
    try:
        response = requests.get(f'https://api.github.com/users/{github_user_id}/repos')
        if response.ok:
            return response
        else:
            return None
    except requests.exceptions.Timeout:
        return 'Bad Response'


def get_commits(github_user_id, repo_name):
    try:
        response = requests.get(f'https://api.github.com/repos/{github_user_id}/{repo_name}/commits')
        if response.ok:
            return response
        else:
            return None
    except requests.exceptions.Timeout:
        return 'Bad Response'


def check_repo_and_commits(github_user_id):
    # Use a dictionary to store the result, key = repo name, value = number of commits
    repository = {}
    # Retrieving a user's repositories:
<<<<<<< HEAD
    user_repos = get_repos(github_user_id)
=======
    user_repos = requests.get(f'https://api.github.com/users/{github_user_id}/repos')
>>>>>>> parent of b31e066... update test
    parsed_user_repos = json.loads(user_repos.text)
    # Retrieving the commits of a repository:
    for repo in parsed_user_repos:
        repo_name = repo["name"]
<<<<<<< HEAD
        repo_commits = get_commits(github_user_id, repo_name)
=======

        repo_commits = requests.get(f'https://api.github.com/repos/{github_user_id}/{repo_name}/commits')
>>>>>>> parent of b31e066... update test
        repo_commit = json.loads(repo_commits.text)
        repository[repo_name] = len(repo_commit)
        print(f'Repo: {repo_name} Number of commits: {len(repo_commit)}')
    return repository


if __name__ == '__main__':
    check_repo_and_commits('richkempinski')
