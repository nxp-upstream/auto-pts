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
from autopts.pybtp.types import (
    BTPError,
    addr2btp_ba,
    WIDParams,
    AVRCPSpecificOperation,
    AVRCPMediaContentNavigationScope,
    AVCTPPassThroughOperation,
    AVRCPNotificationEvents,
    AVRCPVendorUiqueOperationID
)
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
    'get_caps': (defs.BTP_SERVICE_ID_AVRCP,
                 defs.BTP_AVRCP_CMD_GET_CAPS,
                 CONTROLLER_INDEX),
    'list_player_app_setting_attrs': (defs.BTP_SERVICE_ID_AVRCP,
                                      defs.BTP_AVRCP_CMD_LIST_PLAYER_APP_SETTING_ATTRS,
                                      CONTROLLER_INDEX),
    'list_player_app_setting_vals': (defs.BTP_SERVICE_ID_AVRCP,
                                     defs.BTP_AVRCP_CMD_LIST_PLAYER_APP_SETTING_VALS,
                                     CONTROLLER_INDEX),
    'get_curr_player_app_setting_val': (defs.BTP_SERVICE_ID_AVRCP,
                                        defs.BTP_AVRCP_CMD_GET_CURR_PLAYER_APP_SETTING_VAL,
                                        CONTROLLER_INDEX),
    'set_player_app_setting_val': (defs.BTP_SERVICE_ID_AVRCP,
                                   defs.BTP_AVRCP_CMD_SET_PLAYER_APP_SETTING_VAL,
                                   CONTROLLER_INDEX),
    'get_player_app_setting_attr_text': (defs.BTP_SERVICE_ID_AVRCP,
                                         defs.BTP_AVRCP_CMD_GET_PLAYER_APP_SETTING_ATTR_TEXT,
                                         CONTROLLER_INDEX),
    'get_player_app_setting_val_text': (defs.BTP_SERVICE_ID_AVRCP,
                                        defs.BTP_AVRCP_CMD_GET_PLAYER_APP_SETTING_VAL_TEXT,
                                        CONTROLLER_INDEX),
    'inform_displayable_char_set': (defs.BTP_SERVICE_ID_AVRCP,
                                    defs.BTP_AVRCP_CMD_INFORM_DISPLAYABLE_CHAR_SET,
                                    CONTROLLER_INDEX),
    'inform_batt_status_of_ct': (defs.BTP_SERVICE_ID_AVRCP,
                                 defs.BTP_AVRCP_CMD_INFORM_BATT_STATUS_OF_CT,
                                 CONTROLLER_INDEX),
    'get_element_attrs': (defs.BTP_SERVICE_ID_AVRCP,
                          defs.BTP_AVRCP_CMD_GET_ELEMENT_ATTRS,
                          CONTROLLER_INDEX),
    'get_play_status': (defs.BTP_SERVICE_ID_AVRCP,
                        defs.BTP_AVRCP_CMD_GET_PLAY_STATUS,
                        CONTROLLER_INDEX),
    'register_notification': (defs.BTP_SERVICE_ID_AVRCP,
                              defs.BTP_AVRCP_CMD_REGISTER_NOTIFICATION,
                              CONTROLLER_INDEX),
    'set_absolute_volume': (defs.BTP_SERVICE_ID_AVRCP,
                            defs.BTP_AVRCP_CMD_SET_ABSOLUTE_VOLUME,
                            CONTROLLER_INDEX),
    'set_addressed_player': (defs.BTP_SERVICE_ID_AVRCP,
                             defs.BTP_AVRCP_CMD_SET_ADDRESSED_PLAYER,
                             CONTROLLER_INDEX),
    'set_browsed_player': (defs.BTP_SERVICE_ID_AVRCP,
                           defs.BTP_AVRCP_CMD_SET_BROWSED_PLAYER,
                           CONTROLLER_INDEX),
    'get_folder_items': (defs.BTP_SERVICE_ID_AVRCP,
                         defs.BTP_AVRCP_CMD_GET_FOLDER_ITEMS,
                         CONTROLLER_INDEX),
    'change_path': (defs.BTP_SERVICE_ID_AVRCP,
                    defs.BTP_AVRCP_CMD_CHANGE_PATH,
                    CONTROLLER_INDEX),
    'get_item_attrs': (defs.BTP_SERVICE_ID_AVRCP,
                       defs.BTP_AVRCP_CMD_GET_ITEM_ATTRS,
                       CONTROLLER_INDEX),
    'play_item': (defs.BTP_SERVICE_ID_AVRCP,
                  defs.BTP_AVRCP_CMD_PLAY_ITEM,
                  CONTROLLER_INDEX),
    'get_total_number_of_items': (defs.BTP_SERVICE_ID_AVRCP,
                                  defs.BTP_AVRCP_CMD_GET_TOTAL_NUMBER_OF_ITEMS,
                                  CONTROLLER_INDEX),
    'search': (defs.BTP_SERVICE_ID_AVRCP,
               defs.BTP_AVRCP_CMD_SEARCH,
               CONTROLLER_INDEX),
    'add_to_now_playing': (defs.BTP_SERVICE_ID_AVRCP,
                           defs.BTP_AVRCP_CMD_ADD_TO_NOW_PLAYING,
                           CONTROLLER_INDEX),
    'general_reject': (defs.BTP_SERVICE_ID_AVRCP,
                       defs.BTP_AVRCP_CMD_GENERAL_REJECT,
                       CONTROLLER_INDEX),
    'tg_register_notification': (defs.BTP_SERVICE_ID_AVRCP,
                                 defs.BTP_AVRCP_CMD_TG_REGISTER_NOTIFICATION,
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
    return stack.avrcp.wait_for_connection(pts_addr_get(bd_addr), conn_type, timeout)

def avrcp_wait_for_disconnection(conn_type, bd_addr=None, timeout=5):
    stack = get_stack()
    return stack.avrcp.wait_for_disconnection(pts_addr_get(bd_addr), conn_type, timeout)

def avrcp_rx_data_get(ev, bd_addr=None, timeout=5):
    stack = get_stack()
    return stack.avrcp.rx_data_get(pts_addr_get(bd_addr), ev, timeout)

def _avrcp_wait_pass_though(ev, opid, state, bd_addr, timeout):
    stack = get_stack()
    while True:
        rx_data = stack.avrcp.rx_data_get(pts_addr_get(bd_addr), ev, timeout)
        if rx_data is None:
            break
        else:
            result, byte, data_len  = struct.unpack_from('<BBB', rx_data)
            if byte == (opid | state << 7):
                break
    return rx_data

def avrcp_wait_pass_though_req(opid, state, bd_addr=None, timeout=10):
    return _avrcp_wait_pass_though(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ, opid, state, bd_addr, timeout)

def avrcp_wait_pass_though_rsp(opid, state, bd_addr=None, timeout=10):
    return _avrcp_wait_pass_though(defs.BTP_AVRCP_EV_PASS_THROUGH_RSP, opid, state, bd_addr, timeout)

def avrcp_decode_get_folder_items_rsp(data: bytes):
    offset = 0
    if len(data) < 5:
        raise ValueError("Data too short for response header")

    # Parse response header
    status, uid_counter, num_items = struct.unpack_from('>B H H', data, offset)
    offset += 5

    items = []

    for _ in range(num_items):
        if offset + 3 > len(data):
            raise ValueError("Data too short for item header")
        item_type, item_len = struct.unpack_from('>B H', data, offset)
        offset += 3

        item_data = data[offset:offset + item_len]
        if len(item_data) < item_len:
            raise ValueError("Incomplete item data")

        if item_type == 0x01:  # Media Player
            if len(item_data) < 28:
                raise ValueError("Media Player item too short")
            (
                player_id, major_type, player_subtype, play_status,
                feature_bitmask, charset_id, name_len
            ) = struct.unpack_from('>H B I B 16s H H', item_data, 0)
            name_bytes = item_data[28:28 + name_len]
            try:
                name = name_bytes.decode('utf-8')
            except Exception:
                name = name_bytes.hex()
            items.append({
                "type": "media_player",
                "player_id": player_id,
                "major_type": major_type,
                "player_subtype": player_subtype,
                "play_status": play_status,
                "feature_bitmask": feature_bitmask,
                "charset_id": charset_id,
                "name_len": name_len,
                "name": name,
            })

        elif item_type == 0x02:  # Folder
            if len(item_data) < 15:
                raise ValueError("Folder item too short")
            uid = item_data[0:8]
            folder_type, playable, charset_id, name_len = struct.unpack_from('>B B H H', item_data, 8)
            name_bytes = item_data[14:14 + name_len]
            try:
                name = name_bytes.decode('utf-8')
            except Exception:
                name = name_bytes.hex()
            items.append({
                "type": "folder",
                "uid": uid,
                "folder_type": folder_type,
                "playable": playable,
                "charset_id": charset_id,
                "name_len": name_len,
                "name": name,
            })

        elif item_type == 0x03:  # Media Element
            if len(item_data) < 11:
                raise ValueError("Media Element item too short")
            uid = item_data[0:8]
            media_type, charset_id = struct.unpack_from('>B H', item_data, 8)
            # Only decode name (name_len + name[]) for now
            name_len = struct.unpack_from('>H', item_data, 10)[0]
            name_bytes = item_data[12:12 + name_len]
            try:
                name = name_bytes.decode('utf-8')
            except Exception:
                name = name_bytes.hex()
            items.append({
                "type": "media_element",
                "uid": uid,
                "media_type": media_type,
                "charset_id": charset_id,
                "name_len": name_len,
                "name": name,
            })

        else:
            # Skip unsupported item types
            offset = offset

        offset += item_len

    return {
        "status": status,
        "uid_counter": uid_counter,
        "num_items": num_items,
        "items": items,
    }

def avrcp_control_connect(bd_addr=None):
    logging.debug("%s %r", avrcp_control_connect.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['control_connect'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_CONTROL_CONNECT)

def avrcp_control_disconnect(bd_addr=None):
    logging.debug("%s %r", avrcp_control_disconnect.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['control_disconnect'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_CONTROL_DISCONNECT)

def avrcp_browsing_connect(bd_addr=None):
    logging.debug("%s %r", avrcp_browsing_connect.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['browsing_connect'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_BROWSING_CONNECT)

def avrcp_browsing_disconnect(bd_addr=None):
    logging.debug("%s %r", avrcp_browsing_disconnect.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['browsing_disconnect'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_BROWSING_DISCONNECT)

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

def avrcp_get_caps(cap_id, bd_addr=None):
    logging.debug("%s %r %r", avrcp_get_caps.__name__, bd_addr, cap_id)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', cap_id))

    iutctl.btp_socket.send(*AVRCP['get_caps'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_CAPS)

def avrcp_list_player_app_setting_attrs(bd_addr=None):
    logging.debug("%s %r", avrcp_list_player_app_setting_attrs.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['list_player_app_setting_attrs'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_LIST_PLAYER_APP_SETTING_ATTRS)

def avrcp_list_player_app_setting_vals(attr_id, bd_addr=None):
    logging.debug("%s %r %r", avrcp_list_player_app_setting_vals.__name__, bd_addr, attr_id)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', attr_id))

    iutctl.btp_socket.send(*AVRCP['list_player_app_setting_vals'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_LIST_PLAYER_APP_SETTING_VALS)

def avrcp_get_curr_player_app_setting_val_attr(attr_ids: list, bd_addr=None):
    logging.debug("%s %r %r", avrcp_get_curr_player_app_setting_val_attr.__name__, bd_addr, attr_ids)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    if len(attr_ids) == 0:
        raise BTPError("attr_ids shouldn't be empty")

    data_ba.extend(struct.pack('B', len(attr_ids)))
    for attr in attr_ids:
        data_ba.extend(struct.pack('B', attr))

    iutctl.btp_socket.send(*AVRCP['get_curr_player_app_setting_val'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_CURR_PLAYER_APP_SETTING_VAL)

def avrcp_set_player_app_setting_val(attr_vals: list[tuple[int, int]], bd_addr=None):
    logging.debug("%s %r %r", avrcp_set_player_app_setting_val.__name__, bd_addr, attr_vals)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    if len(attr_vals) == 0:
        raise BTPError("attr_vals shouldn't be empty")

    data_ba.extend(struct.pack('B', len(attr_vals)))
    for attr, val in attr_vals:
        data_ba.extend(struct.pack('B', attr))
        data_ba.extend(struct.pack('B', val))

    iutctl.btp_socket.send(*AVRCP['set_player_app_setting_val'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_SET_PLAYER_APP_SETTING_VAL)

def avrcp_get_player_app_setting_attr_text(attr_ids: list, bd_addr=None):
    logging.debug("%s %r %r", avrcp_get_player_app_setting_attr_text.__name__, bd_addr, attr_ids)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    if len(attr_ids) == 0:
        raise BTPError("attr_ids shouldn't be empty")

    data_ba.extend(struct.pack('B', len(attr_ids)))
    for attr in attr_ids:
        data_ba.extend(struct.pack('B', attr))

    iutctl.btp_socket.send(*AVRCP['get_player_app_setting_attr_text'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_PLAYER_APP_SETTING_ATTR_TEXT)

def avrcp_get_player_app_setting_val_text(attr_id, val_ids: list, bd_addr=None):
    logging.debug("%s %r %r", avrcp_get_player_app_setting_val_text.__name__, attr_id, val_ids)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    if len(val_ids) == 0:
        raise BTPError("val_ids shouldn't be empty")

    data_ba.extend(struct.pack('B', len(val_ids)))
    for val in val_ids:
        data_ba.extend(struct.pack('B', val))

    iutctl.btp_socket.send(*AVRCP['get_player_app_setting_val_text'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_PLAYER_APP_SETTING_VAL_TEXT)

def avrcp_get_play_status(bd_addr=None):
    logging.debug("%s %r", avrcp_get_play_status.__name__, bd_addr)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))

    iutctl.btp_socket.send(*AVRCP['get_play_status'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_PLAY_STATUS)

def avrcp_get_element_attrs(attrs: list, bd_addr=None):
    logging.debug("%s %r %r", avrcp_get_element_attrs.__name__, bd_addr, attrs)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', len(attrs)))
    for attr in attrs:
        data_ba.extend(struct.pack('>I', attr))

    iutctl.btp_socket.send(*AVRCP['get_element_attrs'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_ELEMENT_ATTRS)

def avrcp_register_notification(event_id, interval=0, bd_addr=None):
    logging.debug("%s %r %r %r", avrcp_register_notification.__name__, bd_addr, event_id, interval)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', event_id))
    if event_id == AVRCPNotificationEvents.EVENT_PLAYBACK_POS_CHANGED:
        if interval == 0:
            raise BTPError("interval shouldn't be 0 when event_id is EVENT_PLAYBACK_POS_CHANGED")
    data_ba.extend(struct.pack('>I', interval))

    iutctl.btp_socket.send(*AVRCP['register_notification'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_REGISTER_NOTIFICATION)

def avrcp_set_absolute_volume(volume, bd_addr=None):
    logging.debug("%s %r %r", avrcp_set_absolute_volume.__name__, bd_addr, volume)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', volume))

    iutctl.btp_socket.send(*AVRCP['set_absolute_volume'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_SET_ABSOLUTE_VOLUME)

def avrcp_set_addressed_player(player_id, bd_addr=None):
    logging.debug("%s %r %r", avrcp_set_addressed_player.__name__, bd_addr, player_id)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('>H', player_id))

    iutctl.btp_socket.send(*AVRCP['set_addressed_player'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_SET_ADDRESSED_PLAYER)

def avrcp_get_folder_items(scope, start_item, end_item, attr_cnt, attr_list: list, bd_addr=None):
    logging.debug("%s %r %r %r %r %r %r", avrcp_get_folder_items.__name__, bd_addr, scope, start_item, end_item, attr_cnt, attr_list)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', scope))
    data_ba.extend(struct.pack('>I', start_item))
    data_ba.extend(struct.pack('>I', end_item))
    data_ba.extend(struct.pack('B', attr_cnt))
    if attr_cnt >= 0x01 and attr_cnt <= 0xFE:
        if len[attr_list] != attr_cnt:
            raise BTPError("attr_list should be the same as attr_cnt when attr_cnt is 0x01~0xFE")
        for attr in attr_list:
            data_ba.extend(struct.pack('>I', attr))

    iutctl.btp_socket.send(*AVRCP['get_folder_items'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_FOLDER_ITEMS)

def avrcp_get_total_number_of_items(scope, bd_addr=None):
    logging.debug("%s %r %r", avrcp_get_total_number_of_items.__name__, bd_addr, scope)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', scope))

    iutctl.btp_socket.send(*AVRCP['get_total_number_of_items'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_TOTAL_NUMBER_OF_ITEMS)

def avrcp_set_browsed_player(player_id, bd_addr=None):
    logging.debug("%s %r %r", avrcp_set_browsed_player.__name__, bd_addr, player_id)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('<H', player_id))

    iutctl.btp_socket.send(*AVRCP['set_browsed_player'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_SET_BROWSED_PLAYER)

def avrcp_change_path(uid_counter, direction, uid, bd_addr=None):
    logging.debug("%s %r %r %r %r", avrcp_change_path.__name__, bd_addr, uid_counter, direction, uid)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('>H', uid_counter))
    data_ba.extend(struct.pack('B', direction))
    data_ba.extend(uid)

    iutctl.btp_socket.send(*AVRCP['change_path'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_CHANGE_PATH)

def avrcp_get_item_attrs(scope, uid, uid_counter, attrs: list, bd_addr=None):
    logging.debug("%s %r %r %r %r %r", avrcp_get_item_attrs.__name__, bd_addr, scope, uid, uid_counter, attrs)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', scope))
    data_ba.extend(uid)
    data_ba.extend(struct.pack('>H', uid_counter))
    data_ba.extend(struct.pack('B', len(attrs)))
    for attr in attrs:
        data_ba.extend(struct.pack('>I', attr))

    iutctl.btp_socket.send(*AVRCP['get_item_attrs'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_GET_ITEM_ATTRS)

def avrcp_play_item(scope, uid, uid_counter, bd_addr=None):
    logging.debug("%s %r %r %r %r", avrcp_change_path.__name__, bd_addr, scope, uid, uid_counter)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', scope))
    data_ba.extend(uid)
    data_ba.extend(struct.pack('>H', uid_counter))

    iutctl.btp_socket.send(*AVRCP['play_item'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_PLAY_ITEM)

def avrcp_search(string, bd_addr=None):
    logging.debug("%s %r %r", avrcp_search.__name__, bd_addr, string)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('<H', len(string)))
    data_ba.extend(string.encode('utf-8'))

    iutctl.btp_socket.send(*AVRCP['search'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_SEARCH)

def avrcp_add_to_now_playing(scope, uid, uid_counter, bd_addr=None):
    logging.debug("%s %r %r %r %r", avrcp_add_to_now_playing.__name__, bd_addr, scope, uid, uid_counter)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', scope))
    data_ba.extend(uid)
    data_ba.extend(struct.pack('>H', uid_counter))

    iutctl.btp_socket.send(*AVRCP['add_to_now_playing'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_ADD_TO_NOW_PLAYING)

def avrcp_tg_register_notification(event_id, payload=None, bd_addr=None):
    logging.debug("%s %r %r %r", avrcp_tg_register_notification.__name__, bd_addr, event_id, payload)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(addr2btp_ba(pts_addr_get(bd_addr)))
    data_ba.extend(struct.pack('B', event_id))
    if event_id == AVRCPNotificationEvents.EVENT_TRACK_CHANGED:
        if payload is None:
            raise BTPError("payload shouldn't be None")
        uid = struct.pack('>Q', payload)
        data_ba.extend(uid)
    elif event_id == AVRCPNotificationEvents.EVENT_PLAYER_APPLICATION_SETTING_CHANGED:
        if payload is None:
            raise BTPError("payload shouldn't be None")
        data_ba.extend(payload)
    elif event_id == AVRCPNotificationEvents.EVENT_VOLUME_CHANGED:
        if payload is None:
            raise BTPError("payload shouldn't be None")
        volume = struct.pack('B', payload)
        data_ba.extend(volume)

    iutctl.btp_socket.send(*AVRCP['tg_register_notification'], data=data_ba)
    avrcp_command_rsp_succ(defs.BTP_AVRCP_CMD_TG_REGISTER_NOTIFICATION)

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

def _avrcp_ev_decode_addr(data):
    hdr = '<6s'
    hdr_len = struct.calcsize(hdr)
    if len(data) < hdr_len:
        raise BTPError('Invalid data length')

    addr = struct.unpack_from(hdr, data)[0]
    addr = binascii.hexlify(addr[::-1]).lower().decode('utf-8')

    return addr, data[hdr_len:]

def avrcp_ev_control_connected(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_control_connected.__name__, data)
    addr = _avrcp_ev_decode_addr(data)[0]
    avrcp.add_connection(addr, defs.BTP_AVRCP_EV_CONTROL_CONNECTED)

def avrcp_ev_control_disconnected(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_control_disconnected.__name__, data)
    addr = _avrcp_ev_decode_addr(data)[0]
    avrcp.remove_connection(addr, defs.BTP_AVRCP_EV_CONTROL_CONNECTED)

def avrcp_ev_browsing_connected(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_browsing_connected.__name__, data)
    addr = _avrcp_ev_decode_addr(data)[0]
    avrcp.add_connection(addr, defs.BTP_AVRCP_EV_BROWSING_CONNECTED)

def avrcp_ev_browsing_disconnected(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_browsing_disconnected.__name__, data)
    addr = _avrcp_ev_decode_addr(data)[0]
    avrcp.remove_connection(addr, defs.BTP_AVRCP_EV_BROWSING_CONNECTED)

def _avrcp_ev(avrcp, data, data_len, ev):
    addr, data = _avrcp_ev_decode_addr(data)
    avrcp.rx(addr, ev, data)

def avrcp_ev_unit_info_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_unit_info_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_UNIT_INFO_RSP)

def avrcp_ev_subunit_info_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_subunit_info_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SUBUNIT_INFO_RSP)

def avrcp_ev_pass_through_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_pass_through_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_PASS_THROUGH_RSP)

def avrcp_ev_get_caps_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_caps_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_CAPS_RSP)

def avrcp_ev_list_player_app_setting_attrs_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_list_player_app_setting_attrs_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_LIST_PLAYER_APP_SETTING_ATTRS_RSP)

def avrcp_ev_list_player_app_setting_vals_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_list_player_app_setting_vals_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_LIST_PLAYER_APP_SETTING_VALS_RSP)

def avrcp_ev_get_curr_player_app_setting_val_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_curr_player_app_setting_val_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_CURR_PLAYER_APP_SETTING_VAL_RSP)

def avrcp_ev_set_player_app_setting_val_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_set_player_app_setting_val_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SET_PLAYER_APP_SETTING_VAL_RSP)

def avrcp_ev_get_player_app_setting_attr_text_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_player_app_setting_attr_text_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_PLAYER_APP_SETTING_ATTR_TEXT_RSP)

def avrcp_ev_get_player_app_setting_val_text_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_player_app_setting_val_text_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_PLAYER_APP_SETTING_VAL_TEXT_RSP)

def avrcp_ev_inform_displayable_char_set_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_inform_displayable_char_set_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_INFORM_DISPLAYABLE_CHAR_SET_RSP)

def avrcp_ev_inform_batt_status_of_ct_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_inform_batt_status_of_ct_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_INFORM_BATT_STATUS_OF_CT_RSP)

def avrcp_ev_get_element_attrs_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_element_attrs_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_ELEMENT_ATTRS_RSP)

def avrcp_ev_get_play_status_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_play_status_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_PLAY_STATUS_RSP)

def avrcp_ev_register_notification_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_register_notification_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_REGISTER_NOTIFICATION_RSP)

def avrcp_ev_req_continuing_rsp_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_req_continuing_rsp_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_REQ_CONTINUING_RSP_RSP)

def avrcp_ev_abort_continuing_rsp_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_abort_continuing_rsp_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_ABORT_CONTINUING_RSP_RSP)

def avrcp_ev_set_absolute_volume_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_set_absolute_volume_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SET_ABSOLUTE_VOLUME_RSP)

def avrcp_ev_set_addressed_player_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_set_addressed_player_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SET_ADDRESSED_PLAYER_RSP)

