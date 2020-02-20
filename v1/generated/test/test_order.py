# coding: utf-8

"""
    Carbon API (Draft)

    An API to interact with Carbon's Manufacturing Cloud including 3D model upload, automated order processing and part history.  Getting started ---------------  - [Generate and download an API key](https://carbon3d.print.carbon3d.com/api_keys)   - Your API key and client secret will be downloaded into a secret.json file.  - [Use generated API key to generate a JWT token](/token_generator) from the api key.   - If your API key is revoked, this token will no longer work.  - Authorize with generated token  - Upload mesh files  - Create orders  - Monitor order status   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.order import Order  # noqa: E501
from carbon3d.rest import ApiException

class TestOrder(unittest.TestCase):
    """Order unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Order
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.order.Order()  # noqa: E501
        if include_optional :
            return Order(
                uuid = '0', 
                status = 'open', 
                order_number = '0', 
                printed_parts = [
                    carbon3d.models.printed_part_ref.PrintedPartRef(
                        uuid = '0', 
                        part_uuid = '0', 
                        status = 'waiting', )
                    ], 
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                route_to = [
                    '0'
                    ]
            )
        else :
            return Order(
                uuid = '0',
                order_number = '0',
                printed_parts = [
                    carbon3d.models.printed_part_ref.PrintedPartRef(
                        uuid = '0', 
                        part_uuid = '0', 
                        status = 'waiting', )
                    ],
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testOrder(self):
        """Test Order"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
