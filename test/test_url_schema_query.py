# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.url_schema_query import UrlSchemaQuery

class TestUrlSchemaQuery(unittest.TestCase):
    """UrlSchemaQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UrlSchemaQuery:
        """Test UrlSchemaQuery
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UrlSchemaQuery`
        """
        model = UrlSchemaQuery()
        if include_optional:
            return UrlSchemaQuery(
            )
        else:
            return UrlSchemaQuery(
        )
        """

    def testUrlSchemaQuery(self):
        """Test UrlSchemaQuery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