def avrcp_ev_set_browsed_player_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_set_browsed_player_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SET_BROWSED_PLAYER_RSP)

def avrcp_ev_get_folder_items_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_folder_items_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_FOLDER_ITEMS_RSP)

def avrcp_ev_change_path_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_change_path_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_CHANGE_PATH_RSP)

def avrcp_ev_get_item_attrs_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_item_attrs_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_ITEM_ATTRS_RSP)

def avrcp_ev_play_item_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_play_item_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_PLAY_ITEM_RSP)

def avrcp_ev_get_total_number_of_items_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_total_number_of_items_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_TOTAL_NUMBER_OF_ITEMS_RSP)

def avrcp_ev_search_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_search_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SEARCH_RSP)

def avrcp_ev_add_to_now_playing_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_add_to_now_playing_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_ADD_TO_NOW_PLAYING_RSP)

def avrcp_ev_general_reject_rsp(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_general_reject_rsp.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GENERAL_REJECT_RSP)

def avrcp_ev_unit_info_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_unit_info_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_UNIT_INFO_REQ)

def avrcp_ev_subunit_info_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_subunit_info_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SUBUNIT_INFO_REQ)

def avrcp_ev_pass_through_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_pass_through_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)

def avrcp_ev_get_caps_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_caps_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_CAPS_REQ)

