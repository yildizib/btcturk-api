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

class BugBountyNoticeRequestModel(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'phone': 'str',
        'user_email': 'str',
        'diagnosis': 'str',
        'host': 'str',
        'path': 'str',
        'description': 'str',
        'h_captcha_response': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'phone': 'phone',
        'user_email': 'userEmail',
        'diagnosis': 'diagnosis',
        'host': 'host',
        'path': 'path',
        'description': 'description',
        'h_captcha_response': 'hCaptchaResponse'
    }

    def __init__(self, first_name=None, last_name=None, email=None, phone=None, user_email=None, diagnosis=None, host=None, path=None, description=None, h_captcha_response=None):  # noqa: E501
        """BugBountyNoticeRequestModel - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._last_name = None
        self._email = None
        self._phone = None
        self._user_email = None
        self._diagnosis = None
        self._host = None
        self._path = None
        self._description = None
        self._h_captcha_response = None
        self.discriminator = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if phone is not None:
            self.phone = phone
        if user_email is not None:
            self.user_email = user_email
        self.diagnosis = diagnosis
        if host is not None:
            self.host = host
        if path is not None:
            self.path = path
        self.description = description
        if h_captcha_response is not None:
            self.h_captcha_response = h_captcha_response

    @property
    def first_name(self):
        """Gets the first_name of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The first_name of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BugBountyNoticeRequestModel.


        :param first_name: The first_name of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The last_name of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BugBountyNoticeRequestModel.


        :param last_name: The last_name of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The email of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BugBountyNoticeRequestModel.


        :param email: The email of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The phone of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this BugBountyNoticeRequestModel.


        :param phone: The phone of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def user_email(self):
        """Gets the user_email of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The user_email of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this BugBountyNoticeRequestModel.


        :param user_email: The user_email of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """

        self._user_email = user_email

    @property
    def diagnosis(self):
        """Gets the diagnosis of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The diagnosis of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        """Sets the diagnosis of this BugBountyNoticeRequestModel.


        :param diagnosis: The diagnosis of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """
        if diagnosis is None:
            raise ValueError("Invalid value for `diagnosis`, must not be `None`")  # noqa: E501

        self._diagnosis = diagnosis

    @property
    def host(self):
        """Gets the host of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The host of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this BugBountyNoticeRequestModel.


        :param host: The host of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def path(self):
        """Gets the path of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The path of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BugBountyNoticeRequestModel.


        :param path: The path of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def description(self):
        """Gets the description of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The description of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BugBountyNoticeRequestModel.


        :param description: The description of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def h_captcha_response(self):
        """Gets the h_captcha_response of this BugBountyNoticeRequestModel.  # noqa: E501


        :return: The h_captcha_response of this BugBountyNoticeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._h_captcha_response

    @h_captcha_response.setter
    def h_captcha_response(self, h_captcha_response):
        """Sets the h_captcha_response of this BugBountyNoticeRequestModel.


        :param h_captcha_response: The h_captcha_response of this BugBountyNoticeRequestModel.  # noqa: E501
        :type: str
        """

        self._h_captcha_response = h_captcha_response

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
        if issubclass(BugBountyNoticeRequestModel, dict):
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
        if not isinstance(other, BugBountyNoticeRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
