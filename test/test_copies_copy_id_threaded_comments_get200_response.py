# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.copies_copy_id_threaded_comments_get200_response import CopiesCopyIdThreadedCommentsGet200Response

class TestCopiesCopyIdThreadedCommentsGet200Response(unittest.TestCase):
    """CopiesCopyIdThreadedCommentsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopiesCopyIdThreadedCommentsGet200Response:
        """Test CopiesCopyIdThreadedCommentsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopiesCopyIdThreadedCommentsGet200Response`
        """
        model = CopiesCopyIdThreadedCommentsGet200Response()
        if include_optional:
            return CopiesCopyIdThreadedCommentsGet200Response(
                comments = {
                    'key' : openapi_client.models._copies__copy_id__threaded_comments_get_200_response_comments_value._copies__copy_id__threaded_comments_get_200_response_comments_value(
                        id = 0, 
                        add_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_date = null, 
                        body = '', 
                        user_id = 0, 
                        is_deleted = True, 
                        url = '', 
                        needs_moderation = 0, 
                        assets = [
                            ''
                            ], 
                        parent_id = 0, 
                        parent_user_name = '', 
                        parent_url = '', )
                    },
                users = {
                    'key' : openapi_client.models._copies__copy_id__threaded_comments_get_200_response_users_value._copies__copy_id__threaded_comments_get_200_response_users_value(
                        user_name = '', 
                        user_avatar = '', 
                        is_admin = 0, )
                    }
            )
        else:
            return CopiesCopyIdThreadedCommentsGet200Response(
        )
        """

    def testCopiesCopyIdThreadedCommentsGet200Response(self):
        """Test CopiesCopyIdThreadedCommentsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