def avrcp_ev_list_player_app_setting_attrs_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_list_player_app_setting_attrs_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_LIST_PLAYER_APP_SETTING_ATTRS_REQ)

def avrcp_ev_list_player_app_setting_vals_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_list_player_app_setting_vals_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_LIST_PLAYER_APP_SETTING_VALS_REQ)

def avrcp_ev_get_curr_player_app_setting_val_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_curr_player_app_setting_val_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_CURR_PLAYER_APP_SETTING_VAL_REQ)

def avrcp_ev_set_player_app_setting_val_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_set_player_app_setting_val_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SET_PLAYER_APP_SETTING_VAL_REQ)

def avrcp_ev_get_player_app_setting_attr_text_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_player_app_setting_attr_text_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_PLAYER_APP_SETTING_ATTR_TEXT_REQ)

def avrcp_ev_get_player_app_setting_val_text_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_player_app_setting_val_text_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_PLAYER_APP_SETTING_VAL_TEXT_REQ)

def avrcp_ev_inform_displayable_char_set_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_inform_displayable_char_set_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_INFORM_DISPLAYABLE_CHAR_SET_REQ)

def avrcp_ev_inform_batt_status_of_ct_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_inform_batt_status_of_ct_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_INFORM_BATT_STATUS_OF_CT_REQ)

