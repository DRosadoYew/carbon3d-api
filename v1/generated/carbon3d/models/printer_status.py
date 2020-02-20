# coding: utf-8

"""
    Carbon API (Draft)

    An API to interact with Carbon's Manufacturing Cloud including 3D model upload, automated order processing and part history.  Getting started ---------------  - [Generate and download an API key](https://carbon3d.print.carbon3d.com/api_keys)   - Your API key and client secret will be downloaded into a secret.json file.  - [Use generated API key to generate a JWT token](/token_generator) from the api key.   - If your API key is revoked, this token will no longer work.  - Authorize with generated token  - Upload mesh files  - Create orders  - Monitor order status   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from carbon3d.configuration import Configuration


class PrinterStatus(object):
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
        'alerts': 'list[str]',
        'printer_state': 'str',
        'software_version': 'str'
    }

    attribute_map = {
        'alerts': 'alerts',
        'printer_state': 'printer_state',
        'software_version': 'software_version'
    }

    def __init__(self, alerts=None, printer_state=None, software_version=None, local_vars_configuration=None):  # noqa: E501
        """PrinterStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alerts = None
        self._printer_state = None
        self._software_version = None
        self.discriminator = None

        if alerts is not None:
            self.alerts = alerts
        self.printer_state = printer_state
        self.software_version = software_version

    @property
    def alerts(self):
        """Gets the alerts of this PrinterStatus.  # noqa: E501


        :return: The alerts of this PrinterStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this PrinterStatus.


        :param alerts: The alerts of this PrinterStatus.  # noqa: E501
        :type: list[str]
        """

        self._alerts = alerts

    @property
    def printer_state(self):
        """Gets the printer_state of this PrinterStatus.  # noqa: E501


        :return: The printer_state of this PrinterStatus.  # noqa: E501
        :rtype: str
        """
        return self._printer_state

    @printer_state.setter
    def printer_state(self, printer_state):
        """Sets the printer_state of this PrinterStatus.


        :param printer_state: The printer_state of this PrinterStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and printer_state is None:  # noqa: E501
            raise ValueError("Invalid value for `printer_state`, must not be `None`")  # noqa: E501

        self._printer_state = printer_state

    @property
    def software_version(self):
        """Gets the software_version of this PrinterStatus.  # noqa: E501


        :return: The software_version of this PrinterStatus.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this PrinterStatus.


        :param software_version: The software_version of this PrinterStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and software_version is None:  # noqa: E501
            raise ValueError("Invalid value for `software_version`, must not be `None`")  # noqa: E501

        self._software_version = software_version

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
        if not isinstance(other, PrinterStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrinterStatus):
            return True

        return self.to_dict() != other.to_dict()
