"""
Author: Ying Hu
This is for Homework 04a - Develop with the Perspective of the Tester in mind
"""
import unittest
import requests
import json
from CheckRepoAndCommits import check_repo_and_commits


class CheckRepoAndCommitsTest(unittest.TestCase):
    def test_check_repo_and_commits(self):
        expected = {'ssw555tmHogwarts2020Spring': 3, 'Triangle567': 9}
        self.assertEqual(check_repo_and_commits('yhu71'), expected)


if __name__ == '__main__':
    unittest.main()
