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
    'ag_enable_slc': (defs.BTP_SERVICE_ID_HFP,
                      defs.BTP_HFP_CMD_AG_ENABLE_SLC,
                      CONTROLLER_INDEX),
    'hf_enable_slc': (defs.BTP_SERVICE_ID_HFP,
                      defs.BTP_HFP_CMD_HF_ENABLE_SLC,
                      CONTROLLER_INDEX),
    'ag_disable_slc': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_AG_DISABLE_SLC,
                       CONTROLLER_INDEX),
    'hf_disable_slc': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_HF_DISABLE_SLC,
                       CONTROLLER_INDEX),
    'ag_signal_strength_send': (defs.BTP_SERVICE_ID_HFP,
                                defs.BTP_HFP_CMD_AG_SIGNAL_STRENGTH_SEND,
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
    'ag_speaker_volume_send': (defs.BTP_SERVICE_ID_HFP,
                               defs.BTP_HFP_CMD_AG_SPEAKER_VOLUME_SEND,
                               CONTROLLER_INDEX),
    'ag_mic_volume_send': (defs.BTP_SERVICE_ID_HFP,
                           defs.BTP_HFP_CMD_AG_MIC_VOLUME_SEND,
                           CONTROLLER_INDEX),
    'hf_speaker_volume_send': (defs.BTP_SERVICE_ID_HFP,
                               defs.BTP_HFP_CMD_HF_SPEAKER_VOLUME_SEND,
                               CONTROLLER_INDEX),
    'hf_mic_volume_send': (defs.BTP_SERVICE_ID_HFP,
                           defs.BTP_HFP_CMD_HF_MIC_VOLUME_SEND,
                           CONTROLLER_INDEX),
    'ag_enable_audio': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_AG_ENABLE_AUDIO,
                        CONTROLLER_INDEX),
    'hf_enable_audio': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_HF_ENABLE_AUDIO,
                        CONTROLLER_INDEX),
    'disable_audio': (defs.BTP_SERVICE_ID_HFP,
                      defs.BTP_HFP_CMD_DISABLE_AUDIO,
                      CONTROLLER_INDEX),
    'ag_enable_network': (defs.BTP_SERVICE_ID_HFP,
                          defs.BTP_HFP_CMD_AG_ENABLE_NETWORK,
                          CONTROLLER_INDEX),
    'ag_disable_network': (defs.BTP_SERVICE_ID_HFP,
                           defs.BTP_HFP_CMD_AG_DISABLE_NETWORK,
                           CONTROLLER_INDEX),
    'ag_make_roam_active': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_AG_MAKE_ROAM_ACTIVE,
                            CONTROLLER_INDEX),
    'ag_make_roam_inactive': (defs.BTP_SERVICE_ID_HFP,
                              defs.BTP_HFP_CMD_AG_MAKE_ROAM_INACTIVE,
                              CONTROLLER_INDEX),
    'ag_make_battery_not_full_charged': (defs.BTP_SERVICE_ID_HFP,
                                         defs.BTP_HFP_CMD_AG_MAKE_BATTERY_NOT_FULL_CHARGED,
                                         CONTROLLER_INDEX),
    'ag_make_battery_full_charged': (defs.BTP_SERVICE_ID_HFP,
                                     defs.BTP_HFP_CMD_AG_MAKE_BATTERY_FULL_CHARGED,
                                     CONTROLLER_INDEX),
    'verify_battery_charged': (defs.BTP_SERVICE_ID_HFP,
                               defs.BTP_HFP_CMD_VERIFY_BATTERY_CHARGED,
                               CONTROLLER_INDEX),
    'verify_battery_discharged': (defs.BTP_SERVICE_ID_HFP,
                                  defs.BTP_HFP_CMD_VERIFY_BATTERY_DISCHARGED,
                                  CONTROLLER_INDEX),
    'speaker_volume_verify': (defs.BTP_SERVICE_ID_HFP,
                              defs.BTP_HFP_CMD_SPEAKER_VOLUME_VERIFY,
                              CONTROLLER_INDEX),
    'mic_volume_verify': (defs.BTP_SERVICE_ID_HFP,
                          defs.BTP_HFP_CMD_MIC_VOLUME_VERIFY,
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
    'hf_query_network_operator': (defs.BTP_SERVICE_ID_HFP,
                                  defs.BTP_HFP_CMD_HF_QUERY_NETWORK_OPERATOR,
                                  CONTROLLER_INDEX),
    'ag_vre_text': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_AG_VRE_TEXT,
                    CONTROLLER_INDEX),
    'hf_dtmf_code_send': (defs.BTP_SERVICE_ID_HFP,
                          defs.BTP_HFP_CMD_HF_DTMF_CODE_SEND,
                          CONTROLLER_INDEX),
    'verify_roam_inactive': (defs.BTP_SERVICE_ID_HFP,
                             defs.BTP_HFP_CMD_VERIFY_ROAM_INACTIVE,
                             CONTROLLER_INDEX),
    'hf_private_consultation_mode': (defs.BTP_SERVICE_ID_HFP,
                                     defs.BTP_HFP_CMD_HF_PRIVATE_CONSULTATION_MODE,
                                     CONTROLLER_INDEX),
    'hf_release_specified_call': (defs.BTP_SERVICE_ID_HFP,
                                  defs.BTP_HFP_CMD_HF_RELEASE_SPECIFIED_CALL,
                                  CONTROLLER_INDEX),
    'ag_set_ongoing_calls': (defs.BTP_SERVICE_ID_HFP,
                             defs.BTP_HFP_CMD_AG_SET_ONGOING_CALLS,
                             CONTROLLER_INDEX),
    'ag_hold_incoming': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_AG_HOLD_INCOMING,
                         CONTROLLER_INDEX),
    'ag_last_dialed_number': (defs.BTP_SERVICE_ID_HFP,
                              defs.BTP_HFP_CMD_AG_LAST_DIALED_NUMBER,
                              CONTROLLER_INDEX),
    'ag_answer_call': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_AG_ANSWER_CALL,
                       CONTROLLER_INDEX),
    'ag_reject_call': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_AG_REJECT_CALL,
                       CONTROLLER_INDEX),
    'hf_reject_call': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_HF_REJECT_CALL,
                       CONTROLLER_INDEX),
    'ag_end_call': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_AG_END_CALL,
                    CONTROLLER_INDEX),
    'hf_end_call': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_HF_END_CALL,
                    CONTROLLER_INDEX),
    'ag_disable_inband': (defs.BTP_SERVICE_ID_HFP,
                          defs.BTP_HFP_CMD_AG_DISABLE_INBAND,
                          CONTROLLER_INDEX),
    'ag_enable_inband': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_AG_ENABLE_INBAND,
                         CONTROLLER_INDEX),
    'ag_twc_call': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_AG_TWC_CALL,
                    CONTROLLER_INDEX),
    'ag_enable_vr': (defs.BTP_SERVICE_ID_HFP,
                     defs.BTP_HFP_CMD_AG_ENABLE_VR,
                     CONTROLLER_INDEX),
    'hf_enable_vr': (defs.BTP_SERVICE_ID_HFP,
                     defs.BTP_HFP_CMD_HF_ENABLE_VR,
                     CONTROLLER_INDEX),
    'ag_send_bcc': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_AG_SEND_BCC,
                    CONTROLLER_INDEX),
    'hf_send_bcc': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_HF_SEND_BCC,
                    CONTROLLER_INDEX),
    'ag_send_bcc_msbc': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_AG_SEND_BCC_MSBC,
                         CONTROLLER_INDEX),
    'hf_send_bcc_msbc': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_HF_SEND_BCC_MSBC,
                         CONTROLLER_INDEX),
    'ag_send_bcc_swb': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_AG_SEND_BCC_SWB,
                        CONTROLLER_INDEX),
    'hf_send_bcc_swb': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_HF_SEND_BCC_SWB,
                        CONTROLLER_INDEX),
    'cls_mem_call_list': (defs.BTP_SERVICE_ID_HFP,
                          defs.BTP_HFP_CMD_CLS_MEM_CALL_LIST,
                          CONTROLLER_INDEX),
    'hf_accept_held_call': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_HF_ACCEPT_HELD_CALL,
                            CONTROLLER_INDEX),
    'hf_held_active_call': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_HF_HELD_ACTIVE_CALL,
                            CONTROLLER_INDEX),
    'ag_accept_incoming_held_call': (defs.BTP_SERVICE_ID_HFP,
                                     defs.BTP_HFP_CMD_AG_ACCEPT_INCOMING_HELD_CALL,
                                     CONTROLLER_INDEX),
    'hf_accept_incoming_held_call': (defs.BTP_SERVICE_ID_HFP,
                                     defs.BTP_HFP_CMD_HF_ACCEPT_INCOMING_HELD_CALL,
                                     CONTROLLER_INDEX),
    'ag_reject_held_call': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_AG_REJECT_HELD_CALL,
                            CONTROLLER_INDEX),
    'hf_reject_held_call': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_HF_REJECT_HELD_CALL,
                            CONTROLLER_INDEX),
    'ag_out_call': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_AG_OUT_CALL,
                    CONTROLLER_INDEX),
    'hf_out_call': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_HF_OUT_CALL,
                    CONTROLLER_INDEX),
    'hf_enable_clip': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_HF_ENABLE_CLIP,
                       CONTROLLER_INDEX),
    'hf_send_iia': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_HF_SEND_IIA,
                    CONTROLLER_INDEX),
    'hf_enable_sub_number': (defs.BTP_SERVICE_ID_HFP,
                             defs.BTP_HFP_CMD_HF_ENABLE_SUB_NUMBER,
                             CONTROLLER_INDEX),
    'hf_out_mem_call': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_HF_OUT_MEM_CALL,
                        CONTROLLER_INDEX),
    'hf_out_mem_outofrange_call': (defs.BTP_SERVICE_ID_HFP,
                                   defs.BTP_HFP_CMD_HF_OUT_MEM_OUTOFRANGE_CALL,
                                   CONTROLLER_INDEX),
    'hf_ec_nr_disable': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_HF_EC_NR_DISABLE,
                         CONTROLLER_INDEX),
    'ag_disable_vr': (defs.BTP_SERVICE_ID_HFP,
                      defs.BTP_HFP_CMD_AG_DIASBLE_VR,
                      CONTROLLER_INDEX),
    'hf_disable_vr': (defs.BTP_SERVICE_ID_HFP,
                      defs.BTP_HFP_CMD_HF_DISABLE_VR,
                      CONTROLLER_INDEX),
    'hf_enable_binp': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_HF_ENABLE_BINP,
                       CONTROLLER_INDEX),
    'ag_join_conversation_call': (defs.BTP_SERVICE_ID_HFP,
                                  defs.BTP_HFP_CMD_AG_JOIN_CONVERSATION_CALL,
                                  CONTROLLER_INDEX),
    'hf_join_conversation_call': (defs.BTP_SERVICE_ID_HFP,
                                  defs.BTP_HFP_CMD_HF_JOIN_CONVERSATION_CALL,
                                  CONTROLLER_INDEX),
    'hf_explicit_transfer_call': (defs.BTP_SERVICE_ID_HFP,
                                  defs.BTP_HFP_CMD_HF_EXPLICIT_TRANSFER_CALL,
                                  CONTROLLER_INDEX),
    'hf_out_last_call': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_HF_OUT_LAST_CALL,
                         CONTROLLER_INDEX),
    'hf_disable_active_call': (defs.BTP_SERVICE_ID_HFP,
                               defs.BTP_HFP_CMD_HF_DISABLE_ACTIVE_CALL,
                               CONTROLLER_INDEX),
    'hf_end_second_call': (defs.BTP_SERVICE_ID_HFP,
                           defs.BTP_HFP_CMD_HF_END_SECOND_CALL,
                           CONTROLLER_INDEX),
    'mute_inband_ring': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_MUTE_INBAND_RING,
                         CONTROLLER_INDEX),
    'ag_remote_reject': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_AG_REMOTE_REJECT,
                         CONTROLLER_INDEX),
    'ag_remote_ring': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_AG_REMOTE_RING,
                       CONTROLLER_INDEX),
    'ag_hold': (defs.BTP_SERVICE_ID_HFP,
                defs.BTP_HFP_CMD_AG_HOLD,
                CONTROLLER_INDEX),
    'ag_retrieve': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_AG_RETRIEVE,
                    CONTROLLER_INDEX),
    'ag_ver_state': (defs.BTP_SERVICE_ID_HFP,
                     defs.BTP_HFP_CMD_AG_VER_STATE,
                     CONTROLLER_INDEX),
    'hf_indicator_value': (defs.BTP_SERVICE_ID_HFP,
                           defs.BTP_HFP_CMD_HF_INDICATOR_VALUE,
                           CONTROLLER_INDEX),
    'hf_ready_accept_audio': (defs.BTP_SERVICE_ID_HFP,
                              defs.BTP_HFP_CMD_HF_READY_ACCEPT_AUDIO,
                              CONTROLLER_INDEX),
    'hf_impair_signal': (defs.BTP_SERVICE_ID_HFP,
                         defs.BTP_HFP_CMD_HF_IMPAIR_SIGNAL,
                         CONTROLLER_INDEX),
    'ag_set_last_num': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_AG_SET_LAST_NUM,
                        CONTROLLER_INDEX),
    # BOND COMPLETION
}


