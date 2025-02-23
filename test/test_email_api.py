# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.email_api import EmailApi


class TestEmailApi(unittest.TestCase):
    """EmailApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EmailApi()

    def tearDown(self) -> None:
        pass

    def test_email_post(self) -> None:
        """Test case for email_post

        Queuing emails
        """
        pass

    def test_email_thingiverse_enqueue_support_post(self) -> None:
        """Test case for email_thingiverse_enqueue_support_post

        Queue email to Thingiverse support
        """
        pass

    def test_email_type_enqueue_dmca_post(self) -> None:
        """Test case for email_type_enqueue_dmca_post

        Queue email to Thingiverse support (DMCA)
        """
        pass


if __name__ == '__main__':
    unittest.main()
