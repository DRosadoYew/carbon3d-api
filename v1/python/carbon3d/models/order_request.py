# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.0.8
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class OrderRequest(object):
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
        'order_number': 'str',
        'parts': 'list[OrderRequestParts]',
        'due_date': 'datetime',
        'route_to': 'list[str]',
        'flush': 'bool'
    }

    attribute_map = {
        'order_number': 'order_number',
        'parts': 'parts',
        'due_date': 'due_date',
        'route_to': 'route_to',
        'flush': 'flush'
    }

    def __init__(self, order_number=None, parts=None, due_date=None, route_to=None, flush=None, local_vars_configuration=None):  # noqa: E501
        """OrderRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._order_number = None
        self._parts = None
        self._due_date = None
        self._route_to = None
        self._flush = None
        self.discriminator = None

        self.order_number = order_number
        self.parts = parts
        self.due_date = due_date
        if route_to is not None:
            self.route_to = route_to
        if flush is not None:
            self.flush = flush

    @property
    def order_number(self):
        """Gets the order_number of this OrderRequest.  # noqa: E501

        Customer-provided order number  # noqa: E501

        :return: The order_number of this OrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this OrderRequest.

        Customer-provided order number  # noqa: E501

        :param order_number: The order_number of this OrderRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and order_number is None:  # noqa: E501
            raise ValueError("Invalid value for `order_number`, must not be `None`")  # noqa: E501

        self._order_number = order_number

    @property
    def parts(self):
        """Gets the parts of this OrderRequest.  # noqa: E501

        Parts to be printed  # noqa: E501

        :return: The parts of this OrderRequest.  # noqa: E501
        :rtype: list[OrderRequestParts]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this OrderRequest.

        Parts to be printed  # noqa: E501

        :param parts: The parts of this OrderRequest.  # noqa: E501
        :type: list[OrderRequestParts]
        """
        if self.local_vars_configuration.client_side_validation and parts is None:  # noqa: E501
            raise ValueError("Invalid value for `parts`, must not be `None`")  # noqa: E501

        self._parts = parts

    @property
    def due_date(self):
        """Gets the due_date of this OrderRequest.  # noqa: E501

        Print due date, used to prioritize orders for packing and printing  # noqa: E501

        :return: The due_date of this OrderRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this OrderRequest.

        Print due date, used to prioritize orders for packing and printing  # noqa: E501

        :param due_date: The due_date of this OrderRequest.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and due_date is None:  # noqa: E501
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def route_to(self):
        """Gets the route_to of this OrderRequest.  # noqa: E501

        Section(s) to route this order to (e.g. a rework line)  # noqa: E501

        :return: The route_to of this OrderRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._route_to

    @route_to.setter
    def route_to(self, route_to):
        """Sets the route_to of this OrderRequest.

        Section(s) to route this order to (e.g. a rework line)  # noqa: E501

        :param route_to: The route_to of this OrderRequest.  # noqa: E501
        :type: list[str]
        """

        self._route_to = route_to

    @property
    def flush(self):
        """Gets the flush of this OrderRequest.  # noqa: E501

        Push parts in an order through the auto-packer.  # noqa: E501

        :return: The flush of this OrderRequest.  # noqa: E501
        :rtype: bool
        """
        return self._flush

    @flush.setter
    def flush(self, flush):
        """Sets the flush of this OrderRequest.

        Push parts in an order through the auto-packer.  # noqa: E501

        :param flush: The flush of this OrderRequest.  # noqa: E501
        :type: bool
        """

        self._flush = flush

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
        if not isinstance(other, OrderRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderRequest):
            return True

        return self.to_dict() != other.to_dict()