def hfp_ag_enable_slc(bd_addr=None, channel=None):
    logging.debug("%s %r %r", hfp_ag_enable_slc.__name__, bd_addr, channel)
    iutctl = get_iut()

    data_ba = bytearray()
    bd_addr_type_ba = struct.pack('B', pts_addr_type_get(defs.BTP_BR_ADDRESS_TYPE))
    bd_addr_ba = addr2btp_ba(pts_addr_get(bd_addr))

    data_ba.extend(bd_addr_type_ba)
    data_ba.extend(bd_addr_ba)
    data_ba.extend(struct.pack('B', channel))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_enable_slc'], data=data_ba)


def hfp_hf_enable_slc(bd_addr=None, channel=None):
    logging.debug("%s %r %r", hfp_hf_enable_slc.__name__, bd_addr, channel)
    iutctl = get_iut()

    data_ba = bytearray()
    bd_addr_type_ba = struct.pack('B', pts_addr_type_get(defs.BTP_BR_ADDRESS_TYPE))
    bd_addr_ba = addr2btp_ba(pts_addr_get(bd_addr))

    data_ba.extend(bd_addr_type_ba)
    data_ba.extend(bd_addr_ba)
    data_ba.extend(struct.pack('B', channel))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_enable_slc'], data=data_ba)