def avrcp_ev_get_element_attrs_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_element_attrs_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_ELEMENT_ATTRS_REQ)

def avrcp_ev_get_play_status_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_play_status_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_PLAY_STATUS_REQ)

def avrcp_ev_register_notification_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_register_notification_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_REGISTER_NOTIFICATION_REQ)

def avrcp_ev_set_absolute_volume_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_set_absolute_volume_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SET_ABSOLUTE_VOLUME_REQ)

def avrcp_ev_set_addressed_player_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_set_addressed_player_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SET_ADDRESSED_PLAYER_REQ)

def avrcp_ev_set_browsed_player_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_set_browsed_player_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SET_BROWSED_PLAYER_REQ)

def avrcp_ev_get_folder_items_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_folder_items_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_FOLDER_ITEMS_REQ)

def avrcp_ev_change_path_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_change_path_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_CHANGE_PATH_REQ)

def avrcp_ev_get_item_attrs_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_item_attrs_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_ITEM_ATTRS_REQ)

def avrcp_ev_play_item_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_play_item_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_PLAY_ITEM_REQ)

def avrcp_ev_get_total_number_of_items_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_get_total_number_of_items_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GET_TOTAL_NUMBER_OF_ITEMS_REQ)

def avrcp_ev_search_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_search_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_SEARCH_REQ)

