# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.users_username_search_term_get200_response import UsersUsernameSearchTermGet200Response

class TestUsersUsernameSearchTermGet200Response(unittest.TestCase):
    """UsersUsernameSearchTermGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersUsernameSearchTermGet200Response:
        """Test UsersUsernameSearchTermGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersUsernameSearchTermGet200Response`
        """
        model = UsersUsernameSearchTermGet200Response()
        if include_optional:
            return UsersUsernameSearchTermGet200Response(
                total = 56,
                hits = [
                    ''
                    ]
            )
        else:
            return UsersUsernameSearchTermGet200Response(
        )
        """

    def testUsersUsernameSearchTermGet200Response(self):
        """Test UsersUsernameSearchTermGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
