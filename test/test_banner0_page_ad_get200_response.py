# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.banner0_page_ad_get200_response import Banner0PageAdGet200Response

class TestBanner0PageAdGet200Response(unittest.TestCase):
    """Banner0PageAdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Banner0PageAdGet200Response:
        """Test Banner0PageAdGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Banner0PageAdGet200Response`
        """
        model = Banner0PageAdGet200Response()
        if include_optional:
            return Banner0PageAdGet200Response(
                custom_ads = None,
                blocked_ad_variation = ''
            )
        else:
            return Banner0PageAdGet200Response(
        )
        """

    def testBanner0PageAdGet200Response(self):
        """Test Banner0PageAdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
