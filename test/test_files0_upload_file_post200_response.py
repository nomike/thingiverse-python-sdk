# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.files0_upload_file_post200_response import Files0UploadFilePost200Response

class TestFiles0UploadFilePost200Response(unittest.TestCase):
    """Files0UploadFilePost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Files0UploadFilePost200Response:
        """Test Files0UploadFilePost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Files0UploadFilePost200Response`
        """
        model = Files0UploadFilePost200Response()
        if include_optional:
            return Files0UploadFilePost200Response(
                id = 56
            )
        else:
            return Files0UploadFilePost200Response(
        )
        """

    def testFiles0UploadFilePost200Response(self):
        """Test Files0UploadFilePost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
