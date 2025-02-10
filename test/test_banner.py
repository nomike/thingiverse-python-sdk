# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.banner import Banner

class TestBanner(unittest.TestCase):
    """Banner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Banner:
        """Test Banner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Banner`
        """
        model = Banner()
        if include_optional:
            return Banner(
                banner_image = '',
                big_banner_image = '',
                banner_tablet_image = '',
                banner_mobile_image = '',
                banner_url = '',
                banner_video = '',
                big_banner_video = '',
                banner_tablet_video = '',
                banner_mobile_video = '',
                location = ''
            )
        else:
            return Banner(
        )
        """

    def testBanner(self):
        """Test Banner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
