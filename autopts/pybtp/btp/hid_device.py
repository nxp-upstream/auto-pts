#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright 2026, NXP.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#

"""Wrapper around btp messages. The functions are added as needed."""

import logging
import struct

from autopts.pybtp import defs
from autopts.pybtp.btp.btp import CONTROLLER_INDEX, btp_hdr_check, pts_addr_get, pts_addr_type_get
from autopts.pybtp.btp.btp import get_iut_method as get_iut
from autopts.pybtp.btp.gap import gap_wait_for_connection
from autopts.pybtp.types import addr_str_to_le_bytes, le_bytes_to_hex_str

HID_DEVICE = {
    "read_supp_cmds": (defs.BTP_SERVICE_ID_HID_DEVICE,
                       defs.BTP_HID_DEVICE_CMD_READ_SUPPORTED_COMMANDS,
                       defs.BTP_INDEX_NONE, ""),
    "connect": (defs.BTP_SERVICE_ID_HID_DEVICE,
                defs.BTP_HID_DEVICE_CMD_CONNECT,
                CONTROLLER_INDEX),
    "disconnect": (defs.BTP_SERVICE_ID_HID_DEVICE,
                   defs.BTP_HID_DEVICE_CMD_DISCONNECT,
                   CONTROLLER_INDEX),
    "send_report": (defs.BTP_SERVICE_ID_HID_DEVICE,
                    defs.BTP_HID_DEVICE_CMD_SEND_REPORT,
                    CONTROLLER_INDEX),
    "virtual_cable_unplug": (defs.BTP_SERVICE_ID_HID_DEVICE,
                             defs.BTP_HID_DEVICE_CMD_VIRTUAL_CABLE_UNPLUG,
                             CONTROLLER_INDEX),
    "enter_sniff_mode": (defs.BTP_SERVICE_ID_HID_DEVICE,
                         defs.BTP_HID_DEVICE_CMD_ENTER_SNIFF_MODE,
                         CONTROLLER_INDEX),
}


def hid_device_command_rsp_succ(op=None):
    logging.debug("%s", hid_device_command_rsp_succ.__name__)

    iutctl = get_iut()

    tuple_hdr, tuple_data = iutctl.btp_socket.read()
    logging.debug("received %r %r", tuple_hdr, tuple_data)

    btp_hdr_check(tuple_hdr, defs.BTP_SERVICE_ID_HID_DEVICE, op)


def hid_device_connect(bd_addr_type=None, bd_addr=None):
    """
    Establish a HID Device connection to the remote device.
    """
    logging.debug("%s %r %r", hid_device_connect.__name__, bd_addr_type, bd_addr)

    if bd_addr_type is None:
        bd_addr_type = pts_addr_type_get()
    if bd_addr is None:
        bd_addr = pts_addr_get()

    gap_wait_for_connection()

    data = bytearray()
    bd_addr_ba = addr_str_to_le_bytes(bd_addr)
    data.extend([bd_addr_type])
    data.extend(bd_addr_ba)

    iutctl = get_iut()
    iutctl.btp_socket.send(*HID_DEVICE['connect'], data=data)

    hid_device_command_rsp_succ(defs.BTP_HID_DEVICE_CMD_CONNECT)


def hid_device_disconnect(bd_addr_type=None, bd_addr=None):
    """
    Disconnect the HID Device connection from the remote device.
    """
    logging.debug("%s %r %r", hid_device_disconnect.__name__, bd_addr_type, bd_addr)

    if bd_addr_type is None:
        bd_addr_type = pts_addr_type_get()
    if bd_addr is None:
        bd_addr = pts_addr_get()

    data = bytearray()
    bd_addr_ba = addr_str_to_le_bytes(bd_addr)
    data.extend([bd_addr_type])
    data.extend(bd_addr_ba)

    iutctl = get_iut()
    iutctl.btp_socket.send(*HID_DEVICE['disconnect'], data=data)

    hid_device_command_rsp_succ(defs.BTP_HID_DEVICE_CMD_DISCONNECT)


def hid_device_virtual_cable_unplug(bd_addr_type=None, bd_addr=None):
    """
    Send HID Virtual Cable Unplug to the remote host on the Control channel,
    then tear down the L2CAP channels. Required IUT-initiated branch of
    HID/DEV/HCR/BV-04-C.
    """
    logging.debug("%s %r %r", hid_device_virtual_cable_unplug.__name__, bd_addr_type, bd_addr)

    if bd_addr_type is None:
        bd_addr_type = pts_addr_type_get()
    if bd_addr is None:
        bd_addr = pts_addr_get()

    data = bytearray()
    bd_addr_ba = addr_str_to_le_bytes(bd_addr)
    data.extend([bd_addr_type])
    data.extend(bd_addr_ba)

    iutctl = get_iut()
    iutctl.btp_socket.send(*HID_DEVICE['virtual_cable_unplug'], data=data)

    hid_device_command_rsp_succ(defs.BTP_HID_DEVICE_CMD_VIRTUAL_CABLE_UNPLUG)


