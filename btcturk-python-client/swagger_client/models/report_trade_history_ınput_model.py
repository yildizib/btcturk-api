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

class ReportTradeHistoryInputModel(object):
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
        'pairs': 'list[int]',
        'order_types': 'list[int]',
        'begin_date': 'datetime',
        'end_date': 'datetime',
        'document_file_type': 'DocumentFileType'
    }

    attribute_map = {
        'pairs': 'pairs',
        'order_types': 'orderTypes',
        'begin_date': 'beginDate',
        'end_date': 'endDate',
        'document_file_type': 'documentFileType'
    }

    def __init__(self, pairs=None, order_types=None, begin_date=None, end_date=None, document_file_type=None):  # noqa: E501
        """ReportTradeHistoryInputModel - a model defined in Swagger"""  # noqa: E501
        self._pairs = None
        self._order_types = None
        self._begin_date = None
        self._end_date = None
        self._document_file_type = None
        self.discriminator = None
        if pairs is not None:
            self.pairs = pairs
        if order_types is not None:
            self.order_types = order_types
        if begin_date is not None:
            self.begin_date = begin_date
        if end_date is not None:
            self.end_date = end_date
        if document_file_type is not None:
            self.document_file_type = document_file_type

    @property
    def pairs(self):
        """Gets the pairs of this ReportTradeHistoryInputModel.  # noqa: E501


        :return: The pairs of this ReportTradeHistoryInputModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._pairs

    @pairs.setter
    def pairs(self, pairs):
        """Sets the pairs of this ReportTradeHistoryInputModel.


        :param pairs: The pairs of this ReportTradeHistoryInputModel.  # noqa: E501
        :type: list[int]
        """

        self._pairs = pairs

    @property
    def order_types(self):
        """Gets the order_types of this ReportTradeHistoryInputModel.  # noqa: E501


        :return: The order_types of this ReportTradeHistoryInputModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._order_types

    @order_types.setter
    def order_types(self, order_types):
        """Sets the order_types of this ReportTradeHistoryInputModel.


        :param order_types: The order_types of this ReportTradeHistoryInputModel.  # noqa: E501
        :type: list[int]
        """

        self._order_types = order_types

    @property
    def begin_date(self):
        """Gets the begin_date of this ReportTradeHistoryInputModel.  # noqa: E501


        :return: The begin_date of this ReportTradeHistoryInputModel.  # noqa: E501
        :rtype: datetime
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this ReportTradeHistoryInputModel.


        :param begin_date: The begin_date of this ReportTradeHistoryInputModel.  # noqa: E501
        :type: datetime
        """

        self._begin_date = begin_date

    @property
    def end_date(self):
        """Gets the end_date of this ReportTradeHistoryInputModel.  # noqa: E501


        :return: The end_date of this ReportTradeHistoryInputModel.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ReportTradeHistoryInputModel.


        :param end_date: The end_date of this ReportTradeHistoryInputModel.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def document_file_type(self):
        """Gets the document_file_type of this ReportTradeHistoryInputModel.  # noqa: E501


        :return: The document_file_type of this ReportTradeHistoryInputModel.  # noqa: E501
        :rtype: DocumentFileType
        """
        return self._document_file_type

    @document_file_type.setter
    def document_file_type(self, document_file_type):
        """Sets the document_file_type of this ReportTradeHistoryInputModel.


        :param document_file_type: The document_file_type of this ReportTradeHistoryInputModel.  # noqa: E501
        :type: DocumentFileType
        """

        self._document_file_type = document_file_type

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
        if issubclass(ReportTradeHistoryInputModel, dict):
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
        if not isinstance(other, ReportTradeHistoryInputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
