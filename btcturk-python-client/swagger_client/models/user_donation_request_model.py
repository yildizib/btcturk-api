# coding: utf-8

"""
    BtcTurk API 3.0

    White label exchange API documentation.  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: development@btctrader.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserDonationRequestModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'amount': 'str',
        'bank_ıd': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'bank_ıd': 'bankId'
    }

    def __init__(self, amount=None, bank_ıd=None):  # noqa: E501
        """UserDonationRequestModel - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._bank_ıd = None
        self.discriminator = None
        self.amount = amount
        self.bank_ıd = bank_ıd

    @property
    def amount(self):
        """Gets the amount of this UserDonationRequestModel.  # noqa: E501


        :return: The amount of this UserDonationRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UserDonationRequestModel.


        :param amount: The amount of this UserDonationRequestModel.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def bank_ıd(self):
        """Gets the bank_ıd of this UserDonationRequestModel.  # noqa: E501


        :return: The bank_ıd of this UserDonationRequestModel.  # noqa: E501
        :rtype: int
        """
        return self._bank_ıd

    @bank_ıd.setter
    def bank_ıd(self, bank_ıd):
        """Sets the bank_ıd of this UserDonationRequestModel.


        :param bank_ıd: The bank_ıd of this UserDonationRequestModel.  # noqa: E501
        :type: int
        """
        if bank_ıd is None:
            raise ValueError("Invalid value for `bank_ıd`, must not be `None`")  # noqa: E501

        self._bank_ıd = bank_ıd

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UserDonationRequestModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserDonationRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
