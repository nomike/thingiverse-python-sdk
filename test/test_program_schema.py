# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.program_schema import ProgramSchema

class TestProgramSchema(unittest.TestCase):
    """ProgramSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProgramSchema:
        """Test ProgramSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProgramSchema`
        """
        model = ProgramSchema()
        if include_optional:
            return ProgramSchema(
                body = openapi_client.models.program_schema_body.program_schema_body(
                    id = 491683, 
                    name = 'SnapMaker', )
            )
        else:
            return ProgramSchema(
        )
        """

    def testProgramSchema(self):
        """Test ProgramSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
