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

class FiatDepositBankAccountModel(object):
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
        'slug': 'str',
        'code': 'str',
        'name': 'str',
        'status_transfer': 'bool',
        'status_accept_eft': 'bool',
        'iban': 'str',
        'owner': 'str',
        'dark_logo': 'str',
        'light_logo': 'str',
        'currency_symbol': 'str'
    }

    attribute_map = {
        'slug': 'slug',
        'code': 'code',
        'name': 'name',
        'status_transfer': 'statusTransfer',
        'status_accept_eft': 'statusAcceptEFT',
        'iban': 'iban',
        'owner': 'owner',
        'dark_logo': 'darkLogo',
        'light_logo': 'lightLogo',
        'currency_symbol': 'currencySymbol'
    }

    def __init__(self, slug=None, code=None, name=None, status_transfer=None, status_accept_eft=None, iban=None, owner=None, dark_logo=None, light_logo=None, currency_symbol=None):  # noqa: E501
        """FiatDepositBankAccountModel - a model defined in Swagger"""  # noqa: E501
        self._slug = None
        self._code = None
        self._name = None
        self._status_transfer = None
        self._status_accept_eft = None
        self._iban = None
        self._owner = None
        self._dark_logo = None
        self._light_logo = None
        self._currency_symbol = None
        self.discriminator = None
        if slug is not None:
            self.slug = slug
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if status_transfer is not None:
            self.status_transfer = status_transfer
        if status_accept_eft is not None:
            self.status_accept_eft = status_accept_eft
        if iban is not None:
            self.iban = iban
        if owner is not None:
            self.owner = owner
        if dark_logo is not None:
            self.dark_logo = dark_logo
        if light_logo is not None:
            self.light_logo = light_logo
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol

    @property
    def slug(self):
        """Gets the slug of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The slug of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this FiatDepositBankAccountModel.


        :param slug: The slug of this FiatDepositBankAccountModel.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def code(self):
        """Gets the code of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The code of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FiatDepositBankAccountModel.


        :param code: The code of this FiatDepositBankAccountModel.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The name of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FiatDepositBankAccountModel.


        :param name: The name of this FiatDepositBankAccountModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status_transfer(self):
        """Gets the status_transfer of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The status_transfer of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: bool
        """
        return self._status_transfer

    @status_transfer.setter
    def status_transfer(self, status_transfer):
        """Sets the status_transfer of this FiatDepositBankAccountModel.


        :param status_transfer: The status_transfer of this FiatDepositBankAccountModel.  # noqa: E501
        :type: bool
        """

        self._status_transfer = status_transfer

    @property
    def status_accept_eft(self):
        """Gets the status_accept_eft of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The status_accept_eft of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: bool
        """
        return self._status_accept_eft

    @status_accept_eft.setter
    def status_accept_eft(self, status_accept_eft):
        """Sets the status_accept_eft of this FiatDepositBankAccountModel.


        :param status_accept_eft: The status_accept_eft of this FiatDepositBankAccountModel.  # noqa: E501
        :type: bool
        """

        self._status_accept_eft = status_accept_eft

    @property
    def iban(self):
        """Gets the iban of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The iban of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this FiatDepositBankAccountModel.


        :param iban: The iban of this FiatDepositBankAccountModel.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def owner(self):
        """Gets the owner of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The owner of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this FiatDepositBankAccountModel.


        :param owner: The owner of this FiatDepositBankAccountModel.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def dark_logo(self):
        """Gets the dark_logo of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The dark_logo of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: str
        """
        return self._dark_logo

    @dark_logo.setter
    def dark_logo(self, dark_logo):
        """Sets the dark_logo of this FiatDepositBankAccountModel.


        :param dark_logo: The dark_logo of this FiatDepositBankAccountModel.  # noqa: E501
        :type: str
        """

        self._dark_logo = dark_logo

    @property
    def light_logo(self):
        """Gets the light_logo of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The light_logo of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: str
        """
        return self._light_logo

    @light_logo.setter
    def light_logo(self, light_logo):
        """Sets the light_logo of this FiatDepositBankAccountModel.


        :param light_logo: The light_logo of this FiatDepositBankAccountModel.  # noqa: E501
        :type: str
        """

        self._light_logo = light_logo

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this FiatDepositBankAccountModel.  # noqa: E501


        :return: The currency_symbol of this FiatDepositBankAccountModel.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this FiatDepositBankAccountModel.


        :param currency_symbol: The currency_symbol of this FiatDepositBankAccountModel.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

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
        if issubclass(FiatDepositBankAccountModel, dict):
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
        if not isinstance(other, FiatDepositBankAccountModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
