# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import

import dataproperty
import six

from ._error import NetworkInterfaceNotFoundError


def verify_network_interface(device):
    try:
        import netifaces
    except ImportError:
        return

    if device not in netifaces.interfaces():
        raise NetworkInterfaceNotFoundError(
            "network interface not found: " + device)


def sanitize_network(network):
    """
    :return: Network string
    :rtype: str
    :raises ValueError: if the network string is invalid.
    """

    import ipaddress

    if dataproperty.is_empty_string(network):
        return ""

    if network.lower() == "anywhere":
        return "0.0.0.0/0"

    try:
        ipaddress.IPv4Address(six.u(network))
        return network + "/32"
    except ipaddress.AddressValueError:
        pass

    ipaddress.IPv4Network(six.u(network))  # validate network str

    return network
