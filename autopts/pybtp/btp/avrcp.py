#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2025, NXP.
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

import binascii
import logging
import struct

from autopts.ptsprojects.stack import get_stack
from autopts.pybtp import defs
from autopts.pybtp.btp.btp import CONTROLLER_INDEX, get_iut_method as get_iut, \
    btp_hdr_check, pts_addr_get, pts_addr_type_get
from autopts.pybtp.types import BTPError, addr2btp_ba

log = logging.debug


AVRCP = {
    'read_supported_cmds': (defs.BTP_SERVICE_ID_AVRCP,
                            defs.BTP_AVRCP_CMD_READ_SUPPORTED_COMMANDS,
                            CONTROLLER_INDEX),
    'control_connect': (defs.BTP_SERVICE_ID_AVRCP,
                        defs.BTP_AVRCP_CMD_CONTROL_CONNECT,
                        CONTROLLER_INDEX),
    'control_disconnect': (defs.BTP_SERVICE_ID_AVRCP,
                           defs.BTP_AVRCP_CMD_CONTROL_DISCONNECT,
                           CONTROLLER_INDEX),
    'browsing_connect': (defs.BTP_SERVICE_ID_AVRCP,
                         defs.BTP_AVRCP_CMD_BROWSING_CONNECT,
                         CONTROLLER_INDEX),
    'browsing_disconnect': (defs.BTP_SERVICE_ID_AVRCP,
                            defs.BTP_AVRCP_CMD_BROWSING_DISCONNECT,
                            CONTROLLER_INDEX),
    'unit_info': (defs.BTP_SERVICE_ID_AVRCP,
                  defs.BTP_AVRCP_CMD_UNIT_INFO,
                  CONTROLLER_INDEX),
    'subunit_info': (defs.BTP_SERVICE_ID_AVRCP,
                     defs.BTP_AVRCP_CMD_SUBUNIT_INFO,
                     CONTROLLER_INDEX),
    'pass_through': (defs.BTP_SERVICE_ID_AVRCP,
                     defs.BTP_AVRCP_CMD_PASS_THROUGH,
                     CONTROLLER_INDEX),
    'vendor_dependent': (defs.BTP_SERVICE_ID_AVRCP,
                         defs.BTP_AVRCP_CMD_VENDOR_DEPENDENT,
                         CONTROLLER_INDEX),
}


def avrcp_command_rsp_succ(op=None, timeout=20.0):
    logging.debug("%s", avrcp_command_rsp_succ.__name__)

    iutctl = get_iut()

    tuple_hdr, tuple_data = iutctl.btp_socket.read(timeout)
    logging.debug("received %r %r", tuple_hdr, tuple_data)

    btp_hdr_check(tuple_hdr, defs.BTP_SERVICE_ID_AVRCP, op)

    return tuple_data


def avrcp_wait_for_connection(conn_type, bd_addr=None, timeout=5):
    stack = get_stack()
    stack.avrcp.wait_for_connection(pts_addr_get(bd_addr), conn_type, timeout)

def avrcp_wait_for_disconnection(conn_type, bd_addr=None, timeout=5):
    stack = get_stack()
    stack.avrcp.wait_for_disconnection(pts_addr_get(bd_addr), conn_type, timeout)

def avrcp_rx_data_get(ev, bd_addr=None):
    stack = get_stack()
    return stack.avrcp.rx_data_get(pts_addr_get(bd_addr), ev, timeout=5)

def _avrcp_wait_pass_though(type, opid, state, bd_addr, timeout):
    stack = get_stack()
    rx_data = stack.avrcp.rx_data_get(pts_addr_get(bd_addr), type, timeout, clear=False)
    if rx_data != None:
        byte = struct.pack('B', rx_data)
        if byte == (opid | state << 7):
            return rx_data
    return None

def avrcp_wait_pass_though_req(opid, state, bd_addr=None, timeout=5):
    _avrcp_wait_pass_though(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ, opid, state, bd_addr, timeout)

def avrcp_wait_pass_though_rsp(opid, state, bd_addr=None, timeout=5):
    _avrcp_wait_pass_though(defs.BTP_AVRCP_EV_PASS_THROUGH, opid, state, bd_addr, timeout)

