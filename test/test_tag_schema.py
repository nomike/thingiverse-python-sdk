# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tag_schema import TagSchema

class TestTagSchema(unittest.TestCase):
    """TagSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagSchema:
        """Test TagSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagSchema`
        """
        model = TagSchema()
        if include_optional:
            return TagSchema(
                name = 'Benchy',
                url = 'https://staging.thingiverse.com/tags/benchy',
                count = 76,
                things_url = 'https://api.thingiverse.com/tags/benchy/things',
                absolute_url = '/tag:Benchy'
            )
        else:
            return TagSchema(
        )
        """

    def testTagSchema(self):
        """Test TagSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
