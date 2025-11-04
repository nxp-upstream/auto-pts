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

from autopts.pybtp import defs
from autopts.pybtp.btp.btp import CONTROLLER_INDEX, get_iut_method as get_iut, \
    btp_hdr_check, pts_addr_get, pts_addr_type_get
from autopts.pybtp.types import BTPError, addr2btp_ba
from autopts.ptsprojects.stack import get_stack

log = logging.debug

HFP = {
    'read_supported_cmds': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_READ_SUPPORTED_COMMANDS,
                            CONTROLLER_INDEX),
    'enable_slc': (defs.BTP_SERVICE_ID_HFP,
                   defs.BTP_HFP_CMD_ENABLE_SLC,
                   CONTROLLER_INDEX),
    'disable_slc': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_DISABLE_SLC,
                    CONTROLLER_INDEX),
    'signal_strength_send': (defs.BTP_SERVICE_ID_HFP,
                             defs.BTP_HFP_CMD_SIGNAL_STRENGTH_SEND,
                             CONTROLLER_INDEX),
    'control': (defs.BTP_SERVICE_ID_HFP,
                defs.BTP_HFP_CMD_CONTROL,
                CONTROLLER_INDEX),
    'signal_strength_verify': (defs.BTP_SERVICE_ID_HFP,
                               defs.BTP_HFP_CMD_SIGNAL_STRENGTH_VERIFY,
                               CONTROLLER_INDEX),
    'ag_enable_call': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_AG_ENABLE_CALL,
                       CONTROLLER_INDEX),
    'ag_discoverable': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_AG_DISCOVERABLE,
                        CONTROLLER_INDEX),
    'hf_discoverable': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_HF_DISCOVERABLE,
                        CONTROLLER_INDEX),
    'verify_network_operator': (defs.BTP_SERVICE_ID_HFP,
                                defs.BTP_HFP_CMD_VERIFY_NETWORK_OPERATOR,
                                CONTROLLER_INDEX),
    'ag_disable_call_external': (defs.BTP_SERVICE_ID_HFP,
                                 defs.BTP_HFP_CMD_AG_DISABLE_CALL_EXTERNAL,
                                 CONTROLLER_INDEX),
    'hf_answer_call': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_HF_ANSWER_CALL,
                       CONTROLLER_INDEX),
    'verify': (defs.BTP_SERVICE_ID_HFP,
               defs.BTP_HFP_CMD_VERIFY,
               CONTROLLER_INDEX),
    'verify_voice_tag': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_VERIFY_VOICE_TAG,
                         CONTROLLER_INDEX),
    'speaker_mic_volume_send': (defs.BTP_SERVICE_ID_HFP,
                                defs.BTP_HFP_CMD_SPEAKER_MIC_VOLUME_SEND,
                                CONTROLLER_INDEX),
    'enable_audio': (defs.BTP_SERVICE_ID_HFP,
                     defs.BTP_HFP_CMD_ENABLE_AUDIO,
                     CONTROLLER_INDEX),
    'disable_audio': (defs.BTP_SERVICE_ID_HFP,
                      defs.BTP_HFP_CMD_DISABLE_AUDIO,
                      CONTROLLER_INDEX),
    'enable_network': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_ENABLE_NETWORK,
                       CONTROLLER_INDEX),
    'disable_network': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_DISABLE_NETWORK,
                        CONTROLLER_INDEX),
    'make_roam_active': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_MAKE_ROAM_ACTIVE,
                         CONTROLLER_INDEX),
    'make_roam_inactive': (defs.BTP_SERVICE_ID_HFP,
                           defs.BTP_HFP_CMD_MAKE_ROAM_INACTIVE,
                           CONTROLLER_INDEX),
    'make_battery_not_full_charged': (defs.BTP_SERVICE_ID_HFP,
                                      defs.BTP_HFP_CMD_MAKE_BATTERY_NOT_FULL_CHARGED,
                                      CONTROLLER_INDEX),
    'make_battery_full_charged': (defs.BTP_SERVICE_ID_HFP,
                                  defs.BTP_HFP_CMD_MAKE_BATTERY_FULL_CHARGED,
                                  CONTROLLER_INDEX),
    'verify_battery_charged': (defs.BTP_SERVICE_ID_HFP,
                               defs.BTP_HFP_CMD_VERIFY_BATTERY_CHARGED,
                               CONTROLLER_INDEX),
    'verify_battery_discharged': (defs.BTP_SERVICE_ID_HFP,
                                  defs.BTP_HFP_CMD_VERIFY_BATTERY_DISCHARGED,
                                  CONTROLLER_INDEX),
    'speaker_mic_volume_verify': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_SPEAKER_MIC_VOLUME_VERIFY,
                            CONTROLLER_INDEX),
    'ag_register': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_AG_REGISTER,
                            CONTROLLER_INDEX),
    'hf_register': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_HF_REGISTER,
                            CONTROLLER_INDEX),
    'verify_roam_active': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_VERIFY_ROAM_ACTIVE,
                            CONTROLLER_INDEX),
    'query_network_operator': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_QUERY_NETWORK_OPERATOR,
                            CONTROLLER_INDEX),
    'ag_vre_text': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_AG_VRE_TEXT,
                            CONTROLLER_INDEX),
    'dtmf_code_send': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_DTMF_CODE_SEND,
                            CONTROLLER_INDEX),
    'verify_roam_inactive': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_VERIFY_ROAM_INACTIVE,
                            CONTROLLER_INDEX),
    'private_consultation_mode': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_PRIVATE_CONSULTATION_MODE,
                            CONTROLLER_INDEX),
    'release_specified_call': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_RELEASE_SPECIFIED_CALL,
                            CONTROLLER_INDEX),
    'set_ongoing_calls': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_SET_ONGOING_CALLS,
                            CONTROLLER_INDEX),
    'ag_hold_incoming': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_AG_HOLD_INCOMING,
                         CONTROLLER_INDEX),
    'ag_last_dialed_number': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_AG_LAST_DIALED_NUMBER,
                         CONTROLLER_INDEX),
