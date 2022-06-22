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

class CheckCurrencyRiskAgreementResponseModel(object):
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
        'required': 'str',
        'approved': 'bool'
    }

    attribute_map = {
        'slug': 'slug',
        'required': 'required',
        'approved': 'approved'
    }

    def __init__(self, slug=None, required=None, approved=None):  # noqa: E501
        """CheckCurrencyRiskAgreementResponseModel - a model defined in Swagger"""  # noqa: E501
        self._slug = None
        self._required = None
        self._approved = None
        self.discriminator = None
        if slug is not None:
            self.slug = slug
        if required is not None:
            self.required = required
        if approved is not None:
            self.approved = approved

    @property
    def slug(self):
        """Gets the slug of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501


        :return: The slug of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this CheckCurrencyRiskAgreementResponseModel.


        :param slug: The slug of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def required(self):
        """Gets the required of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501


        :return: The required of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this CheckCurrencyRiskAgreementResponseModel.


        :param required: The required of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501
        :type: str
        """

        self._required = required

    @property
    def approved(self):
        """Gets the approved of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501


        :return: The approved of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this CheckCurrencyRiskAgreementResponseModel.


        :param approved: The approved of this CheckCurrencyRiskAgreementResponseModel.  # noqa: E501
        :type: bool
        """

        self._approved = approved

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
        if issubclass(CheckCurrencyRiskAgreementResponseModel, dict):
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
        if not isinstance(other, CheckCurrencyRiskAgreementResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other