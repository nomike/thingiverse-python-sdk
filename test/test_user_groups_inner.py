# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_groups_inner import UserGroupsInner

class TestUserGroupsInner(unittest.TestCase):
    """UserGroupsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGroupsInner:
        """Test UserGroupsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGroupsInner`
        """
        model = UserGroupsInner()
        if include_optional:
            return UserGroupsInner(
                id = 25,
                name = 'Engineering',
                public_url = 'https://www.thingiverse.com/groups/engineering'
            )
        else:
            return UserGroupsInner(
        )
        """

    def testUserGroupsInner(self):
        """Test UserGroupsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
