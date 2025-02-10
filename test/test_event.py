# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.event import Event

class TestEvent(unittest.TestCase):
    """Event unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Event:
        """Test Event
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Event`
        """
        model = Event()
        if include_optional:
            return Event(
                id = 56,
                type = 56,
                message = '',
                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                targets = [
                    openapi_client.models.event_targets_inner.Event_targets_inner(
                        thumbnail = '', 
                        things_url = '', 
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
                            added = '2015-04-09T12:55:23Z', ), )
                    ],
                sources = [
                    null
                    ],
                subscription = openapi_client.models.event_subscription.Event_subscription(
                    users_url = '', )
            )
        else:
            return Event(
        )
        """

    def testEvent(self):
        """Test Event"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
