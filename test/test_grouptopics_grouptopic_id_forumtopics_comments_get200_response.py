# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.grouptopics_grouptopic_id_forumtopics_comments_get200_response import GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response

class TestGrouptopicsGrouptopicIdForumtopicsCommentsGet200Response(unittest.TestCase):
    """GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response:
        """Test GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response`
        """
        model = GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response()
        if include_optional:
            return GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response(
                topics_comments = [
                    null
                    ],
                total = 0
            )
        else:
            return GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response(
        )
        """

    def testGrouptopicsGrouptopicIdForumtopicsCommentsGet200Response(self):
        """Test GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
