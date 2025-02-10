# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.comment_schema import CommentSchema

class TestCommentSchema(unittest.TestCase):
    """CommentSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentSchema:
        """Test CommentSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentSchema`
        """
        model = CommentSchema()
        if include_optional:
            return CommentSchema(
                id = 56,
                url = 'https://api.thingiverse.com/comments/1',
                target_type = 'grouptopic',
                target_id = 56,
                public_url = 'https://www.thingiverse.local/thing:1/comments#comment-1',
                target_url = '',
                body = '',
                body_html = '',
                user = openapi_client.models.user_summary_schema_1.user_summary_schema_1(
                    id = 1336, 
                    name = 'CreativeTools', 
                    first_name = 'Creative', 
                    last_name = 'Tools', 
                    url = 'https://api.thingiverse.com/users/CreativeTools', 
                    public_url = 'https://www.thingiverse.com/CreativeTools', 
                    thumbnail = 'https://cdn.thingiverse.com/renders/b3/a5/0c/45/3f/CT_thumb_medium.jpg', 
                    count_of_followers = 9828, 
                    count_of_following = 975, 
                    count_of_designs = 147, 
                    make_count = 56, 
                    accepts_tips = False, 
                    is_following = True, 
                    location = 'Halmstad, Sweden', 
                    cover = 'https://cdn.thingiverse.com/renders/6d/54/65/5c/9b/Thingiverse_background_3_preview_large.jpg', 
                    is_admin = False, 
                    is_moderator = False, 
                    is_featured = False, 
                    is_verified = False, ),
                added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified = None,
                parent_id = 0,
                parent_url = '',
                parent_user_name = '',
                is_deleted = True,
                attachments = [
                    openapi_client.models.comment_attachments_inner.Comment_attachments_inner(
                        id = 56, 
                        name = '', 
                        download_url = '', )
                    ],
                needs_moderation = True,
                is_root_comment = True,
                has_children = True,
                recaptcha_token = '',
                can_comment = True,
                things = [
                    openapi_client.models.thing_schema.thing_schema(
                        id = 763622, 
                        name = '#3DBenchy - The jolly 3D printing torture-test by CreativeTools.se', 
                        thumbnail = 'https://cdn.thingiverse.com/renders/62/ab/d7/e3/ea/1_3D-printed_3DBenchy_by_Creative-Tools.com_display_large.JPG', 
                        url = 'https://api.thingiverse.com/things/763622', 
                        public_url = 'https://wwww.thingiverse.com/thing:763622', 
                        creator = openapi_client.models.user_summary_schema_1.user_summary_schema_1(
                            id = 1336, 
                            name = 'CreativeTools', 
                            first_name = 'Creative', 
                            last_name = 'Tools', 
                            url = 'https://api.thingiverse.com/users/CreativeTools', 
                            public_url = 'https://www.thingiverse.com/CreativeTools', 
                            thumbnail = 'https://cdn.thingiverse.com/renders/b3/a5/0c/45/3f/CT_thumb_medium.jpg', 
                            count_of_followers = 9828, 
                            count_of_following = 975, 
                            count_of_designs = 147, 
                            make_count = 56, 
                            accepts_tips = False, 
                            is_following = True, 
                            location = 'Halmstad, Sweden', 
                            cover = 'https://cdn.thingiverse.com/renders/6d/54/65/5c/9b/Thingiverse_background_3_preview_large.jpg', 
                            is_admin = False, 
                            is_moderator = False, 
                            is_featured = False, 
                            is_verified = False, ), 
                        added = '2015-04-09T12:57:28Z', 
                        modified = '2015-04-09T12:57:28Z', 
                        is_published = 1, 
                        is_wip = 1, 
                        is_featured = True, 
                        is_nsfw = False, 
                        is_ai = False, 
                        like_count = 80855, 
                        is_liked = True, 
                        collect_count = 135811, 
                        is_collected = False, 
                        comment_count = 808, 
                        is_watched = False, 
                        default_image = openapi_client.models.image_summary_schema.image_summary_schema(
                            id = 2012326, 
                            url = 'https://cdn.thingiverse.com/assets/ee/dc/9a/fb/74/1_3D-printed_3DBenchy_by_Creative-Tools.com.JPG', 
                            name = '1_3D-printed_3DBenchy_by_Creative-Tools.com.JPG', 
                            sizes = [
                                openapi_client.models.image_summary_sizes_inner.ImageSummary_sizes_inner(
                                    type = 'thumb', 
                                    size = 'large', 
                                    url = 'https://cdn.thingiverse.com/renders/62/ab/d7/e3/ea/1_3D-printed_3DBenchy_by_Creative-Tools.com_thumb_large.JPG', )
                                ], 
                            added = '2015-04-09T12:55:23Z', ), 
                        description = 'Creative Tools](https:\/\/www.creativetools.se\/) Creative Tools supplies 3D printer and 3D scanner products incl filaments, accessories and support and also 3D software for leading CAD, modeling, animation, and rendering.', 
                        instructions = '', 
                        description_html = '<div><p><a rel=\"ugc nofollow\" href=\"https://www.creativetools.se/\">Creative Tools</a> Creative Tools supplies 3D printer and 3D scanner products incl filaments, accessories and support and also 3D software for leading CAD, modeling, animation, and rendering.</p></div>', 
                        instructions_html = '<div><\/div>\n', 
                        details = '', 
                        details_parts = [
                            None
                            ], 
                        edu_details = '', 
                        edu_details_parts = [
                            None
                            ], 
                        license = 'Creative Commons - Attribution - No Derivatives', 
                        allows_derivatives = False, 
                        files_url = 'https://api.thingiverse.com/things/763622/files', 
                        images_url = 'https://api.thingiverse.com/things/763622/images', 
                        likes_url = 'https://api.thingiverse.com/things/763622/likes', 
                        ancestors_url = 'https://api.thingiverse.com/things/763622/ancestors', 
                        derivatives_url = 'https://api.thingiverse.com/things/763622/derivatives', 
                        tags_url = '', 
                        tags = [
                            openapi_client.models.tag_schema.tag_schema(
                                name = 'Benchy', 
                                url = 'https://staging.thingiverse.com/tags/benchy', 
                                count = 76, 
                                things_url = 'https://api.thingiverse.com/tags/benchy/things', 
                                absolute_url = '/tag:Benchy', )
                            ], 
                        categories_url = 'https://api.thingiverse.com/things/763622/categories', 
                        file_count = 24, 
                        is_purchased = 1, 
                        app_id = 56, 
                        download_count = 3169879, 
                        view_count = 4065156, 
                        education = openapi_client.models.thing_education.Thing_education(
                            grades = [
                                ''
                                ], 
                            subjects = [
                                ''
                                ], ), 
                        remix_count = 0, 
                        make_count = 4518, 
                        app_count = 3, 
                        root_comment_count = 535, 
                        moderation = '', 
                        is_derivative = False, 
                        ancestors = [], 
                        can_comment = True, 
                        type_name = 'Thing', 
                        is_banned = False, 
                        is_comments_disabled = False, 
                        needs_moderation = 0, 
                        is_decoy = 0, 
                        zip_data = openapi_client.models.thing_zip_data.Thing_zip_data(
                            files = [
                                openapi_client.models.thing_zip_data_files_inner.Thing_zip_data_files_inner(
                                    name = '3DBenchy_Broschure_3DBenchy.com.pdf', 
                                    url = 'https://cdn.thingiverse.com/assets/a7/2c/bd/ba/ea/3DBenchy_Broschure_3DBenchy.com.pdf', )
                                ], ), )
                    ]
            )
        else:
            return CommentSchema(
                id = 56,
        )
        """

    def testCommentSchema(self):
        """Test CommentSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
