# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.users_username_stats_by_day_start_date_end_date_get200_response_inner import UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner

class TestUsersUsernameStatsByDayStartDateEndDateGet200ResponseInner(unittest.TestCase):
    """UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner:
        """Test UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner`
        """
        model = UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner()
        if include_optional:
            return UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner(
                day = '2023-03-28',
                user_id = 56,
                views = 56,
                downloads = 56,
                likes = 56,
                collects = 56,
                watches = 56,
                comments = 56,
                makes = 56,
                derivatives = 56
            )
        else:
            return UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner(
        )
        """

    def testUsersUsernameStatsByDayStartDateEndDateGet200ResponseInner(self):
        """Test UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
