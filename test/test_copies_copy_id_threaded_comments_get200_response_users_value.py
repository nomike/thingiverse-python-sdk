# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.copies_copy_id_threaded_comments_get200_response_users_value import CopiesCopyIdThreadedCommentsGet200ResponseUsersValue

class TestCopiesCopyIdThreadedCommentsGet200ResponseUsersValue(unittest.TestCase):
    """CopiesCopyIdThreadedCommentsGet200ResponseUsersValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopiesCopyIdThreadedCommentsGet200ResponseUsersValue:
        """Test CopiesCopyIdThreadedCommentsGet200ResponseUsersValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopiesCopyIdThreadedCommentsGet200ResponseUsersValue`
        """
        model = CopiesCopyIdThreadedCommentsGet200ResponseUsersValue()
        if include_optional:
            return CopiesCopyIdThreadedCommentsGet200ResponseUsersValue(
                user_name = '',
                user_avatar = '',
                is_admin = 0
            )
        else:
            return CopiesCopyIdThreadedCommentsGet200ResponseUsersValue(
        )
        """

    def testCopiesCopyIdThreadedCommentsGet200ResponseUsersValue(self):
        """Test CopiesCopyIdThreadedCommentsGet200ResponseUsersValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
