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

class AkbankDirektCommissionOutputModel(object):
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
        'deposit_fee': 'float',
        'deposit_max_fee': 'int',
        'deposit_tax': 'float',
        'deposit_min_amount': 'float'
    }

    attribute_map = {
        'deposit_fee': 'depositFee',
        'deposit_max_fee': 'depositMaxFee',
        'deposit_tax': 'depositTax',
        'deposit_min_amount': 'depositMinAmount'
    }

    def __init__(self, deposit_fee=None, deposit_max_fee=None, deposit_tax=None, deposit_min_amount=None):  # noqa: E501
        """AkbankDirektCommissionOutputModel - a model defined in Swagger"""  # noqa: E501
        self._deposit_fee = None
        self._deposit_max_fee = None
        self._deposit_tax = None
        self._deposit_min_amount = None
        self.discriminator = None
        if deposit_fee is not None:
            self.deposit_fee = deposit_fee
        if deposit_max_fee is not None:
            self.deposit_max_fee = deposit_max_fee
        if deposit_tax is not None:
            self.deposit_tax = deposit_tax
        if deposit_min_amount is not None:
            self.deposit_min_amount = deposit_min_amount

    @property
    def deposit_fee(self):
        """Gets the deposit_fee of this AkbankDirektCommissionOutputModel.  # noqa: E501


        :return: The deposit_fee of this AkbankDirektCommissionOutputModel.  # noqa: E501
        :rtype: float
        """
        return self._deposit_fee

    @deposit_fee.setter
    def deposit_fee(self, deposit_fee):
        """Sets the deposit_fee of this AkbankDirektCommissionOutputModel.


        :param deposit_fee: The deposit_fee of this AkbankDirektCommissionOutputModel.  # noqa: E501
        :type: float
        """

        self._deposit_fee = deposit_fee

    @property
    def deposit_max_fee(self):
        """Gets the deposit_max_fee of this AkbankDirektCommissionOutputModel.  # noqa: E501


        :return: The deposit_max_fee of this AkbankDirektCommissionOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._deposit_max_fee

    @deposit_max_fee.setter
    def deposit_max_fee(self, deposit_max_fee):
        """Sets the deposit_max_fee of this AkbankDirektCommissionOutputModel.


        :param deposit_max_fee: The deposit_max_fee of this AkbankDirektCommissionOutputModel.  # noqa: E501
        :type: int
        """

        self._deposit_max_fee = deposit_max_fee

    @property
    def deposit_tax(self):
        """Gets the deposit_tax of this AkbankDirektCommissionOutputModel.  # noqa: E501


        :return: The deposit_tax of this AkbankDirektCommissionOutputModel.  # noqa: E501
        :rtype: float
        """
        return self._deposit_tax

    @deposit_tax.setter
    def deposit_tax(self, deposit_tax):
        """Sets the deposit_tax of this AkbankDirektCommissionOutputModel.


        :param deposit_tax: The deposit_tax of this AkbankDirektCommissionOutputModel.  # noqa: E501
        :type: float
        """

        self._deposit_tax = deposit_tax

    @property
    def deposit_min_amount(self):
        """Gets the deposit_min_amount of this AkbankDirektCommissionOutputModel.  # noqa: E501


        :return: The deposit_min_amount of this AkbankDirektCommissionOutputModel.  # noqa: E501
        :rtype: float
        """
        return self._deposit_min_amount

    @deposit_min_amount.setter
    def deposit_min_amount(self, deposit_min_amount):
        """Sets the deposit_min_amount of this AkbankDirektCommissionOutputModel.


        :param deposit_min_amount: The deposit_min_amount of this AkbankDirektCommissionOutputModel.  # noqa: E501
        :type: float
        """

        self._deposit_min_amount = deposit_min_amount

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
        if issubclass(AkbankDirektCommissionOutputModel, dict):
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
        if not isinstance(other, AkbankDirektCommissionOutputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
