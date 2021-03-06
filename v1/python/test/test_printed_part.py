# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.0.8
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.printed_part import PrintedPart  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintedPart(unittest.TestCase):
    """PrintedPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintedPart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.printed_part.PrintedPart()  # noqa: E501
        if include_optional :
            return PrintedPart(
                uuid = '0', 
                part_uuid = '0', 
                model_uuid = '0', 
                part_number = '0', 
                build_uuid = '0', 
                part_order_uuid = '0', 
                part_order_number = '0', 
                print_order_uuid = '0', 
                print_order_number = '0', 
                print_id = '0', 
                serial_number = '0', 
                tags = carbon3d.models.printed_part_tags.PrintedPart_tags(
                    part_number = {
                        'key' : '0'
                        }, 
                    part = {
                        'key' : '0'
                        }, 
                    printed_part = {
                        'key' : '0'
                        }, ), 
                status = 'waiting', 
                genealogy = {"status":"printed","build_info":{"build_uuid":"29b2c0e9-ba72-45b0-b0f6-4005f0c2327a","traveler_url":"http://<url>","slice_video_url":"http://<url>"},"print_info":{"queued_at":"2019-10-11T21:25:00.000Z","printer_serial":"5Y01GZ","print_uuid":"2992c0e9-ba72-45b0-b0f6-4005f0c2327a","printed_part_serial":"123334-2","started_at":"2019-10-11T21:30:00.000Z","finished_at":"2019-10-11T21:38:00.000Z","platform_serial":"6P64234","cassette_serial":"7C124234"}}, 
                error = '0'
            )
        else :
            return PrintedPart(
                uuid = '0',
                part_uuid = '0',
                status = 'waiting',
        )

    def testPrintedPart(self):
        """Test PrintedPart"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
