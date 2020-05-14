# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  A Carbon DLS API token ([JWT](https://en.wikipedia.org/wiki/JSON_Web_Token)) must be included with each request to the API.  Steps to create API tokens: - Create and download an API key [here](https://print.carbon3d.com/api_keys) - For testing: Generate JWT tokens using the [token generator](/token_generator) - For production: Generate JWT tokens dynamically (<em>see authtoken-create.py example</em>) - A valid Carbon API token must be included as <code>Authorization: Bearer [token]</code> HTTP header.  This API provides a programmatic interface for submitting part (and soon build) orders. The general process for creating an order is as follows:  - Upload model files to the API with the [/models](#/Models) endpoint - Create parts that reference a model and a part number with the [/parts](#/Parts) endpoint   -  Part numbers can be created [here](https://print.carbon3d.com/catalog_parts) - Create an order with the [/orders](#/Orders) endpoint  Uploaded models, parts and orders can be retrieved either in bulk or by UUID at the [/models](#/Models), [/parts](#/Parts) and [/orders](#/Orders) endpoints, respectively.  Once a part order is submitted, automatic packing will create one or more builds (for mass-customization applications only).  Builds can be retrieved either in bulk or by UUID at the [/builds](#/Builds) endpoint. - Build attachments (traveler, slice video) can be retrieved by UUID at the [/attachments](#/Attachments) endpoint.  This API also provides a programmatic interface to access [printer](#/Printers) (fleet) status and query for [prints](#/Prints).   # noqa: E501

    The version of the OpenAPI document: 0.0.5
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.printed_parts_response import PrintedPartsResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintedPartsResponse(unittest.TestCase):
    """PrintedPartsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintedPartsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.printed_parts_response.PrintedPartsResponse()  # noqa: E501
        if include_optional :
            return PrintedPartsResponse(
                limit = 56, 
                offset = 56, 
                total_count = 56, 
                parts = [
                    {"uuid":"6401c93f-f340-4da2-8784-bddd4065e75c","part_uuid":"3585e82c-999f-4594-b619-5925c0203237","part_number":"12345","order_uuid":"3585e82c-999f-4594-b619-5925c0203777","model_uuid":"3cc663e2-c762-4f8f-8997-30d17bc13e8d","status":"waiting","genealogy":{"build_info":{},"print_info":{}},"build_uuid":"7482212b-1fd4-45aa-aba4-00db8cf8776d"}
                    ]
            )
        else :
            return PrintedPartsResponse(
        )

    def testPrintedPartsResponse(self):
        """Test PrintedPartsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
