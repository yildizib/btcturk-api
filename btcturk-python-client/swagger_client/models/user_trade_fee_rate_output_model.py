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

class UserTradeFeeRateOutputModel(object):
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
        'pair_ıd': 'int',
        'pair_symbol': 'str',
        'order_method': 'OrderMethod',
        'maker_fee_percentage': 'float',
        'taker_fee_percentage': 'float',
        'tax_percentage': 'float',
        'has_active_coupon': 'bool'
    }

    attribute_map = {
        'pair_ıd': 'pairId',
        'pair_symbol': 'pairSymbol',
        'order_method': 'orderMethod',
        'maker_fee_percentage': 'makerFeePercentage',
        'taker_fee_percentage': 'takerFeePercentage',
        'tax_percentage': 'taxPercentage',
        'has_active_coupon': 'hasActiveCoupon'
    }

    def __init__(self, pair_ıd=None, pair_symbol=None, order_method=None, maker_fee_percentage=None, taker_fee_percentage=None, tax_percentage=None, has_active_coupon=None):  # noqa: E501
        """UserTradeFeeRateOutputModel - a model defined in Swagger"""  # noqa: E501
        self._pair_ıd = None
        self._pair_symbol = None
        self._order_method = None
        self._maker_fee_percentage = None
        self._taker_fee_percentage = None
        self._tax_percentage = None
        self._has_active_coupon = None
        self.discriminator = None
        if pair_ıd is not None:
            self.pair_ıd = pair_ıd
        if pair_symbol is not None:
            self.pair_symbol = pair_symbol
        if order_method is not None:
            self.order_method = order_method
        if maker_fee_percentage is not None:
            self.maker_fee_percentage = maker_fee_percentage
        if taker_fee_percentage is not None:
            self.taker_fee_percentage = taker_fee_percentage
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if has_active_coupon is not None:
            self.has_active_coupon = has_active_coupon

    @property
    def pair_ıd(self):
        """Gets the pair_ıd of this UserTradeFeeRateOutputModel.  # noqa: E501


        :return: The pair_ıd of this UserTradeFeeRateOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._pair_ıd

    @pair_ıd.setter
    def pair_ıd(self, pair_ıd):
        """Sets the pair_ıd of this UserTradeFeeRateOutputModel.


        :param pair_ıd: The pair_ıd of this UserTradeFeeRateOutputModel.  # noqa: E501
        :type: int
        """

        self._pair_ıd = pair_ıd

    @property
    def pair_symbol(self):
        """Gets the pair_symbol of this UserTradeFeeRateOutputModel.  # noqa: E501


        :return: The pair_symbol of this UserTradeFeeRateOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._pair_symbol

    @pair_symbol.setter
    def pair_symbol(self, pair_symbol):
        """Sets the pair_symbol of this UserTradeFeeRateOutputModel.


        :param pair_symbol: The pair_symbol of this UserTradeFeeRateOutputModel.  # noqa: E501
        :type: str
        """

        self._pair_symbol = pair_symbol

    @property
    def order_method(self):
        """Gets the order_method of this UserTradeFeeRateOutputModel.  # noqa: E501


        :return: The order_method of this UserTradeFeeRateOutputModel.  # noqa: E501
        :rtype: OrderMethod
        """
        return self._order_method

    @order_method.setter
    def order_method(self, order_method):
        """Sets the order_method of this UserTradeFeeRateOutputModel.


        :param order_method: The order_method of this UserTradeFeeRateOutputModel.  # noqa: E501
        :type: OrderMethod
        """

        self._order_method = order_method

    @property
    def maker_fee_percentage(self):
        """Gets the maker_fee_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501


        :return: The maker_fee_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501
        :rtype: float
        """
        return self._maker_fee_percentage

    @maker_fee_percentage.setter
    def maker_fee_percentage(self, maker_fee_percentage):
        """Sets the maker_fee_percentage of this UserTradeFeeRateOutputModel.


        :param maker_fee_percentage: The maker_fee_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501
        :type: float
        """

        self._maker_fee_percentage = maker_fee_percentage

    @property
    def taker_fee_percentage(self):
        """Gets the taker_fee_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501


        :return: The taker_fee_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501
        :rtype: float
        """
        return self._taker_fee_percentage

    @taker_fee_percentage.setter
    def taker_fee_percentage(self, taker_fee_percentage):
        """Sets the taker_fee_percentage of this UserTradeFeeRateOutputModel.


        :param taker_fee_percentage: The taker_fee_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501
        :type: float
        """

        self._taker_fee_percentage = taker_fee_percentage

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501


        :return: The tax_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501
        :rtype: float
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this UserTradeFeeRateOutputModel.


        :param tax_percentage: The tax_percentage of this UserTradeFeeRateOutputModel.  # noqa: E501
        :type: float
        """

        self._tax_percentage = tax_percentage

    @property
    def has_active_coupon(self):
        """Gets the has_active_coupon of this UserTradeFeeRateOutputModel.  # noqa: E501


        :return: The has_active_coupon of this UserTradeFeeRateOutputModel.  # noqa: E501
        :rtype: bool
        """
        return self._has_active_coupon

    @has_active_coupon.setter
    def has_active_coupon(self, has_active_coupon):
        """Sets the has_active_coupon of this UserTradeFeeRateOutputModel.


        :param has_active_coupon: The has_active_coupon of this UserTradeFeeRateOutputModel.  # noqa: E501
        :type: bool
        """

        self._has_active_coupon = has_active_coupon

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
        if issubclass(UserTradeFeeRateOutputModel, dict):
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
        if not isinstance(other, UserTradeFeeRateOutputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
