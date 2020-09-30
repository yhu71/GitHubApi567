"""
Author: Ying Hu
This is for Homework 04a - Develop with the Perspective of the Tester in mind
"""
import unittest
from CheckRepoAndCommits import check_repo_and_commits


class CheckRepoAndCommitsTest(unittest.TestCase):
    def test_check_repo_and_commits(self):
        expected = {'csp': 2, 'hellogitworld': 30, 'helloworld': 6, 'Mocks': 10, 'Project1': 2,
                    'richkempinski.github.io': 9, 'threads-of-life': 1, 'try_nbdev': 2, 'try_nbdev2': 5}
        self.assertEqual(check_repo_and_commits('richkempinski'), expected, 'Repo or Commits not match.')


if __name__ == '__main__':
    unittest.main()
