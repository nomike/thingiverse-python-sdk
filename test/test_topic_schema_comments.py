# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.topic_schema_comments import TopicSchemaComments

class TestTopicSchemaComments(unittest.TestCase):
    """TopicSchemaComments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TopicSchemaComments:
        """Test TopicSchemaComments
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TopicSchemaComments`
        """
        model = TopicSchemaComments()
        if include_optional:
            return TopicSchemaComments(
                count = 56,
                threaded_url = '',
                url = ''
            )
        else:
            return TopicSchemaComments(
        )
        """

    def testTopicSchemaComments(self):
        """Test TopicSchemaComments"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