# Default HID Interrupt channel MTU per HID spec defaults. When a report
# payload exceeds this size, the IUT is expected to fragment the report and
# may not emit a command-complete response for the SEND_REPORT command; in
# that case the host must not block waiting for it.
HID_DEVICE_DEFAULT_MTU = 48


def hid_device_send_report(report_type, report, mtu=HID_DEVICE_DEFAULT_MTU):
    """
    Send a HID report to the connected host.

    :param report_type: HID report type (e.g. input report)
    :param report: bytes/bytearray with the report payload
    :param mtu: retained for backward compatibility; no longer used to
        skip waiting for the BTP command-complete response. The Zephyr
        tester always returns a BTP status for SEND_REPORT (success or
        failure) regardless of whether the report exceeds the L2CAP MTU,
        so we must always drain that response to keep the rx queue in
        sync. Fragmentation on the wire is handled by the L2CAP layer.
    """
    del mtu  # unused; kept in signature for backward compatibility
    logging.debug("%s report_type=%d", hid_device_send_report.__name__, report_type)

    report = bytearray(report)

    data = bytearray()
    data.extend(struct.pack('B', report_type))
    data.extend(struct.pack('H', len(report)))
    data.extend(report)

    iutctl = get_iut()
    iutctl.btp_socket.send(*HID_DEVICE['send_report'], data=data)

    hid_device_command_rsp_succ(defs.BTP_HID_DEVICE_CMD_SEND_REPORT)


def hid_device_enter_sniff_mode(min_interval, max_interval, attempt, timeout,
                                bd_addr_type=None, bd_addr=None):
    """Ask the IUT to put the ACL link to the peer into sniff mode.

    All four parameters are in baseband slots of 0.625 ms and are passed
    straight to HCI_Sniff_Mode by the IUT.
    """
    logging.debug("%s %r %r %r %r %r %r", hid_device_enter_sniff_mode.__name__,
                  min_interval, max_interval, attempt, timeout,
                  bd_addr_type, bd_addr)

    if bd_addr_type is None:
        # BR/EDR-only command: pts_addr_type_get() would hand back the LE
        # address type and the tester would reject the request.
        bd_addr_type = defs.BTP_BR_ADDRESS_TYPE
    if bd_addr is None:
        bd_addr = pts_addr_get()

    data = bytearray()
    data.extend([bd_addr_type])
    data.extend(addr_str_to_le_bytes(bd_addr))
    data.extend(struct.pack('<HHHH', min_interval, max_interval, attempt,
                            timeout))

    iutctl = get_iut()
    iutctl.btp_socket.send(*HID_DEVICE['enter_sniff_mode'], data=data)

    hid_device_command_rsp_succ(defs.BTP_HID_DEVICE_CMD_ENTER_SNIFF_MODE)


def hid_device_ev_connected(hid_device, data, data_len):
    """Decode HID Device Connected Event.

    BTP HID Device Connected Event format:
    0        6
    +--------+
    | Addr   |
    | (6B)   |
    +--------+

    """
    logging.debug("%s %r", hid_device_ev_connected.__name__, data)

    fmt = '<6s'
    if len(data) != struct.calcsize(fmt):
        raise ValueError("Invalid data length for HID Device Connected Event")

    (addr,) = struct.unpack(fmt, data)
    addr = le_bytes_to_hex_str(addr).upper()

    logging.debug("HID Device Connected: addr=%s", addr)

    hid_device.set_connected(addr, None)
    return True


def hid_device_ev_disconnected(hid_device, data, data_len):
    """Decode HID Device Disconnected Event.

    BTP HID Device Disconnected Event format:
    0        6
    +--------+
    | Addr   |
    | (6B)   |
    +--------+

    """
    logging.debug("%s %r", hid_device_ev_disconnected.__name__, data)

    fmt = '<6s'
    if len(data) != struct.calcsize(fmt):
        raise ValueError("Invalid data length for HID Device Disconnected Event")

    (addr,) = struct.unpack(fmt, data)
    addr = le_bytes_to_hex_str(addr).upper()

    logging.debug("HID Device Disconnected: addr=%s", addr)

    hid_device.set_disconnected(addr, None)
    return True


HID_DEVICE_EV = {
    defs.BTP_HID_DEVICE_EV_CONNECTED: hid_device_ev_connected,
    defs.BTP_HID_DEVICE_EV_DISCONNECTED: hid_device_ev_disconnected,
}
