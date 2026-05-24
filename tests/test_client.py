# SPDX-FileCopyrightText: 2015, 2016 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""Test client."""

import socket
import ssl

import pytest
import responses
from helpers import APIURL, get_client
from mock import patch
from requests import ConnectionError

from datacite import DataCiteMDSClient
from datacite.errors import HttpError as DataCiteHttpError


def test_api_url():
    """Test client init."""
    c = DataCiteMDSClient(
        username="TEST",
        password="",
        prefix="10.1234",
        test_mode=False,
        url="https://mds.example.org",  # without slash
    )
    assert c.api_url == "https://mds.example.org/"  # with slash
    assert c.prefix == "10.1234"
    assert c.__repr__() == "<DataCiteMDSClient: TEST>"


@patch("datacite.request.requests")
def test_connection_error(requests):
    """Test connection error."""
    requests.get.side_effect = ConnectionError()

    c = get_client()
    with pytest.raises(DataCiteHttpError):
        c.doi_get("10.1234/foo.bar")


@patch("datacite.request.requests")
def test_ssl_error(requests):
    """Test HTTP error."""
    requests.get.side_effect = ssl.SSLError("The read operation timed out.")

    c = get_client()
    with pytest.raises(DataCiteHttpError):
        c.doi_get("10.1234/foo.bar")


# Haven't gotten timeout to work correctly with responses
# Commenting out until someone can fix
# @responses.activate
# def test_timeout():
#    """Test timeouts."""
#    def callback(request):
#        raise socket.timeout("timeout")
#
#    responses.add_callback(
#        responses.GET,
#        "{0}doi/10.1234/1".format(APIURL),
#        callback=callback,
#    )
#
#    d = get_client(timeout=0.1)
#    with pytest.raises(DataCiteHttpError):
#        d.doi_get("10.1234/1")
