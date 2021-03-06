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

class SystemNotificationContentModel(object):
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
        'id': 'int',
        'subtitle': 'str',
        'activity': 'str',
        'code': 'str',
        'created_date': 'int',
        'pin': 'bool',
        'content': 'str',
        'read': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'subtitle': 'subtitle',
        'activity': 'activity',
        'code': 'code',
        'created_date': 'createdDate',
        'pin': 'pin',
        'content': 'content',
        'read': 'read'
    }

    def __init__(self, id=None, subtitle=None, activity=None, code=None, created_date=None, pin=None, content=None, read=None):  # noqa: E501
        """SystemNotificationContentModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._subtitle = None
        self._activity = None
        self._code = None
        self._created_date = None
        self._pin = None
        self._content = None
        self._read = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if subtitle is not None:
            self.subtitle = subtitle
        if activity is not None:
            self.activity = activity
        if code is not None:
            self.code = code
        if created_date is not None:
            self.created_date = created_date
        if pin is not None:
            self.pin = pin
        if content is not None:
            self.content = content
        if read is not None:
            self.read = read

    @property
    def id(self):
        """Gets the id of this SystemNotificationContentModel.  # noqa: E501


        :return: The id of this SystemNotificationContentModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SystemNotificationContentModel.


        :param id: The id of this SystemNotificationContentModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def subtitle(self):
        """Gets the subtitle of this SystemNotificationContentModel.  # noqa: E501


        :return: The subtitle of this SystemNotificationContentModel.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this SystemNotificationContentModel.


        :param subtitle: The subtitle of this SystemNotificationContentModel.  # noqa: E501
        :type: str
        """

        self._subtitle = subtitle

    @property
    def activity(self):
        """Gets the activity of this SystemNotificationContentModel.  # noqa: E501


        :return: The activity of this SystemNotificationContentModel.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this SystemNotificationContentModel.


        :param activity: The activity of this SystemNotificationContentModel.  # noqa: E501
        :type: str
        """

        self._activity = activity

    @property
    def code(self):
        """Gets the code of this SystemNotificationContentModel.  # noqa: E501


        :return: The code of this SystemNotificationContentModel.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SystemNotificationContentModel.


        :param code: The code of this SystemNotificationContentModel.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def created_date(self):
        """Gets the created_date of this SystemNotificationContentModel.  # noqa: E501


        :return: The created_date of this SystemNotificationContentModel.  # noqa: E501
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this SystemNotificationContentModel.


        :param created_date: The created_date of this SystemNotificationContentModel.  # noqa: E501
        :type: int
        """

        self._created_date = created_date

    @property
    def pin(self):
        """Gets the pin of this SystemNotificationContentModel.  # noqa: E501


        :return: The pin of this SystemNotificationContentModel.  # noqa: E501
        :rtype: bool
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this SystemNotificationContentModel.


        :param pin: The pin of this SystemNotificationContentModel.  # noqa: E501
        :type: bool
        """

        self._pin = pin

    @property
    def content(self):
        """Gets the content of this SystemNotificationContentModel.  # noqa: E501


        :return: The content of this SystemNotificationContentModel.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SystemNotificationContentModel.


        :param content: The content of this SystemNotificationContentModel.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def read(self):
        """Gets the read of this SystemNotificationContentModel.  # noqa: E501


        :return: The read of this SystemNotificationContentModel.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this SystemNotificationContentModel.


        :param read: The read of this SystemNotificationContentModel.  # noqa: E501
        :type: bool
        """

        self._read = read

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
        if issubclass(SystemNotificationContentModel, dict):
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
        if not isinstance(other, SystemNotificationContentModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