def hfp_ag_disable_slc():
    logging.debug("%s", hfp_ag_disable_slc.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_disable_slc'], data=bytearray())


def hfp_hf_disable_slc():
    logging.debug("%s", hfp_hf_disable_slc.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_disable_slc'], data=bytearray())


def hfp_ag_signal_strength_send(strength):
    logging.debug("%s %r", hfp_ag_signal_strength_send.__name__, strength)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', strength))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_signal_strength_send'], data=data_ba)


def hfp_signal_strength_verify(strength):
    logging.debug("%s %r", hfp_signal_strength_verify.__name__, strength)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', strength))

    iutctl.btp_socket.send_wait_rsp(*HFP['signal_strength_verify'], data=data_ba)


def hfp_ag_enable_call():
    logging.debug("%s", hfp_ag_enable_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_enable_call'], data=bytearray())


def hfp_ag_discoverable():
    logging.debug("%s", hfp_ag_discoverable.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_discoverable'], data=bytearray())


def hfp_hf_discoverable():
    logging.debug("%s", hfp_hf_discoverable.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_discoverable'], data=bytearray())


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


def hfp_ag_disable_call_external():
    logging.debug("%s", hfp_ag_disable_call_external.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_disable_call_external'], data=bytearray())


def hfp_hf_answer_call():
    logging.debug("%s", hfp_hf_answer_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_answer_call'], data=bytearray())


def hfp_verify(verify_type):
    logging.debug("%s", hfp_verify.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', verify_type))

    iutctl.btp_socket.send_wait_rsp(*HFP['verify'], data=data_ba)


def hfp_verify_voice_tag(voice_tag=""):
    logging.debug("%s", hfp_verify_voice_tag.__name__)
    iutctl = get_iut()

    data_ba = voice_tag.encode()

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_voice_tag'], data=data_ba)


def hfp_ag_speaker_volume_send(volume):
    logging.debug("%s", hfp_ag_speaker_volume_send.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', volume))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_speaker_volume_send'], data=data_ba)


def hfp_ag_mic_volume_send(volume):
    logging.debug("%s", hfp_ag_mic_volume_send.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', volume))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_mic_volume_send'], data=data_ba)


def hfp_hf_speaker_volume_send(volume):
    logging.debug("%s", hfp_hf_speaker_volume_send.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', volume))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_speaker_volume_send'], data=data_ba)


def hfp_hf_mic_volume_send(volume):
    logging.debug("%s", hfp_hf_mic_volume_send.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', volume))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_mic_volume_send'], data=data_ba)


def hfp_ag_enable_audio():
    logging.debug("%s", hfp_ag_enable_audio.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_enable_audio'], data=bytearray())


def hfp_hf_enable_audio():
    logging.debug("%s", hfp_hf_enable_audio.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_enable_audio'], data=bytearray())


def hfp_disable_audio():
    logging.debug("%s", hfp_disable_audio.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['disable_audio'], data=bytearray())


def hfp_ag_enable_network():
    logging.debug("%s", hfp_ag_enable_network.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_enable_network'], data=bytearray())


def hfp_ag_disable_network():
    logging.debug("%s", hfp_ag_disable_network.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_disable_network'], data=bytearray())


def hfp_ag_make_roam_active():
    logging.debug("%s", hfp_ag_make_roam_active.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_make_roam_active'], data=bytearray())


def hfp_ag_make_roam_inactive():
    logging.debug("%s", hfp_ag_make_roam_inactive.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_make_roam_inactive'], data=bytearray())


def hfp_ag_make_battery_not_full_charged():
    logging.debug("%s", hfp_ag_make_battery_not_full_charged.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_make_battery_not_full_charged'], data=bytearray())


def hfp_ag_make_battery_full_charged():
    logging.debug("%s", hfp_ag_make_battery_full_charged.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_make_battery_full_charged'], data=bytearray())


def hfp_verify_battery_charged():
    logging.debug("%s", hfp_verify_battery_charged.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_battery_charged'], data=bytearray())


def hfp_verify_battery_discharged():
    logging.debug("%s", hfp_verify_battery_discharged.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_battery_discharged'], data=bytearray())


def hfp_speaker_volume_verify(volume):
    logging.debug("%s", hfp_speaker_volume_verify.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', volume))

    iutctl.btp_socket.send_wait_rsp(*HFP['speaker_volume_verify'], data=data_ba)


def hfp_mic_volume_verify(volume):
    logging.debug("%s", hfp_mic_volume_verify.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', volume))

    iutctl.btp_socket.send_wait_rsp(*HFP['mic_volume_verify'], data=data_ba)


def hfp_ag_register():
    logging.debug("%s", hfp_ag_register.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_register'], data=bytearray())


def hfp_hf_register():
    logging.debug("%s", hfp_hf_register.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_register'], data=bytearray())


def hfp_verify_roam_active():
    logging.debug("%s", hfp_verify_roam_active.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_roam_active'], data=bytearray())


def hfp_hf_query_network_operator():
    logging.debug("%s", hfp_hf_query_network_operator.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_query_network_operator'], data=bytearray())


def hfp_ag_vre_text(type, operation, status=1, id=2, delay=0):
    logging.debug("%s", hfp_ag_vre_text.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', status))
    data_ba.extend(struct.pack('H', id))
    data_ba.extend(struct.pack('B', type))
    data_ba.extend(struct.pack('B', operation))
    data_ba.extend(struct.pack('I', delay))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_vre_text'], data=data_ba)


def hfp_hf_dtmf_code_send(dtmf_code):
    logging.debug("%s", hfp_hf_dtmf_code_send.__name__)
    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(struct.pack('B', dtmf_code))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_dtmf_code_send'], data=data_ba)


def hfp_verify_roam_inactive():
    logging.debug("%s", hfp_verify_roam_inactive.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['verify_roam_inactive'], data=bytearray())


def hfp_hf_private_consultation_mode(index):
    logging.debug("%s", hfp_hf_private_consultation_mode.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', index - 1))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_private_consultation_mode'], data=data_ba)


def hfp_hf_release_specified_call(index):
    logging.debug("%s", hfp_hf_release_specified_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', index - 1))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_release_specified_call'], data=bytearray())


def hfp_ag_set_ongoing_calls(number, type, status, dir, all=False):
    logging.debug("%s", hfp_ag_set_ongoing_calls.__name__)

    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(struct.pack('B', type))
    data_ba.extend(struct.pack('B', status))
    data_ba.extend(struct.pack('B', dir))
    if all:
        data_ba.extend(struct.pack('B', 1))
    else:
        data_ba.extend(struct.pack('B', 0))

    data_ba.extend(struct.pack('B', len(number)))
    data_ba.extend(number.encode('utf-8'))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_set_ongoing_calls'], data=data_ba)


def hfp_ag_hold_incoming():
    logging.debug("%s", hfp_ag_hold_incoming.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_hold_incoming'], data=bytearray())


def hfp_ag_last_dialed_number(number, type):
    logging.debug("%s", hfp_ag_last_dialed_number.__name__)

    iutctl = get_iut()

    data_ba = bytearray()
    data_ba.extend(struct.pack('B', type))
    data_ba.extend(struct.pack('B', len(number)))
    data_ba.extend(number.encode('utf-8'))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_last_dialed_number'], data=data_ba)


def hfp_control(index, value=0):
    logging.debug("%s %r %r", hfp_control.__name__, index, value)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', index))
    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['control'], data=data_ba)


def hfp_ag_answer_call(value=0):
    logging.debug("%s", hfp_ag_answer_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_answer_call'], data=data_ba)


def hfp_ag_reject_call(value=0):
    logging.debug("%s", hfp_ag_reject_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_reject_call'], data=data_ba)


def hfp_hf_reject_call(value=0):
    logging.debug("%s", hfp_hf_reject_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_reject_call'], data=data_ba)


def hfp_ag_end_call(value=0):
    logging.debug("%s", hfp_ag_end_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_end_call'], data=data_ba)


def hfp_hf_end_call(value=0):
    logging.debug("%s", hfp_hf_end_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_end_call'], data=data_ba)


def hfp_ag_disable_inband():
    logging.debug("%s", hfp_ag_disable_inband.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_disable_inband'], data=bytearray())


def hfp_ag_enable_inband():
    logging.debug("%s", hfp_ag_enable_inband.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_enable_inband'], data=bytearray())


def hfp_ag_twc_call():
    logging.debug("%s", hfp_ag_twc_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_twc_call'], data=bytearray())


def hfp_ag_enable_vr():
    logging.debug("%s", hfp_ag_enable_vr.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_enable_vr'], data=bytearray())


def hfp_hf_enable_vr():
    logging.debug("%s", hfp_hf_enable_vr.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_enable_vr'], data=bytearray())


def hfp_ag_send_bcc():
    logging.debug("%s", hfp_ag_send_bcc.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_send_bcc'], data=bytearray())


def hfp_hf_send_bcc():
    logging.debug("%s", hfp_hf_send_bcc.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_send_bcc'], data=bytearray())


def hfp_ag_send_bcc_msbc():
    logging.debug("%s", hfp_ag_send_bcc_msbc.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_send_bcc_msbc'], data=bytearray())


def hfp_hf_send_bcc_msbc():
    logging.debug("%s", hfp_hf_send_bcc_msbc.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_send_bcc_msbc'], data=bytearray())


def hfp_ag_send_bcc_swb():
    logging.debug("%s", hfp_ag_send_bcc_swb.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_send_bcc_swb'], data=bytearray())


def hfp_hf_send_bcc_swb():
    logging.debug("%s", hfp_hf_send_bcc_swb.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_send_bcc_swb'], data=bytearray())


def hfp_cls_mem_call_list():
    logging.debug("%s", hfp_cls_mem_call_list.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['cls_mem_call_list'], data=bytearray())


def hfp_hf_accept_held_call(value=0):
    logging.debug("%s", hfp_hf_accept_held_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_accept_held_call'], data=data_ba)


def hfp_hf_held_active_call():
    logging.debug("%s", hfp_hf_held_active_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_held_active_call'], data=bytearray())


def hfp_ag_accept_incoming_held_call(value=0):
    logging.debug("%s", hfp_ag_accept_incoming_held_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_accept_incoming_held_call'], data=data_ba)


def hfp_hf_accept_incoming_held_call(value=0):
    logging.debug("%s", hfp_hf_accept_incoming_held_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_accept_incoming_held_call'], data=data_ba)


def hfp_ag_reject_held_call(value=0):
    logging.debug("%s", hfp_ag_reject_held_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_reject_held_call'], data=data_ba)


def hfp_hf_reject_held_call(value=0):
    logging.debug("%s", hfp_hf_reject_held_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_reject_held_call'], data=data_ba)


def hfp_ag_out_call():
    logging.debug("%s", hfp_ag_out_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_out_call'], data=bytearray())


def hfp_hf_out_call():
    logging.debug("%s", hfp_hf_out_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_out_call'], data=bytearray())


def hfp_hf_enable_clip():
    logging.debug("%s", hfp_hf_enable_clip.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_enable_clip'], data=bytearray())


def hfp_hf_send_iia():
    logging.debug("%s", hfp_hf_send_iia.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_send_iia'], data=bytearray())


def hfp_hf_enable_sub_number():
    logging.debug("%s", hfp_hf_enable_sub_number.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_enable_sub_number'], data=bytearray())


def hfp_hf_out_mem_call():
    logging.debug("%s", hfp_hf_out_mem_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_out_mem_call'], data=bytearray())


def hfp_hf_out_mem_outofrange_call():
    logging.debug("%s", hfp_hf_out_mem_outofrange_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_out_mem_outofrange_call'], data=bytearray())


def hfp_hf_ec_nr_disable():
    logging.debug("%s", hfp_hf_ec_nr_disable.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_ec_nr_disable'], data=bytearray())


def hfp_ag_disable_vr():
    logging.debug("%s", hfp_ag_disable_vr.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_diasble_vr'], data=bytearray())


def hfp_hf_disable_vr():
    logging.debug("%s", hfp_hf_disable_vr.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_disable_vr'], data=bytearray())


def hfp_hf_enable_binp():
    logging.debug("%s", hfp_hf_enable_binp.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_enable_binp'], data=bytearray())


def hfp_ag_join_conversation_call():
    logging.debug("%s", hfp_ag_join_conversation_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_join_conversation_call'], data=bytearray())


def hfp_hf_join_conversation_call():
    logging.debug("%s", hfp_hf_join_conversation_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_join_conversation_call'], data=bytearray())


def hfp_hf_explicit_transfer_call():
    logging.debug("%s", hfp_hf_explicit_transfer_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_explicit_transfer_call'], )


def hfp_hf_out_last_call():
    logging.debug("%s", hfp_hf_out_last_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_out_last_call'], data=bytearray())


def hfp_hf_disable_active_call():
    logging.debug("%s", hfp_hf_disable_active_call.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_disable_active_call'], data=bytearray())


def hfp_hf_end_second_call(value=0):
    logging.debug("%s", hfp_hf_end_second_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_end_second_call'], data=data_ba)


def hfp_mute_inband_ring():
    logging.debug("%s", hfp_mute_inband_ring.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['mute_inband_ring'], data=bytearray())


def hfp_ag_remote_reject(value=0):
    logging.debug("%s", hfp_ag_remote_reject.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_remote_reject'], data=data_ba)


def hfp_ag_remote_ring(value=0):
    logging.debug("%s", hfp_ag_remote_ring.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_remote_ring'], data=data_ba)


def hfp_ag_hold(value=0):
    logging.debug("%s", hfp_ag_hold.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_hold'], data=data_ba)


def hfp_ag_retrieve(value=0):
    logging.debug("%s", hfp_ag_retrieve.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_retrieve'], data=data_ba)


def hfp_ag_ver_state(value=0):
    logging.debug("%s", hfp_ag_ver_state.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_ver_state'], data=data_ba)


def hfp_hf_indicator_value(flag, value=0):
    logging.debug("%s", hfp_hf_indicator_value.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flag))
    data_ba.extend(struct.pack('B', value))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_indicator_value'], data=data_ba)


def hfp_hf_ready_accept_audio():
    logging.debug("%s", hfp_hf_ready_accept_audio.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_ready_accept_audio'], data=bytearray())


def hfp_hf_impair_signal():
    logging.debug("%s", hfp_hf_impair_signal.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_impair_signal'], data=bytearray())


def hfp_ag_set_last_num():
    logging.debug("%s", hfp_ag_set_last_num.__name__)
    iutctl = get_iut()

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_set_last_num'], data=bytearray())


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
