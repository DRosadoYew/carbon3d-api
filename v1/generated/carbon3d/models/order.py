# coding: utf-8

"""
    Carbon API (Draft)

    An API to interact with Carbon's Manufacturing Cloud including 3D model upload, automated order processing and part history.  Getting started ---------------  - [Generate and download an API key](https://carbon3d.print.carbon3d.com/api_keys)   - Your API key and client secret will be downloaded into a secret.json file.  - [Use generated API key to generate a JWT token](/token_generator) from the api key.   - If your API key is revoked, this token will no longer work.  - Authorize with generated token  - Upload mesh files  - Create orders  - Monitor order status   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class Order(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'uuid': 'str',
        'status': 'OrderStatus',
        'order_number': 'str',
        'printed_parts': 'list[PrintedPartRef]',
        'due_date': 'datetime',
        'route_to': 'list[str]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'status': 'status',
        'order_number': 'order_number',
        'printed_parts': 'printed_parts',
        'due_date': 'due_date',
        'route_to': 'route_to'
    }

    def __init__(self, uuid=None, status=None, order_number=None, printed_parts=None, due_date=None, route_to=None, local_vars_configuration=None):  # noqa: E501
        """Order - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._status = None
        self._order_number = None
        self._printed_parts = None
        self._due_date = None
        self._route_to = None
        self.discriminator = None

        self.uuid = uuid
        if status is not None:
            self.status = status
        self.order_number = order_number
        self.printed_parts = printed_parts
        self.due_date = due_date
        if route_to is not None:
            self.route_to = route_to

    @property
    def uuid(self):
        """Gets the uuid of this Order.  # noqa: E501

        Order UUID  # noqa: E501

        :return: The uuid of this Order.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Order.

        Order UUID  # noqa: E501

        :param uuid: The uuid of this Order.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501


        :return: The status of this Order.  # noqa: E501
        :rtype: OrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.


        :param status: The status of this Order.  # noqa: E501
        :type: OrderStatus
        """

        self._status = status

    @property
    def order_number(self):
        """Gets the order_number of this Order.  # noqa: E501

        Customer-provided order number  # noqa: E501

        :return: The order_number of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this Order.

        Customer-provided order number  # noqa: E501

        :param order_number: The order_number of this Order.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and order_number is None:  # noqa: E501
            raise ValueError("Invalid value for `order_number`, must not be `None`")  # noqa: E501

        self._order_number = order_number

    @property
    def printed_parts(self):
        """Gets the printed_parts of this Order.  # noqa: E501

        Parts already printed or to be printed  # noqa: E501

        :return: The printed_parts of this Order.  # noqa: E501
        :rtype: list[PrintedPartRef]
        """
        return self._printed_parts

    @printed_parts.setter
    def printed_parts(self, printed_parts):
        """Sets the printed_parts of this Order.

        Parts already printed or to be printed  # noqa: E501

        :param printed_parts: The printed_parts of this Order.  # noqa: E501
        :type: list[PrintedPartRef]
        """
        if self.local_vars_configuration.client_side_validation and printed_parts is None:  # noqa: E501
            raise ValueError("Invalid value for `printed_parts`, must not be `None`")  # noqa: E501

        self._printed_parts = printed_parts

    @property
    def due_date(self):
        """Gets the due_date of this Order.  # noqa: E501

        Print due date, used to prioritize orders for packing and printing  # noqa: E501

        :return: The due_date of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Order.

        Print due date, used to prioritize orders for packing and printing  # noqa: E501

        :param due_date: The due_date of this Order.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and due_date is None:  # noqa: E501
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def route_to(self):
        """Gets the route_to of this Order.  # noqa: E501

        Section to route this order to (e.g. a rework line)  # noqa: E501

        :return: The route_to of this Order.  # noqa: E501
        :rtype: list[str]
        """
        return self._route_to

    @route_to.setter
    def route_to(self, route_to):
        """Sets the route_to of this Order.

        Section to route this order to (e.g. a rework line)  # noqa: E501

        :param route_to: The route_to of this Order.  # noqa: E501
        :type: list[str]
        """

        self._route_to = route_to

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()
