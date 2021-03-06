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

class JumioKycIdentityVerificationRequestModel(object):
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
        'error_url': 'str',
        'success_url': 'str',
        'is_provider_flow_driven_by_client': 'bool'
    }

    attribute_map = {
        'error_url': 'errorUrl',
        'success_url': 'successUrl',
        'is_provider_flow_driven_by_client': 'isProviderFlowDrivenByClient'
    }

    def __init__(self, error_url=None, success_url=None, is_provider_flow_driven_by_client=None):  # noqa: E501
        """JumioKycIdentityVerificationRequestModel - a model defined in Swagger"""  # noqa: E501
        self._error_url = None
        self._success_url = None
        self._is_provider_flow_driven_by_client = None
        self.discriminator = None
        if error_url is not None:
            self.error_url = error_url
        if success_url is not None:
            self.success_url = success_url
        if is_provider_flow_driven_by_client is not None:
            self.is_provider_flow_driven_by_client = is_provider_flow_driven_by_client

    @property
    def error_url(self):
        """Gets the error_url of this JumioKycIdentityVerificationRequestModel.  # noqa: E501


        :return: The error_url of this JumioKycIdentityVerificationRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._error_url

    @error_url.setter
    def error_url(self, error_url):
        """Sets the error_url of this JumioKycIdentityVerificationRequestModel.


        :param error_url: The error_url of this JumioKycIdentityVerificationRequestModel.  # noqa: E501
        :type: str
        """

        self._error_url = error_url

    @property
    def success_url(self):
        """Gets the success_url of this JumioKycIdentityVerificationRequestModel.  # noqa: E501


        :return: The success_url of this JumioKycIdentityVerificationRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """Sets the success_url of this JumioKycIdentityVerificationRequestModel.


        :param success_url: The success_url of this JumioKycIdentityVerificationRequestModel.  # noqa: E501
        :type: str
        """

        self._success_url = success_url

    @property
    def is_provider_flow_driven_by_client(self):
        """Gets the is_provider_flow_driven_by_client of this JumioKycIdentityVerificationRequestModel.  # noqa: E501


        :return: The is_provider_flow_driven_by_client of this JumioKycIdentityVerificationRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_provider_flow_driven_by_client

    @is_provider_flow_driven_by_client.setter
    def is_provider_flow_driven_by_client(self, is_provider_flow_driven_by_client):
        """Sets the is_provider_flow_driven_by_client of this JumioKycIdentityVerificationRequestModel.


        :param is_provider_flow_driven_by_client: The is_provider_flow_driven_by_client of this JumioKycIdentityVerificationRequestModel.  # noqa: E501
        :type: bool
        """

        self._is_provider_flow_driven_by_client = is_provider_flow_driven_by_client

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
        if issubclass(JumioKycIdentityVerificationRequestModel, dict):
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
        if not isinstance(other, JumioKycIdentityVerificationRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
