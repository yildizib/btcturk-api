# coding: utf-8

"""
    BtcTurk API 3.0

    White label exchange API documentation.  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: development@btctrader.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="BtcTurk API 3.0",
    author_email="development@btctrader.com",
    url="",
    keywords=["Swagger", "BtcTurk API 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    White label exchange API documentation.  # noqa: E501
    """
)