# BOND COMPLETION
}


def hfp_enable_slc(bd_addr=None, channel=None, is_ag=1, flags=0):
    logging.debug("%s %r %r %r", hfp_enable_slc.__name__, bd_addr, channel, is_ag)
    iutctl = get_iut()

    data_ba = bytearray()
    bd_addr_type_ba = struct.pack('B', pts_addr_type_get(defs.BTP_BR_ADDRESS_TYPE))
    bd_addr_ba = addr2btp_ba(pts_addr_get(bd_addr))

    data_ba.extend(bd_addr_type_ba)
    data_ba.extend(bd_addr_ba)
    data_ba.extend(struct.pack('B', channel))
    data_ba.extend(struct.pack('B', is_ag))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['enable_slc'], data=data_ba)


def hfp_disable_slc(flags=0):
    logging.debug("%s", hfp_disable_slc.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['disable_slc'], data=data_ba)


def hfp_signal_strength_send(strength, flags=0):
    logging.debug("%s %r", hfp_signal_strength_send.__name__, strength)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', strength))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['signal_strength_send'], data=data_ba)


def hfp_control(index, value=0, flags=0):
    logging.debug("%s %r %r", hfp_control.__name__, index, value)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', index))
    data_ba.extend(struct.pack('B', value))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['control'], data=data_ba)


def hfp_signal_strength_verify(strength, flags=0):
    logging.debug("%s %r", hfp_signal_strength_verify.__name__, strength)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', strength))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['signal_strength_verify'], data=data_ba)