def avrcp_ev_add_to_now_playing_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_add_to_now_playing_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_ADD_TO_NOW_PLAYING_REQ)

def avrcp_ev_general_reject_req(avrcp, data, data_len):
    logging.debug('%s %r', avrcp_ev_general_reject_req.__name__, data)
    _avrcp_ev(avrcp, data, data_len, defs.BTP_AVRCP_EV_GENERAL_REJECT_REQ)

AVRCP_EV = {
    defs.BTP_AVRCP_EV_CONTROL_CONNECTED: avrcp_ev_control_connected,
    defs.BTP_AVRCP_EV_CONTROL_DISCONNECTED: avrcp_ev_control_disconnected,
    defs.BTP_AVRCP_EV_BROWSING_CONNECTED: avrcp_ev_browsing_connected,
    defs.BTP_AVRCP_EV_BROWSING_DISCONNECTED: avrcp_ev_browsing_disconnected,
    defs.BTP_AVRCP_EV_UNIT_INFO_RSP: avrcp_ev_unit_info_rsp,
    defs.BTP_AVRCP_EV_SUBUNIT_INFO_RSP: avrcp_ev_subunit_info_rsp,
    defs.BTP_AVRCP_EV_PASS_THROUGH_RSP: avrcp_ev_pass_through_rsp,
    defs.BTP_AVRCP_EV_GET_CAPS_RSP: avrcp_ev_get_caps_rsp,
    defs.BTP_AVRCP_EV_LIST_PLAYER_APP_SETTING_ATTRS_RSP: avrcp_ev_list_player_app_setting_attrs_rsp,
    defs.BTP_AVRCP_EV_LIST_PLAYER_APP_SETTING_VALS_RSP: avrcp_ev_list_player_app_setting_vals_rsp,
    defs.BTP_AVRCP_EV_GET_CURR_PLAYER_APP_SETTING_VAL_RSP: avrcp_ev_get_curr_player_app_setting_val_rsp,
    defs.BTP_AVRCP_EV_SET_PLAYER_APP_SETTING_VAL_RSP: avrcp_ev_set_player_app_setting_val_rsp,
    defs.BTP_AVRCP_EV_GET_PLAYER_APP_SETTING_ATTR_TEXT_RSP: avrcp_ev_get_player_app_setting_attr_text_rsp,
    defs.BTP_AVRCP_EV_GET_PLAYER_APP_SETTING_VAL_TEXT_RSP: avrcp_ev_get_player_app_setting_val_text_rsp,
    defs.BTP_AVRCP_EV_INFORM_DISPLAYABLE_CHAR_SET_RSP: avrcp_ev_inform_displayable_char_set_rsp,
    defs.BTP_AVRCP_EV_INFORM_BATT_STATUS_OF_CT_RSP: avrcp_ev_inform_batt_status_of_ct_rsp,
    defs.BTP_AVRCP_EV_GET_ELEMENT_ATTRS_RSP: avrcp_ev_get_element_attrs_rsp,
    defs.BTP_AVRCP_EV_GET_PLAY_STATUS_RSP: avrcp_ev_get_play_status_rsp,
    defs.BTP_AVRCP_EV_REGISTER_NOTIFICATION_RSP: avrcp_ev_register_notification_rsp,
    defs.BTP_AVRCP_EV_REQ_CONTINUING_RSP_RSP: avrcp_ev_req_continuing_rsp_rsp,
    defs.BTP_AVRCP_EV_ABORT_CONTINUING_RSP_RSP: avrcp_ev_abort_continuing_rsp_rsp,
    defs.BTP_AVRCP_EV_SET_ABSOLUTE_VOLUME_RSP: avrcp_ev_set_absolute_volume_rsp,
    defs.BTP_AVRCP_EV_SET_ADDRESSED_PLAYER_RSP: avrcp_ev_set_addressed_player_rsp,
    defs.BTP_AVRCP_EV_SET_BROWSED_PLAYER_RSP: avrcp_ev_set_browsed_player_rsp,
    defs.BTP_AVRCP_EV_GET_FOLDER_ITEMS_RSP: avrcp_ev_get_folder_items_rsp,
    defs.BTP_AVRCP_EV_CHANGE_PATH_RSP: avrcp_ev_change_path_rsp,
    defs.BTP_AVRCP_EV_GET_ITEM_ATTRS_RSP: avrcp_ev_get_item_attrs_rsp,
    defs.BTP_AVRCP_EV_PLAY_ITEM_RSP: avrcp_ev_play_item_rsp,
    defs.BTP_AVRCP_EV_GET_TOTAL_NUMBER_OF_ITEMS_RSP: avrcp_ev_get_total_number_of_items_rsp,
    defs.BTP_AVRCP_EV_SEARCH_RSP: avrcp_ev_search_rsp,
    defs.BTP_AVRCP_EV_ADD_TO_NOW_PLAYING_RSP: avrcp_ev_add_to_now_playing_rsp,
    defs.BTP_AVRCP_EV_GENERAL_REJECT_RSP: avrcp_ev_general_reject_rsp,
    defs.BTP_AVRCP_EV_UNIT_INFO_REQ: avrcp_ev_unit_info_req,
    defs.BTP_AVRCP_EV_SUBUNIT_INFO_REQ: avrcp_ev_subunit_info_req,
    defs.BTP_AVRCP_EV_PASS_THROUGH_REQ: avrcp_ev_pass_through_req,
    defs.BTP_AVRCP_EV_GET_CAPS_REQ: avrcp_ev_get_caps_req,
    defs.BTP_AVRCP_EV_LIST_PLAYER_APP_SETTING_ATTRS_REQ: avrcp_ev_list_player_app_setting_attrs_req,
    defs.BTP_AVRCP_EV_LIST_PLAYER_APP_SETTING_VALS_REQ: avrcp_ev_list_player_app_setting_vals_req,
    defs.BTP_AVRCP_EV_GET_CURR_PLAYER_APP_SETTING_VAL_REQ: avrcp_ev_get_curr_player_app_setting_val_req,
    defs.BTP_AVRCP_EV_SET_PLAYER_APP_SETTING_VAL_REQ: avrcp_ev_set_player_app_setting_val_req,
    defs.BTP_AVRCP_EV_GET_PLAYER_APP_SETTING_ATTR_TEXT_REQ: avrcp_ev_get_player_app_setting_attr_text_req,
    defs.BTP_AVRCP_EV_GET_PLAYER_APP_SETTING_VAL_TEXT_REQ: avrcp_ev_get_player_app_setting_val_text_req,
    defs.BTP_AVRCP_EV_INFORM_DISPLAYABLE_CHAR_SET_REQ: avrcp_ev_inform_displayable_char_set_req,
    defs.BTP_AVRCP_EV_INFORM_BATT_STATUS_OF_CT_REQ: avrcp_ev_inform_batt_status_of_ct_req,
    defs.BTP_AVRCP_EV_GET_ELEMENT_ATTRS_REQ: avrcp_ev_get_element_attrs_req,
    defs.BTP_AVRCP_EV_GET_PLAY_STATUS_REQ: avrcp_ev_get_play_status_req,
    defs.BTP_AVRCP_EV_REGISTER_NOTIFICATION_REQ: avrcp_ev_register_notification_req,
    defs.BTP_AVRCP_EV_SET_ABSOLUTE_VOLUME_REQ: avrcp_ev_set_absolute_volume_req,
    defs.BTP_AVRCP_EV_SET_ADDRESSED_PLAYER_REQ: avrcp_ev_set_addressed_player_req,
    defs.BTP_AVRCP_EV_SET_BROWSED_PLAYER_REQ: avrcp_ev_set_browsed_player_req,
    defs.BTP_AVRCP_EV_GET_FOLDER_ITEMS_REQ: avrcp_ev_get_folder_items_req,
    defs.BTP_AVRCP_EV_CHANGE_PATH_REQ: avrcp_ev_change_path_req,
    defs.BTP_AVRCP_EV_GET_ITEM_ATTRS_REQ: avrcp_ev_get_item_attrs_req,
    defs.BTP_AVRCP_EV_PLAY_ITEM_REQ: avrcp_ev_play_item_req,
    defs.BTP_AVRCP_EV_GET_TOTAL_NUMBER_OF_ITEMS_REQ: avrcp_ev_get_total_number_of_items_req,
    defs.BTP_AVRCP_EV_SEARCH_REQ: avrcp_ev_search_req,
    defs.BTP_AVRCP_EV_ADD_TO_NOW_PLAYING_REQ: avrcp_ev_add_to_now_playing_req,
    defs.BTP_AVRCP_EV_GENERAL_REJECT_REQ: avrcp_ev_general_reject_req,
}
