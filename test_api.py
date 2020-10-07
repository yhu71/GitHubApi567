import unittest
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from CheckRepoAndCommits import get_repos


class TestAPI(unittest.TestCase):
    @patch('requests.get')
    def test_getting_repos(self, mock_get_repos):
        # Configure the mock to return a response with an OK status code.
        mock_get_repos.return_value.ok = True

        # Call the service, which will send a request to the server.
        response = get_repos('11111111')

        # If the request is sent successfully, then I expect a response to be returned.
        assert_is_not_none(response)




if __name__ == '__main__':
    unittest.main()
