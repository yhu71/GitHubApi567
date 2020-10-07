"""
Author: Ying Hu
This is for Homework 05a - Isolate External Dependencies
"""
import os
import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none, assert_list_equal
from CheckRepoAndCommits import get_repos, get_commits
import json


class TestAPI(unittest.TestCase):
    def test_get_repos(self):
        # To test get repos for an existing user ID
        mock_get_repos_patcher = patch('CheckRepoAndCommits.get_repos')
        mock_get_repos = mock_get_repos_patcher.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/richkempinski_repos.json') as file:
            mock_get_repos.return_value = json.load(file)
        mock_get_repos_patcher.stop()
        repo = mock_get_repos()
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo[0].get("id"), 286633893)

    def test_get_repos_not_found(self):
        # To test get result for an user ID that not found
        mock_get_repos_patcher = patch('CheckRepoAndCommits.get_repos')
        mock_get_repos = mock_get_repos_patcher.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/NotFound.json') as file:
            mock_get_repos.return_value = json.load(file)
        mock_get_repos_patcher.stop()
        repo = mock_get_repos()
        self.assertEqual(repo.get('message'), "Not Found")

    def test_get_commits(self):
        # To test get commits info
        mock_get_commits_patcher = patch('CheckRepoAndCommits.get_commits')
        mock_get_commits = mock_get_commits_patcher.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/csp.json') as file:
            mock_get_commits.return_value = json.load(file)
        mock_get_commits.stop()
        commits = mock_get_commits()

        self.assertEqual(len(commits), 2)
        self.assertEqual(commits[0].get('node_id'),
                         'MDY6Q29tbWl0Mjg2NjMzODkzOjI5MTk1MjRkNzQxZmVmNDk5YmYzM2E2YzQ0MTM5NjUyMWZhZDQyNGQ=')


if __name__ == '__main__':
    unittest.main()
