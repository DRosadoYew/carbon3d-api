# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  A Carbon DLS API token ([JWT](https://en.wikipedia.org/wiki/JSON_Web_Token)) must be included with each request to the API.  Steps to create API tokens: - Create and download an API key [here](https://print.carbon3d.com/api_keys) - For testing: Generate JWT tokens using the [token generator](/token_generator) - For production: Generate JWT tokens dynamically (<em>see authtoken-create.py example</em>) - A valid Carbon API token must be included as <code>Authorization: Bearer [token]</code> HTTP header.  This API provides a programmatic interface for submitting part (and soon build) orders. The general process for creating an order is as follows:  - Upload model files to the API with the [/models](#/Models) endpoint - Create parts that reference a model and a part number with the [/parts](#/Parts) endpoint   -  Part numbers can be created [here](https://print.carbon3d.com/catalog_parts) - Create an order with the [/orders](#/Orders) endpoint  Uploaded models, parts and orders can be retrieved either in bulk or by UUID at the [/models](#/Models), [/parts](#/Parts) and [/orders](#/Orders) endpoints, respectively.  Once a part order is submitted, automatic packing will create one or more builds (for mass-customization applications only).  Builds can be retrieved either in bulk or by UUID at the [/builds](#/Builds) endpoint. - Build attachments (traveler, slice video) can be retrieved by UUID at the [/attachments](#/Attachments) endpoint.  This API also provides a programmatic interface to access [printer](#/Printers) (fleet) status and query for [prints](#/Prints).   # noqa: E501

    The version of the OpenAPI document: 0.0.3
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.printer import Printer  # noqa: E501
from carbon3d.rest import ApiException

class TestPrinter(unittest.TestCase):
    """Printer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Printer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.printer.Printer()  # noqa: E501
        if include_optional :
            return Printer(
                name = '0', 
                serial = '0', 
                hw_type = '0', 
                url = '0', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = carbon3d.models.printer_status.Printer_status(
                    alerts = [
                        '0'
                        ], 
                    printer_state = '0', 
                    software_version = '0', ), 
                prints = carbon3d.models.printer_prints.Printer_prints(
                    last = carbon3d.models.print.Print(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    current = carbon3d.models.print.Print(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    next = carbon3d.models.print.Print(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    queue_length = 56, )
            )
        else :
            return Printer(
                name = '0',
                serial = '0',
                hw_type = '0',
                url = '0',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = carbon3d.models.printer_status.Printer_status(
                    alerts = [
                        '0'
                        ], 
                    printer_state = '0', 
                    software_version = '0', ),
                prints = carbon3d.models.printer_prints.Printer_prints(
                    last = carbon3d.models.print.Print(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    current = carbon3d.models.print.Print(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    next = carbon3d.models.print.Print(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    queue_length = 56, ),
        )

    def testPrinter(self):
        """Test Printer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