def hfp_ag_enable_call(flags=0):
    logging.debug("%s", hfp_ag_enable_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_enable_call'], data=data_ba)


def hfp_ag_discoverable(flags=0):
    logging.debug("%s", hfp_ag_discoverable.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_discoverable'], data=data_ba)


def hfp_hf_discoverable(flags=0):
    logging.debug("%s", hfp_hf_discoverable.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_discoverable'], data=data_ba)


def hfp_verify_network_operator(name=""):
    logging.debug("%s", hfp_verify_network_operator.__name__)
    iutctl = get_iut()

    data_len = len(name)
    remain_len = 16 - data_len

    data_ba = bytearray()
    data_ba.extend(struct.pack('B', data_len))
    data_ba.extend(name.encode())
    if remain_len > 0:
        data_ba.extend(b'\x00' * remain_len)

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_network_operator'], data=data_ba)


def hfp_ag_disable_call_external(flags=0):
    logging.debug("%s", hfp_ag_disable_call_external.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_disable_call_external'], data=data_ba)


def hfp_hf_answer_call(flags=0):
    logging.debug("%s", hfp_hf_answer_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_answer_call'], data=data_ba)


def hfp_verify(verify_type, flags=0):
    logging.debug("%s", hfp_verify.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', verify_type))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['verify'], data=data_ba)


def hfp_verify_voice_tag(voice_tag=""):
    logging.debug("%s", hfp_verify_voice_tag.__name__)
    iutctl = get_iut()

    data_ba = voice_tag.encode()

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_voice_tag'], data=data_ba)


def hfp_speaker_mic_volume_send(speaker_mic, speaker_mic_volume, flags=0):
    logging.debug("%s", hfp_speaker_mic_volume_send.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', speaker_mic))
    data_ba.extend(struct.pack('B', speaker_mic_volume))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['speaker_mic_volume_send'], data=data_ba)


def hfp_enable_audio(flags=0):
    logging.debug("%s", hfp_enable_audio.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['enable_audio'], data=data_ba)


def hfp_disable_audio(flags=0):
    logging.debug("%s", hfp_disable_audio.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['disable_audio'], data=data_ba)


def hfp_enable_network(flags=0):
    logging.debug("%s", hfp_enable_network.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['enable_network'], data=data_ba)


def hfp_disable_network(flags=0):
    logging.debug("%s", hfp_disable_network.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['disable_network'], data=data_ba)


def hfp_make_roam_active(flags=0):
    logging.debug("%s", hfp_make_roam_active.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['make_roam_active'], data=data_ba)


def hfp_make_roam_inactive(flags=0):
    logging.debug("%s", hfp_make_roam_inactive.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['make_roam_inactive'], data=data_ba)


def hfp_make_battery_not_full_charged(flags=0):
    logging.debug("%s", hfp_make_battery_not_full_charged.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['make_battery_not_full_charged'], data=data_ba)


def hfp_make_battery_full_charged(flags=0):
    logging.debug("%s", hfp_make_battery_full_charged.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['make_battery_full_charged'], data=data_ba)


def hfp_verify_battery_charged(flags=0):
    logging.debug("%s", hfp_verify_battery_charged.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_battery_charged'], data=data_ba)


def hfp_verify_battery_discharged(flags=0):
    logging.debug("%s", hfp_verify_battery_discharged.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_battery_discharged'], data=data_ba)


def hfp_speaker_mic_volume_verify(speaker_mic, speaker_mic_volume, flags=0):
    logging.debug("%s", hfp_speaker_mic_volume_verify.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', speaker_mic))
    data_ba.extend(struct.pack('B', speaker_mic_volume))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['speaker_mic_volume_verify'], data=data_ba)

def hfp_ag_register(flags=0):
    logging.debug("%s", hfp_ag_register.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_register'], data=data_ba)

def hfp_hf_register(flags=0):
    logging.debug("%s", hfp_hf_register.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_register'], data=data_ba)

def hfp_verify_roam_active(flags=0):
    logging.debug("%s", hfp_verify_roam_active.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_roam_active'], data=data_ba)

def hfp_query_network_operator(flags=0):
    logging.debug("%s", hfp_query_network_operator.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['query_network_operator'], data=data_ba)

def hfp_ag_vre_text(type, operation, status=1, id=2, delay=0, flags=0):
    logging.debug("%s", hfp_ag_vre_text.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', status))
    data_ba.extend(struct.pack('H', id))
    data_ba.extend(struct.pack('B', type))
    data_ba.extend(struct.pack('B', operation))
    data_ba.extend(struct.pack('I', delay))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_vre_text'], data=data_ba)

def hfp_dtmf_code_send(dtmf_code, flags=0):
    logging.debug("%s", hfp_dtmf_code_send.__name__)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(struct.pack('B', dtmf_code))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['dtmf_code_send'], data=data_ba)

def hfp_verify_roam_inactive(flags=0):
    logging.debug("%s", hfp_verify_roam_inactive.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_roam_inactive'], data=data_ba)

def hfp_private_consultation_mode(index, flags=0):
    logging.debug("%s", hfp_private_consultation_mode.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', index-1))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['private_consultation_mode'], data=data_ba)

def hfp_release_specified_call(index, flags=0):
    logging.debug("%s", hfp_release_specified_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', index-1))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['release_specified_call'], data=data_ba)

def hfp_set_ongoing_calls(number, type, status, dir, all=False, flags=0):
    logging.debug("%s", hfp_set_ongoing_calls.__name__)

    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(struct.pack('B', type))
    data_ba.extend(struct.pack('B', status))
    data_ba.extend(struct.pack('B', dir))
    if all:
        data_ba.extend(struct.pack('B', 1))
    else:
        data_ba.extend(struct.pack('B', 0))

    data_ba.extend(struct.pack('B', flags))
    data_ba.extend(struct.pack('B', len(number)))
    data_ba.extend(number.encode('utf-8'))

    iutctl.btp_socket.send_wait_rsp(*HFP['set_ongoing_calls'], data=data_ba)

def hfp_ag_hold_incoming(flags=0):
    logging.debug("%s", hfp_ag_hold_incoming.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_hold_incoming'], data=data_ba)

def hfp_ag_last_dialed_number(number, type, flags=0):
    logging.debug("%s", hfp_ag_last_dialed_number.__name__)

    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(struct.pack('B', type))
    data_ba.extend(struct.pack('B', flags))
    data_ba.extend(struct.pack('B', len(number)))
    data_ba.extend(number.encode('utf-8'))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_last_dialed_number'], data=data_ba)

# FUNC COMPLETION

def hfp_command_rsp_succ(timeout=20.0):
    logging.debug("%s", hfp_command_rsp_succ.__name__)

    iutctl = get_iut()

    tuple_hdr, tuple_data = iutctl.btp_socket.read(timeout)
    logging.debug("received %r %r", tuple_hdr, tuple_data)

    btp_hdr_check(tuple_hdr, defs.BTP_SERVICE_ID_HFP)

    return tuple_data


# An example event, to be changed or deleted
def hfp_ev_dummy_completed(hfp, data, data_len):
    logging.debug('%s %r', hfp_ev_dummy_completed.__name__, data)

    fmt = '<B6sB'
    if len(data) < struct.calcsize(fmt):
        raise BTPError('Invalid data length')

    addr_type, addr, status = struct.unpack_from(fmt, data)

    addr = binascii.hexlify(addr[::-1]).lower().decode('utf-8')

    logging.debug(f'HFP Dummy event completed: addr {addr} addr_type '
                  f'{addr_type} status {status}')

    hfp.event_received(defs.BTP_HFP_EV_DUMMY_COMPLETED, (addr_type, addr, status))


def hfp_sco_connected_ev(hfp, data, data_len):
    logging.debug("%s %r %r", hfp_sco_connected_ev.__name__, data, data_len)

    stack = get_stack()
    stack.hfp.sco_connected = True
    hfp.event_received(defs.BTP_HFP_EV_SCO_CONNECTED, None)


def hfp_sco_disconnected_ev(hfp, data, data_len):
    logging.debug("%s %r %r", hfp_sco_disconnected_ev.__name__, data, data_len)

    stack = get_stack()
    stack.hfp.sco_connected = False
    hfp.event_received(defs.BTP_HFP_EV_SCO_DISCONNECTED, None)


def hfp_new_call_ev(hfp, data, data_len):
    logging.debug("%s %r %r", hfp_new_call_ev.__name__, data, data_len)

    hdr_fmt = '<BBBB'
    hdr_len = struct.calcsize(hdr_fmt)

    if len(data) < hdr_len:
        raise BTPError('Invalid data length')

    index, type, dir, number_len = struct.unpack_from(hdr_fmt, data[:hdr_len])
    number = struct.unpack_from(f"{number_len}s", data, hdr_len)[0]
    hfp.new_call(number, type, index, dir)


def hfp_call_status_ev(hfp, data, data_len):
    logging.debug("%s %r %r", hfp_call_status_ev.__name__, data, data_len)

    hdr_fmt = '<BB'

    index, status = struct.unpack_from(hdr_fmt, data)
    hfp.update_call(index, status)


HFP_EV = {
    defs.BTP_HFP_EV_DUMMY_COMPLETED: hfp_ev_dummy_completed,
    defs.BTP_HFP_EV_SCO_CONNECTED: hfp_sco_connected_ev,
    defs.BTP_HFP_EV_SCO_DISCONNECTED: hfp_sco_disconnected_ev,
    defs.BTP_HFP_EV_NEW_CALL: hfp_new_call_ev,
    defs.BTP_HFP_EV_CALL_STATUS: hfp_call_status_ev,
}
