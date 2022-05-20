# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Status(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, warning=None, message=None):  # noqa: E501
        """Status - a model defined in OpenAPI

        :param warning: The warning of this Status.  # noqa: E501
        :type warning: bool
        :param message: The message of this Status.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'warning': bool,
            'message': str
        }

        self.attribute_map = {
            'warning': 'warning',
            'message': 'message'
        }

        self._warning = warning
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'Status':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Status of this Status.  # noqa: E501
        :rtype: Status
        """
        return util.deserialize_model(dikt, cls)

    @property
    def warning(self):
        """Gets the warning of this Status.


        :return: The warning of this Status.
        :rtype: bool
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this Status.


        :param warning: The warning of this Status.
        :type warning: bool
        """

        self._warning = warning

    @property
    def message(self):
        """Gets the message of this Status.


        :return: The message of this Status.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Status.


        :param message: The message of this Status.
        :type message: str
        """

        self._message = message
