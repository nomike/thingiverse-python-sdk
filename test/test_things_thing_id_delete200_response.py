# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.things_thing_id_delete200_response import ThingsThingIdDelete200Response

class TestThingsThingIdDelete200Response(unittest.TestCase):
    """ThingsThingIdDelete200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ThingsThingIdDelete200Response:
        """Test ThingsThingIdDelete200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ThingsThingIdDelete200Response`
        """
        model = ThingsThingIdDelete200Response()
        if include_optional:
            return ThingsThingIdDelete200Response(
                error = ''
            )
        else:
            return ThingsThingIdDelete200Response(
        )
        """

    def testThingsThingIdDelete200Response(self):
        """Test ThingsThingIdDelete200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