def avrcp_control_connect(bd_addr=None):
    logging.debug("%s %r", avrcp_control_connect.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['control_connect'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_CONTROL_CONNECT)
    avrcp_wait_for_connection(defs.BTP_AVRCP_EV_CONTROL_CONNECTED)

def avrcp_control_disconnect(bd_addr=None):
    logging.debug("%s %r", avrcp_control_disconnect.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['control_disconnect'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_CONTROL_DISCONNECT)
    avrcp_wait_for_disconnection(defs.BTP_AVRCP_EV_CONTROL_CONNECTED)

def avrcp_browsing_connect(bd_addr=None):
    logging.debug("%s %r", avrcp_browsing_connect.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['browsing_connect'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_BROWSING_CONNECT)
    avrcp_wait_for_connection(defs.BTP_AVRCP_EV_BROWSING_CONNECTED)

def avrcp_browsing_disconnect(bd_addr=None):
    logging.debug("%s %r", avrcp_browsing_disconnect.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['browsing_disconnect'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_BROWSING_DISCONNECT)
    avrcp_wait_for_disconnection(defs.BTP_AVRCP_EV_BROWSING_CONNECTED)

def avrcp_unit_info(bd_addr=None):
    logging.debug("%s %r", avrcp_unit_info.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['unit_info'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_UNIT_INFO)

def avrcp_subunit_info(bd_addr=None):
    logging.debug("%s %r", avrcp_subunit_info.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['subunit_info'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_SUBUNIT_INFO)

def avrcp_pass_through(opid, state, payload=None, bd_addr=None):
    logging.debug("%s %r %r %r %r", avrcp_pass_through.__name__, bd_addr, opid, state, payload)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', opid))
    data_ba.extend(struct.pack('B', state))
    if payload is not None:
        data_ba.extend(struct.pack('B', len(payload)))
        data_ba.extend(payload)
    else:
        data_ba.extend(struct.pack('B', 0))

    iutctl.btp_socket.send(*AVRCP['pass_through'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_PASS_THROUGH)

def avrcp_vendor_dependent(pduid, payload=None, bd_addr=None):
    logging.debug("%s %r %r %r", avrcp_vendor_dependent.__name__, bd_addr, pduid, payload)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', pduid))
    if payload is not None:
        data_ba.extend(struct.pack('B', len(payload)))
        data_ba.extend(payload)
    else:
        data_ba.extend(struct.pack('B', 0))

    iutctl.btp_socket.send(*AVRCP['vendor_dependent'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_VENDOR_DEPENDENT)

# An example event, to be changed or deleted
# def avrcp_ev_dummy_completed(avrcp, data, data_len):
#     logging.debug('%s %r', avrcp_ev_dummy_completed.__name__, data)

#     fmt = '<B6sB'
#     if len(data) < struct.calcsize(fmt):
#         raise BTPError('Invalid data length')

#     addr_type, addr, status = struct.unpack_from(fmt, data)

#     addr = binascii.hexlify(addr[::-1]).lower().decode('utf-8')

#     logging.debug(f'AVRCP Dummy event completed: addr {addr} addr_type '
#                   f'{addr_type} status {status}')

#     avrcp.event_received(defs.BTP_AVRCP_EV_DUMMY_COMPLETED, (addr_type, addr, status))

def avrcp_ev_control_connected(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_control_connected.__name__, data)
    avrcp.add_connection(pts_addr_get(None), defs.BTP_AVRCP_EV_CONTROL_CONNECTED)

def avrcp_ev_control_disconnected(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_control_disconnected.__name__, data)
    avrcp.remove_connection(pts_addr_get(None), defs.BTP_AVRCP_EV_CONTROL_CONNECTED)

def avrcp_ev_browsing_connected(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_browsing_connected.__name__, data)
    avrcp.add_connection(pts_addr_get(None), defs.BTP_AVRCP_EV_BROWSING_CONNECTED)

def avrcp_ev_browsing_disconnected(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_browsing_disconnected.__name__, data)
    avrcp.remove_connection(pts_addr_get(None), defs.BTP_AVRCP_EV_BROWSING_CONNECTED)

def avrcp_ev_(avrcp, data, data_len, ev):
    avrcp.rx(pts_addr_get(None), ev, data)

def avrcp_ev_unit_info(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_unit_info.__name__, data)
    avrcp_ev_(avrcp, data, data_len, defs.BTP_AVRCP_EV_UNIT_INFO)

def avrcp_ev_subunit_info(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_subunit_info.__name__, data)
    avrcp_ev_(avrcp, data, data_len, defs.BTP_AVRCP_EV_SUBUNIT_INFO)

def avrcp_ev_pass_through(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_pass_through.__name__, data)
    avrcp_ev_(avrcp, data, data_len, defs.BTP_AVRCP_EV_PASS_THROUGH)

def avrcp_ev_vendor_dependent(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_vendor_dependent.__name__, data)
    avrcp_ev_(avrcp, data, data_len, defs.BTP_AVRCP_EV_VENDOR_DEPENDENT)

def avrcp_ev_unit_info_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_unit_info_req.__name__, data)
    avrcp_ev_(avrcp, data, data_len, defs.BTP_AVRCP_EV_UNIT_INFO_REQ)

def avrcp_ev_subunit_info_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_subunit_info_req.__name__, data)
    avrcp_ev_(avrcp, data, data_len, defs.BTP_AVRCP_EV_SUBUNIT_INFO_REQ)

def avrcp_ev_pass_through_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_pass_through_req.__name__, data)
    avrcp_ev_(avrcp, data, data_len, defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)

def avrcp_ev_vendor_dependent_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_vendor_dependent_req.__name__, data)
    avrcp_ev_(avrcp, data, data_len, defs.BTP_AVRCP_EV_VENDOR_DEPENDENT_REQ)

AVRCP_EV = {
    defs.BTP_AVRCP_EV_CONTROL_CONNECTED: avrcp_ev_control_connected,
    defs.BTP_AVRCP_EV_CONTROL_DISCONNECTED: avrcp_ev_control_disconnected,
    defs.BTP_AVRCP_EV_BROWSING_CONNECTED: avrcp_ev_browsing_connected,
    defs.BTP_AVRCP_EV_BROWSING_DISCONNECTED: avrcp_ev_browsing_disconnected,
    defs.BTP_AVRCP_EV_UNIT_INFO: avrcp_ev_unit_info,
    defs.BTP_AVRCP_EV_SUBUNIT_INFO: avrcp_ev_subunit_info,
    defs.BTP_AVRCP_EV_PASS_THROUGH: avrcp_ev_pass_through,
    defs.BTP_AVRCP_EV_VENDOR_DEPENDENT: avrcp_ev_vendor_dependent,
    defs.BTP_AVRCP_EV_UNIT_INFO_REQ: avrcp_ev_unit_info_req,
    defs.BTP_AVRCP_EV_SUBUNIT_INFO_REQ: avrcp_ev_subunit_info_req,
    defs.BTP_AVRCP_EV_PASS_THROUGH_REQ: avrcp_ev_pass_through_req,
    defs.BTP_AVRCP_EV_VENDOR_DEPENDENT_REQ: avrcp_ev_vendor_dependent_req,
}
