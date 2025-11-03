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

import logging
import re

from autopts.pybtp.types import WIDParams, IOCap
from autopts.pybtp import btp, defs
from autopts.wid import generic_wid_hdl
from autopts.ptsprojects.stack import get_stack
from time import sleep

log = logging.debug


def hfp_wid_hdl(wid, description, test_case_name):
    log(f'{hfp_wid_hdl.__name__}, {wid}, {description}, {test_case_name}')
    return generic_wid_hdl(wid, description, test_case_name, [__name__])


# wid handlers section begin
def hdl_wid_0(params: WIDParams):
    stack = get_stack()
    # if params.test_case_name.find('HFP/HF/SLC/BV-0') >= 0:
    #     return True
    # if params.test_case_name in ['HFP/HF/ACC/BV-10-C']:
    #     return True
    btp.gap_set_conn()
    btp.gap_set_gendiscov()

    if params.test_case_name in ["HFP/AG/SLC/BV-01-C", "HFP/AG/SLC/BV-02-C", "HFP/AG/SLC/BV-04-C", "HFP/AG/SLC/BV-05-C",
                                 "HFP/AG/SLC/BV-07-C"]:
        btp.hfp_ag_register()
        return True
    if params.test_case_name in ["HFP/HF/SLC/BV-01-C"]:
        return True
    if params.test_case_name in ["HFP/HF/SLC/BI-01-C", "HFP/HF/SLC/BV-11-C"]:
        btp.hfp_hf_register()
        return True

    if params.test_case_name.find('HFP/AG/') >= 0:
        # btp.hfp_ag_discoverable()
        if not stack.gap.is_connected():
            btp.gap_conn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
            btp.gap_wait_for_connection()

        btp.gap_pair(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
        if params.test_case_name.find('HFP/AG/SLC/BV-0') >= 0:
            return True
        if params.test_case_name.find('HFP/AG/OOR/BV-02-C') >= 0:
            return True

        btp.hfp_enable_slc(None, 1)
    # elif params.test_case_name.find('HFP/HF/') >= 0:
    # btp.hfp_make_discoverable()
    return True


def hdl_wid_1(params: WIDParams):
    """
    Click Ok, then initiate a service level connection from the Implementation Under Test (IUT) to the PTS.
    """
    log("hdl_wid_1: Initiate a service level connection")

    stack = get_stack()
    stack.gap.set_passkey(None)

    if not stack.gap.is_connected():
        btp.gap_conn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
        btp.gap_wait_for_connection()
        if not stack.gap.is_connected():
            return False

    if params.test_case_name in ['HFP/AG/RHH/BV-04-C', 'HFP/AG/RHH/BV-05-C', 'HFP/AG/RHH/BV-06-C', 'HFP/AG/RHH/BV-07-C',
                                 'HFP/AG/RHH/BV-08-C']:
        btp.hfp_ag_enable_call(defs.BTP_HFP_AG_ENABLE_CALL_FLAGS_INCOMING_HELD)

    btp.gap_pair(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)

    if params.test_case_name in ['HFP/AG/OCL/BV-01-C']:
        btp.hfp_ag_register()
        sleep(3)

    if params.test_case_name.find('HFP/AG/') >= 0:
        if not stack.hfp.is_sco_connected():
            btp.hfp_enable_slc(None, 1, 1)
    else:
        btp.hfp_enable_slc(None, 1, 0)
    return True


def hdl_wid_2(_: WIDParams):
    """
    Click Ok, then disable the service level connection using the Implementation Under Test (IUT).
    """
    log("hdl_wid_2: Disable service level connection")

    btp.hfp_disable_slc()
    return True


def hdl_wid_3(params: WIDParams):
    """
    Click Ok, then initiate an audio connection (SCO) from the Implementation Under Test (IUT) to the PTS.
    """
    sleep(3)
    if params.test_case_name in ['HFP/HF/ATA/BV-02-C'] or params.test_case_name in [
        'HFP/HF/ATH/BV-03-C'] or params.test_case_name in ['HFP/HF/ATH/BV-04-C'] or params.test_case_name in [
        'HFP/HF/ATH/BV-09-C']:
        return True
    btp.hfp_control(defs.HFP_SEND_BCC)
    return True


def hdl_wid_4(_: WIDParams):
    """
    Click Ok, then close the audio connection (SCO)
    between the Implementation Under Test (IUT) and the PTS. Do
    not close the serivice level connection (SLC) or power-off the IUT.
    """
    btp.hfp_disable_audio()
    return True


def hdl_wid_5(params: WIDParams):
    """
    Place a call from an external line to the Implementation Under Test (IUT).  When the call is active, click Ok.
    """
    if params.test_case_name in ['HFP/HF/ATH/BV-03-C']:
        btp.gap_set_conn()
        btp.gap_set_gendiscov()
        # btp.hfp_ag_make_discoverable()
        btp.hfp_enable_slc(None, 1)
    sleep(3)
    if params.test_case_name in ['HFP/AG/TWC/BV-04-C']:
        btp.hfp_control(defs.HFP_TWC_CALL)
        return True
    btp.hfp_ag_enable_call()
    return True


def hdl_wid_7(params: WIDParams):
    """
    Click Ok, then answer the incoming call on the external terminal.
    """
    if params.test_case_name in ['HFP/AG/OCL/BV-01-C', 'HFP/AG/OCM/BV-01-C', 'HFP/AG/OCN/BV-01-C']:
        btp.hfp_control(defs.HFP_REMOTE_RING)
    btp.hfp_control(defs.HFP_AG_ANSWER_CALL)
    return True


def hdl_wid_8(params: WIDParams):
    """
    Click Ok, then answer the incoming call on the Implementation Under Test (IUT).
    """
    if params.test_case_name.find('HFP/HF/') >= 0:
        btp.hfp_hf_answer_call()
    else:
        btp.hfp_control(defs.HFP_AG_ANSWER_CALL)
    return True


def hdl_wid_9(params: WIDParams):
    """
    Click Ok, then answer the incoming call using the Implementation Under Test (IUT).
    """
    if params.test_case_name in ['HFP/HF/ICA/BV-01-C']:
        sleep(1)
    btp.hfp_hf_answer_call()
    return True


def hdl_wid_10(_: WIDParams):
    """
    Click Ok, then reject the incoming call using the Implemention Under Test (IUT).
    """
    sleep(10)
    btp.hfp_control(defs.HFP_REJECT_CALL)
    return True


def hdl_wid_11(_: WIDParams):
    """
    Place the Implementation Under Test (IUT) in a mode that will allow an outgoing call initiated by the PTS, and click Ok.
    """
    return True


def hdl_wid_12(params: WIDParams):
    """
    Click Ok, then place a call from an external line to the Implementation Under Test (IUT).
    Do not answer the call unless prompted to do so.
    """
    sleep(3)
    if params.test_case_name in ['HFP/AG/ACC/BV-09-C']:
        sleep(3)
    log("hdl_wid_12: External call to IUT")
    btp.hfp_ag_enable_call()
    return True


def hdl_wid_13(params: WIDParams):
    """
    Click Ok, then place a call from an external line to the Implementation Under Test (IUT).
    Do not answer the call unless prompted to do so.
    """
    sleep(3)
    if params.test_case_name in ['HFP/AG/ECC/BV-01-C', 'HFP/AG/ECC/BV-02-C',
                                 'HFP/AG/ECS/BV-03-C', 'HFP/AG/TCA/BV-05-C',
                                 'HFP/AG/TWC/BV-01-C', 'HFP/AG/TWC/BV-03-C',
                                 'HFP/AG/TWC/BV-04-C']:
        btp.hfp_control(defs.HFP_TWC_CALL)
        return True
    btp.hfp_ag_enable_call()
    return True


def hdl_wid_14(params: WIDParams):
    """
    Click Ok, then end the call using the external terminal.
    """
    sleep(10)
    btp.hfp_ag_disable_call_external()
    return True


def hdl_wid_15(_: WIDParams):
    """
    Click Ok, then end the call using the external terminal.
    """
    log("hdl_wid_15: End the call using external terminal")
    sleep(10)
    # End the call by disabling the call on AG side
    btp.hfp_ag_disable_call_external()

    return True


def hdl_wid_18(_: WIDParams):
    """
    Clear the call history on  the Implementation Under Test (IUT) such that there are zero records of any numbers dialed, then click Ok.
    """
    return True


def hdl_wid_21(_: WIDParams):
    """
    Click Ok, then place an outgoing call from the Implementation Under Test (IUT) using an enterted phone number.
    """
    sleep(10)
    btp.hfp_control(defs.HFP_OUT_CALL)
    return True


def hdl_wid_22(_: WIDParams):
    """
    Click Ok, then place an outgoing call from the Implementation Under Test (IUT) by entering the memory index.
    """
    sleep(10)
    btp.hfp_control(defs.HFP_OUT_MEM_CALL)
    return True


def hdl_wid_23(_: WIDParams):
    """
    Click Ok, then attempt to place an outgoing call from the Implementation Under Test (IUT)
    by entering a memory index which does not equal the TSPX_phone_number_memory.
    """
    sleep(10)
    btp.hfp_control(defs.HFP_OUT_MEM_OUTOFRANGE_CALL)
    return True


def hdl_wid_24(_: WIDParams):
    """
    description: Click Ok, then place an outgoing call from the Implementation Under Test (IUT) by entering the memory index.  For further clarification please see the HFP 1.5 Specification.
    """
    sleep(10)
    btp.hfp_control(defs.HFP_OUT_LAST_CALL)
    return True


def hdl_wid_25(_: WIDParams):
    """
    Click Ok, then end the call process from the Implementation Under Test (IUT)
    """
    btp.hfp_control(defs.HFP_END_CALL)
    return True


def hdl_wid_27(_: WIDParams):
    """
    Click Ok, then end the 2nd call using the Implementation Under Test (IUT).
    """
    btp.hfp_control(defs.HFP_END_SECOND_CALL)
    return True


def hdl_wid_28(params: WIDParams):
    """
    Verify that the call is disabled on the Implementation Under Test (IUT) and then click Ok.
    """
    stack = get_stack()
    if stack.hfp.is_sco_connected():
        return False
    else:
        return True


def hdl_wid_29(_: WIDParams):
    """
    Click Ok, then make the held call active which will result in the active call being placed on hold.
    """
    btp.hfp_control(defs.HFP_DISABLE_ACTIVE_CALL)
    have_active_call = 1
    return True


def hdl_wid_30(_: WIDParams):
    """
    Click Ok, then make the held call active which will result in the active call being placed on hold.
    """
    btp.hfp_control(defs.HFP_HELD_ACTIVE_CALL)
    return True


def hdl_wid_31(_: WIDParams):
    """
    Click Ok, then add the held call to the conversation.
    """
    btp.hfp_control(defs.HFP_JOIN_CONVERSATION_CALL)
    return True


def hdl_wid_32(_: WIDParams):
    """
    Click Ok, then join the held and active making one conversation and disconnect the Implementation Under Test (IUT) from the said conversation.,
    """
    btp.hfp_control(defs.HFP_EXPLICIT_TRANSFER_CALL)
    return True


def hdl_wid_33(_: WIDParams):
    """
    Click Ok, then disable the in-band ringtone using the Implementation Under Test (IUT).
    """
    log("hdl_wid_33: Disable in-band ringtone on IUT")

    sleep(5)
    btp.hfp_control(defs.HFP_DISABLE_IN_BAND)

    return True


def hdl_wid_34(_: WIDParams):
    """
    Click Ok, then enable the in-band ringtone using the Implementation Under Test (IUT)
    """
    btp.hfp_control(defs.HFP_ENABLE_INBAND_RING)
    return True


def hdl_wid_35(params: WIDParams):
    """
    Verify the presence of an audio connection, then click Ok.
    """
    log("hdl_wid_35: Verify presence of audio connection")

    sleep(5)
    if params.test_case_name in ['HFP/HF/OCM/BV-01-C', 'HFP/HF/ICA/BV-07-C']:
        btp.hfp_disable_slc()
    # stack = get_stack()
    return True
    # if stack.hfp.is_sco_connected():
    #     return True
    # else:
    #     stack.hfp.wait_sco_connected_ev(10)
    #     if not stack.hfp.is_sco_connected():
    #         # if keep waiting here, it blocks the doggle to reply the SCO HCI_Connection_Request HCI cmd.
    #         if params.test_case_name in ['HFP/AG/ACS/BV-10-C'] or params.test_case_name in [
    #             'HFP/AG/ACC/BV-23-C'] or params.test_case_name in ['HFP/AG/ACC/BV-25-C']:
    #             stack.hfp.need_check_sco_connection = True
    #             return True
    #         elif params.test_case_name in ['HFP/AG/OOR/BV-01-C'] or params.test_case_name in ['HFP/AG/ATH/BV-03-C']:
    #             stack.hfp.need_check_sco_connection = True
    #             return True
    #         elif params.test_case_name in ['HFP/AG/TCA/BV-01-C'] or params.test_case_name in ['HFP/AG/ATH/BV-03-C']:
    #             stack.hfp.need_check_sco_connection = True
    #             return True
    #         elif params.test_case_name in ['HFP/HF/TDC/BV-01-C']:
    #             stack.hfp.need_check_sco_connection = True
    #             return True
    #         elif params.test_case_name in ['HFP/HF/ATH/BV-06-C']:
    #             stack.hfp.need_check_sco_connection = True
    #             return True
    #         elif params.test_case_name in ['HFP/HF/RSV/BV-03-C']:
    #             stack.hfp.need_check_sco_connection = True
    #             return True
    #         elif params.test_case_name in ['HFP/HF/ECC/BV-01-C']:
    #             stack.hfp.need_check_sco_connection = True
    #             return True
    #         elif params.test_case_name in ['HFP/AG/ICA/BV-02-C']:
    #             stack.hfp.need_check_sco_connection = True
    #             return True
    #         else:
    #             return False
    #     return True


def hdl_wid_36(_: WIDParams):
    """
    Verify the audio is returned to the 1st call and click Ok. Resume action my be needed.  If the audio is not present in the 1st call, click Cancel.
    """
    return True


def hdl_wid_37(_: WIDParams):
    """
    Verify the audio is returned to the 2nd call and then click Ok.  Resume action may be needed.  If the audio is not returned to the 2nd call, click Cancel.
    """
    return True


def hdl_wid_38(_: WIDParams):
    """
    Verify the audio is returned to the 2nd call and then click Ok.  Resume action may be needed.  If the audio is not returned to the 2nd call, click Cancel.
    """
    return True


def hdl_wid_39(_: WIDParams):
    """
    Verify the absence of an audio connection (SCO), then click Ok.
    """

    stack = get_stack()
    if stack.hfp.is_sco_connected():
        return False
    else:
        return True


def hdl_wid_41(_: WIDParams):
    """
    Click Ok, then disable the network using the Implementation Under Test (IUT) by performing one of the below actions:
    1. If the IUT is an Audio Gateway (AG), turn the network using the UI.
    2. Place the PTS and IUT in an RF shield box. Once the network is disabled the PTS will send an alert to your machine confirming the network connection was lost.
    """
    log("hdl_wid_41: Disable network on IUT")
    btp.hfp_disable_network()
    return True


def hdl_wid_42(_: WIDParams):
    """
    Click Ok, then enable the network using the Implementation Under Test (IUT).
    """
    log("hdl_wid_42: Enable network on IUT")
    btp.hfp_enable_network()
    return True


def hdl_wid_43(params: WIDParams):
    """
    Send the DTMF code %s, then click Ok
    """
    pattern = re.compile(r"DTMF\scode\s([0-9*#]+)")
    data = pattern.findall(params.description)
    if not data:
        logging.error("%s parsing error", hdl_wid_43.__name__)
        return False

    dtmf_code = data[0]
    btp.hfp_dtmf_code_send(ord(dtmf_code[0]))
    return True


def hdl_wid_45(_: WIDParams):
    """
    Using the Implemenation Under Test (IUT), disable  EC/NR, then click Ok.
    """
    sleep(10)
    btp.hfp_control(defs.HFP_EC_NR_DISABLE)
    return True


def hdl_wid_46(_: WIDParams):
    """
    Verify that EC and NR functionality is disabled, then click Ok..
    """
    sleep(10)
    btp.hfp_verify(defs.HFP_VERIFY_EC_NR_DISABLED)
    return True


def hdl_wid_47(params: WIDParams):
    """
    Mute the in-band ringtone on the Implementation Under Test (IUT) and then click OK.
    """
    btp.hfp_control(defs.HFP_MUTE_INBAND_RING)
    return True


def hdl_wid_48(_: WIDParams):
    """
    Verify that the in-band ringtone is not audible , then click Ok.
    """
    sleep(10)
    btp.hfp_verify(defs.HFP_VERIFY_INBAND_RING_MUTING)
    return True


def hdl_wid_49(params: WIDParams):
    """
    Verify that the in-band ringtone is audible, then click Ok.
    """
    sleep(10)
    # if params.test_case_name not in ['HFP/HF/ICA/BV-02-C']:
    #     stack = get_stack()
    #     if not stack.hfp.is_sco_connected():
    #         stack.hfp.wait_sco_connected_ev(2)
    #         if not stack.hfp.is_sco_connected():
    #             return False
    btp.hfp_verify(defs.HFP_VERIFY_INBAND_RING)
    return True


def hdl_wid_50(_: WIDParams):
    """
    Verify that the Implementation Under Test (IUT) is generating a local alert, then click Ok.
    """
    sleep(10)
    btp.hfp_verify(defs.HFP_VERIFY_IUT_ALERTING)
    return True


def hdl_wid_51(_: WIDParams):
    """
    Verify that the Implementation Under Test (IUT) is not generating a local alert
    """
    btp.hfp_verify(defs.HFP_VERIFY_IUT_NOT_ALERTING)
    return True


def hdl_wid_53(params: WIDParams):
    """
    Verify that the signal reported on the Implementation Under Test (IUT) is proportional to the value (out of 5), then click Ok.
    """
    log(f"hdl_wid_53: Verify signal strength indication on IUT: {params.description[-1]}")

    sleep(1)
    if params.description[-1] == '5':
        if params.test_case_name in ['HFP/AG/PSI/BV-01-C']:
            btp.hfp_signal_strength_send(5)
        btp.hfp_signal_strength_verify(5)
    elif params.description[-1] == '4':
        if params.test_case_name in ['HFP/AG/PSI/BV-01-C']:
            btp.hfp_signal_strength_send(4)
        btp.hfp_signal_strength_verify(4)
    elif params.description[-1] == '3':
        if params.test_case_name in ['HFP/AG/PSI/BV-01-C']:
            btp.hfp_signal_strength_send(3)
        btp.hfp_signal_strength_verify(3)
    elif params.description[-1] == '2':
        if params.test_case_name in ['HFP/AG/PSI/BV-01-C']:
            btp.hfp_signal_strength_send(2)
        btp.hfp_signal_strength_verify(2)
    elif params.description[-1] == '1':
        btp.hfp_signal_strength_verify(1)

    return True


def hdl_wid_54(params: WIDParams):
    """
        Verify that the Implementation Under Test (IUT) reports the roam status as active, then click Ok.
    """
    sleep(10)
    btp.hfp_verify_roam_active()

    return True


def hdl_wid_55(params: WIDParams):
    """
    Verify that the Implemenatation Under Test (IUT) reports the roam status as inactive, then click Ok.
    """
    sleep(10)
    btp.hfp_verify_roam_inactive()

    return True


def hdl_wid_56(_: WIDParams):
    """
    Enable roaming on the Implementation Under Test (IUT), then click Ok.
    """
    log("hdl_wid_56: Enable roaming on IUT")

    btp.hfp_make_roam_active()

    return True


def hdl_wid_57(_: WIDParams):
    """
    Disable roaming on the Implementation Under Test (IUT), then click Ok.
    """
    log("hdl_wid_56: Disable roaming on IUT")

    btp.hfp_make_roam_inactive()

    return True


def hdl_wid_59(params: WIDParams):
    """
    Verify that the Implementation Under Test (IUT) reports the Audio Gateway (AG) battery level as fully charged, then click Ok.
    """
    sleep(10)
    btp.hfp_verify_battery_charged()

    return True


def hdl_wid_60(_: WIDParams):
    """
    Click Ok, then manipulate the Implementation Under Test (IUT) so that the battery is fully charged.
    """
    log("hdl_wid_60: Set battery level to fully charged")

    sleep(10)
    btp.hfp_make_battery_full_charged()

    return True


def hdl_wid_61(_: WIDParams):
    """
    Manipulate the Implementation Under Test (IUT) so that the battery level is not fully charged, then click Ok.
    """
    log("hdl_wid_61: Set battery level to not fully charged")

    sleep(10)
    btp.hfp_make_battery_not_full_charged()

    return True


def hdl_wid_62(params: WIDParams):
    """
    Verify the following information matches the network operator reported on the Implementation Under Test (IUT), then click Ok
    """
    if params.test_case_name in ['HFP/AG/PSI/BV-04-C']:
        return True
    sleep(10)
    keywork = "Ok:"
    start_idx = params.description.find(keywork) + len(keywork)
    result = params.description[start_idx:].strip()

    btp.hfp_verify_network_operator(result)

    return True


def hdl_wid_63(_: WIDParams):
    """
    Using the Implementation Under Test (IUT), query the network operator, then click Ok.
    """
    btp.hfp_query_network_operator()


def hdl_wid_64(_: WIDParams):
    """
    Using the Implementation Under Test (IUT), query the list of currents calls on the Audio Gateway (AG),
    then click Ok.
    """
    sleep(10)
    btp.hfp_control(defs.HFP_QUERY_LIST_CALL)
    return True


def hdl_wid_67(_: WIDParams):
    """
    Verify that the Implementation Under Test (IUT) interprets both held and active call signals, then click Ok.
    If applicable, verify that the information is correctly displayed on the IUT, then click Ok.
    """
    return True


def hdl_wid_68(params: WIDParams):
    """
    Click Ok, then use the Implementation Under Test (IUT)
    to enable private consultation with the specified call with index 2
    """
    btp.hfp_private_consultation_mode(int(params.description[-1]))
    return True


def hdl_wid_69(params: WIDParams):
    """
    Click OK, then use the Implementation Under Test (IUT) to release the specified call with index 2
    """
    btp.hfp_release_specified_call(int(params.description[-1]))
    return True


def hdl_wid_70(_: WIDParams):
    btp.hfp_speaker_mic_volume_send(0, 7)
    return True


def hdl_wid_71(_: WIDParams):
    btp.hfp_speaker_mic_volume_send(0, 12)
    return True


def hdl_wid_72(_: WIDParams):
    btp.hfp_speaker_mic_volume_send(0, 3)
    return True


def hdl_wid_73(params: WIDParams):
    if params.test_case_name in ['HFP/AG/RSV/BV-01-C']:
        btp.hfp_speaker_mic_volume_send(0, 7)
    else:
        btp.hfp_speaker_mic_volume_send(1, 7)
    return True


def hdl_wid_74(_: WIDParams):
    btp.hfp_speaker_mic_volume_send(1, 12)
    return True


def hdl_wid_75(_: WIDParams):
    btp.hfp_speaker_mic_volume_send(1, 3)
    return True


def hdl_wid_76(params: WIDParams):
    sleep(10)
    btp.hfp_speaker_mic_volume_verify(0, int(re.sub(r'\D', '', params.description[-2:])))
    return True


def hdl_wid_77(params: WIDParams):
    sleep(10)
    btp.hfp_speaker_mic_volume_verify(1, int(re.sub(r'\D', '', params.description[-2:])))
    return True


def hdl_wid_78(_: WIDParams):
    """
    1. TSPX_phone_number - the 1st call
    2. TSPX_second_phone_number - the 2nd call
    """
    btp.hfp_control(defs.HFP_TWC_CALL)
    return True


def hdl_wid_79(_: WIDParams):
    """
    Using the Implementation Under Test (IUT), verify that the following is a valid Audio Gateway (AG) subscriber number, then click Ok.
    """
    btp.hfp_control(defs.HFP_ENABLE_SUB_NUMBER)
    return True


def hdl_wid_81(params: WIDParams):
    """
    Verify that the following number is a vallid number in the Audio Gateway (AG) to use as a voice tag in the Hands Free (HF), then click Ok.NP: +918067064000
    """
    sleep(5)
    btp.hfp_verify_voice_tag(params.description[-13:])
    return True


def hdl_wid_82(_: WIDParams):
    """
    Using the Implementation Under Test (IUT), request a phone number to attach to a voice tag previously entered, then click Ok.
    """
    sleep(10)
    btp.hfp_control(defs.HFP_ENABLE_BINP)
    return True


def hdl_wid_84(_: WIDParams):
    """
    Using the Implementation Under Test (IUT), deactivate voice recognitio
    """
    sleep(10)
    btp.hfp_control(defs.HFP_DISABLE_VR)
    return True


def hdl_wid_85(_: WIDParams):
    """
    Clear the memory indexed by TSPX_phone_number_memory on the AG such that  the memory slot becomes empty, then Click OK.
    """
    btp.hfp_control(defs.HFP_CLS_MEM_CALL_LIST)

    return True


def hdl_wid_86(_: WIDParams):
    """
    Place the Implementation Under Test (IUT) in a state which will allow a request from the PTS to activate voice recognition, then click Ok.
    """
    return True


def hdl_wid_87(_: WIDParams):
    """
    Place the Implementation Under Test (IUT) in a state which will allow the PTS to request a voice tag number, then click Ok.
    """
    return True


def hdl_wid_89(_: WIDParams):
    """
    Enable calling line identification using the HF (send AT+CLIP=1 to the PTS-AG), then Click Ok.
    """
    btp.hfp_control(defs.HFP_ENABLE_CLIP)


def hdl_wid_91(_: WIDParams):
    """
    Delete the pairing with the PTS using the Implementation Under Test (IUT), then click Ok.
    """
    log("hdl_wid_91: Delete pairing with PTS")

    btp.gap_unpair(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
    sleep(3)
    return True


def hdl_wid_94(_: WIDParams):
    """
    Click Ok, then move the PTS and the Implementation Under Test (IUT) out of range of each other.
    """
    log("hdl_wid_94: Move IUT out of range")

    # For automated testing, we can simulate going out of range by:
    # 1. Disconnecting the connection
    # 2. Or setting a flag to simulate out of range condition

    # Disconnect to simulate out of range
    sleep(1)
    btp.hfp_disable_slc()
    btp.gap_disconn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
    sleep(2)

    return True


def hdl_wid_95(params: WIDParams):
    """
    Click Ok, then remove the Implementation Under Test (IUT) and/or the PTS from the RF shield.
    If the out of range method was used, bring the IUT and PTS back within range.
    """
    log("hdl_wid_95: Bring IUT back within range")

    # Simulate bringing devices back within range by re-establishing connection
    sleep(1)

    btp.gap_set_conn()
    btp.gap_set_gendiscov()
    if params.test_case_name.find('HFP/AG/') >= 0:
        btp.hfp_ag_discoverable()
    elif params.test_case_name.find('HFP/HF/') >= 0:
        btp.hfp_ag_discoverable()
    btp.gap_set_io_cap(IOCap.no_input_output)

    return True


def hdl_wid_98(_: WIDParams):
    """
    Click Ok, then close the audio connection (SCO) by one of the following ways:
    1. Close the service level connection (SLC)
    2. Powering off the Implementation Under Test (IUT)
    """
    btp.hfp_disable_slc()

    return True


def hdl_wid_99(_: WIDParams):
    """
    Verify that the +CLCC response(s) received by the Implementation Under Test (IUT) contains the correct call status information, then click Ok.
    """
    return True


def hdl_wid_100(_: WIDParams):
    """
    Set the Implementation Under Test (IUT) in a state that will allow the PTS to initiate a service level disconnection, then click Ok.
    """
    return True


def hdl_wid_101(_: WIDParams):
    """
    Set the Implementation Under Test (IUT) in a state which will allow the PTS to disconnect the audio (SCO), then click Ok.
    """
    return True


def hdl_wid_105(_: WIDParams):
    """
    Set the Implementation Under Test (IUT) in a state that will allow the PTS to initiate a AT+CHLD=1 operation,  then click Ok..
    """
    return True


def hdl_wid_106(_: WIDParams):
    """
    Set the Implementation Under Test (IUT) in a state that will allow the PTS to initiate a AT+CHLD=2 operation,  then click Ok.
    """
    return True


def hdl_wid_108(_: WIDParams):
    """
    Set the Implementation Under Test (IUT) in a state that will allow the PTS to answer the call being set up, then click Ok
    """
    return True


def hdl_wid_109(_: WIDParams):
    """
    Set the Implementation Under Test (IUT) in a state that will allow the PTS to initiate an outgoing call, then click Ok.
    """
    return True


def hdl_wid_110(params: WIDParams):
    """
    Set the Implementation Under Test (IUT) in a state that can receive the following AT Command, then click Ok: AT+CLCC
    """
    if params.test_case_name in ['HFP/AG/VRT/BV-02-C', "HFP/AG/EVR/BV-01-C"]:
        sleep(10)
        btp.hfp_enable_audio()
    return True


def hdl_wid_114(_: WIDParams):
    """
    Set the Implemenation Under Test (IUT) in an appropriate state which will allow the PTS to iniate an audio connection (SCO), then click Ok.
    """
    return True


def hdl_wid_115(params: WIDParams):
    """
    1. Place an outgoing call.
    2. Cancel the outgoing call once the PTS indicates that an outgoing call process has begun.
    """
    # btp.gap_conn(transport=defs.GAP_CONNECT_BREDR)
    if params.test_case_name in ['HFP/HF/TCA/BV-04-C']:
        sleep(10)
    btp.hfp_control(defs.HFP_OUT_CALL)
    return True


def hdl_wid_117(_: WIDParams):
    """
    End the call using the external terminal, then click Ok.
    """
    btp.hfp_control(defs.HFP_END_CALL)
    return True


def hdl_wid_119(_: WIDParams):
    """
    Verify that the last number dialed on the Implementation Under Test (IUT)
    matches the TSPX_Second_phone_number entered in the IXIT settings.
    """
    return True


def hdl_wid_120(_: WIDParams):
    """
    Using the Implementation Under Test (IUT), perform a search for the PTS.  If found, click OK.
    """
    return True


def hdl_wid_121(_: WIDParams):
    """
    make a connection request to the PTS from the Implementation Under Test (IUT).
    """
    stack = get_stack()
    stack.gap.set_passkey(None)

    if not stack.gap.is_connected():
        btp.gap_conn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
        btp.gap_wait_for_connection()

    btp.gap_pair(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
    btp.hfp_enable_slc(None, 1)
    return True


def hdl_wid_122(params: WIDParams):
    """
    Place the Implementation Under Test (IUT) in discoverable mode
    """
    # if params.test_case_name in ['HFP/HF/DIS/BV-01-C']:
    btp.gap_set_conn()
    btp.gap_set_gendiscov()
    btp.hfp_hf_discoverable()

    btp.gap_wait_for_connection()
    # btp.gap_pair(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
    return True


def hdl_wid_123(_: WIDParams):
    """
    accept the pairing and connection requests on the Implementation Under Test (IUT)
    """
    sleep(10)
    return True


def hdl_wid_124(_: WIDParams):
    """
    accept the pairing and connection requests on the Implementation Under Test (IUT)
    """
    return True


def hdl_wid_126(_: WIDParams):
    """
    The PTS will send a call request containing an invalid/out of range memory index from the TSPX_phone_number_memory_invalid_index found in the IXIT settings.
    """
    return True


def hdl_wid_130(_: WIDParams):
    """
     then place the current call on hold and make the incoming/held call active using the Implementation Under Test (IUT).
    """
    btp.hfp_control(defs.HFP_TWC_CALL)
    return True


def hdl_wid_134(_: WIDParams):
    """
     Click Ok, then cancel the call once the PTS indicates to the Implementation Under Test (IUT) that an outgoing call has process has begun.
    """
    return True


def hdl_wid_135(params: WIDParams):
    """
    Place a call from an external line to the Implemenation Under Test (IUT).  Place the call on hold after accepting, then click Ok
    """
    stack = get_stack()
    stack.gap.set_passkey(None)

    if not stack.gap.is_connected():
        btp.gap_conn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
        btp.gap_wait_for_connection()

    btp.gap_pair(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)

    if params.test_case_name.find('HFP/AG/') >= 0:
        if not stack.hfp.is_sco_connected():
            btp.hfp_enable_slc(None, 1, 1)
    else:
        btp.hfp_enable_slc(None, 1, 0)
    return True


def hdl_wid_136(_: WIDParams):
    """
    Place a call from an external line to the Implemenation Under Test (IUT).  Place the call on hold after accepting, then click Ok
    """
    return True


def hdl_wid_139(_: WIDParams):
    """
    Place a call from an external line to the Implemenation Under Test (IUT).  Place the call on hold after accepting, then click Ok
    """
    btp.hfp_control(defs.HFP_ACCEPT_HELD_CALL)
    return True


def hdl_wid_140(_: WIDParams):
    """
     Click Ok, then accept the held incoming call using the Implementation Under Test (IUT)
    """
    btp.hfp_control(defs.HFP_ACCEPT_INCOMING_HELD_CALL)
    return True


def hdl_wid_141(_: WIDParams):
    """
    Click OK, then reject the held incoming call using the Implementation Under Test (IUT)
    """
    btp.hfp_control(defs.HFP_REJECT_HELD_CALL)
    return True


def hdl_wid_142(_: WIDParams):
    """
    Click OK, and then verify that the held call is rejected using the Implementation Under Test (IUT).
    """
    return True


def hdl_wid_143(_: WIDParams):
    """
    Verify that the call is still active and audio (SCO) is returned to the Implementation Under Test (IUT).
    """
    return True


def hdl_wid_144(_: WIDParams):
    """
    Power off the Implementation Under Test (IUT), then click OK
    """

    return True


def hdl_wid_145(_: WIDParams):
    """
    Verify that there is an incoming call on the Implementation Under Test (IUT).
    """

    return True


def hdl_wid_148(_: WIDParams):
    """
    Power on the Implementation Under Test (IUT), then click Ok.
    """

    return True


def hdl_wid_149(_: WIDParams):
    """
    Place the Implementation Under Test (IUT) in non-discoverable mode, then click Ok.
    """
    return True


def hdl_wid_147(_: WIDParams):
    """
    Place an outgoing call using the Implementation Under Test (IUT).  When the call is active click Ok.,
    """
    btp.hfp_control(defs.HFP_OUT_CALL)
    return True


def hdl_wid_146(_: WIDParams):
    """
    When the Implementation Under Test (IUT) alerts the incoming call, click Ok.
    """
    btp.hfp_ag_enable_call()
    return True


def hdl_wid_150(_: WIDParams):
    """
    Click OK, then place a call from an external line to the Implementation Under Test (IUT).  Accept and then place the call on hold using the IUT.
    """
    btp.hfp_ag_enable_call()
    btp.hfp_ag_hold_incoming()
    return True


def hdl_wid_151(_: WIDParams):
    """
    Click OK, then verify on the Implemenatation Under Test (IUT) that the held call is accepted and is active, not on hold.
    """
    return True


def hdl_wid_153(_: WIDParams):
    """
    Verify that at least one of the following statements are true HFP_HF_VRA_BV-03-C.
    """
    return True


def hdl_wid_154(_: WIDParams):
    """
    end all active calls using the external line or the Implementation Under Test (IUT).  Click OK to continue.
    """
    return True


def hdl_wid_155(_: WIDParams):
    """
    Place the Implemenation Under Test (IUT) in a state which will accept an outgoing call set-up request from the PTS, then click OK.
    """
    return True


def hdl_wid_156(_: WIDParams):
    """
    Verify that the Implemenation Under Test (IUT) has called the last dialed number and the bi-directional conversation is available between the external line and the HF.
    """
    return True


def hdl_wid_158(_: WIDParams):
    """
    Place a second call from an external line to the Audio Gateway (AG) or place an outgoing call from the AG, putting the currently active call on hold using the AG.  When the second call is active on the AG, and the first is on hold, click OK.
    """
    return True


def hdl_wid_159(_: WIDParams):
    """
    Click OK, and then send an AT+BIA command to the PTS to activiate or deactiviate any indicator.,
    """
    sleep(10)
    btp.hfp_control(defs.HFP_SEND_IIA)
    return True


def hdl_wid_160(_: WIDParams):
    """
    Impair the signal to the AG so that a reduction in signal strength can be observed. Then, click OK.
    """
    sleep(10)
    btp.hfp_control(defs.HFP_IMPAIR_SIGNAL)
    return True


def hdl_wid_161(_: WIDParams):
    """
    Click OK. Then register AG on a network other than the home network.
    """
    sleep(10)
    btp.hfp_make_roam_active()
    return True


def hdl_wid_162(_: WIDParams):
    """
    Click OK. Then register AG on the home network.
    """
    sleep(10)
    btp.hfp_make_roam_inactive()
    return True


def hdl_wid_163(params: WIDParams):
    """
    Adjust the battery level on the AG to a level that should cause a battery level indication to be sent to HF. Then, click OK.
    """
    if params.test_case_name in ['HFP/AG/IIA/BV-02-C']:
        return True

    btp.hfp_make_battery_full_charged()
    return True


def hdl_wid_164(_: WIDParams):
    """
    Click OK. Then, use a test device to simulate the presence of a control channel of a network, such that the AG is registered.
    """
    btp.hfp_enable_network()
    return True


def hdl_wid_165(_: WIDParams):
    """
    Click OK. Then, disable the control channel, such that the AG is de-registered.
    """
    sleep(1)
    btp.hfp_disable_network()
    return True


def hdl_wid_168(_: WIDParams):
    """
    Click OK, then initiate an audio connection using the Codec Connection Setup procedure.
    """
    sleep(1)
    btp.hfp_control(defs.HFP_SEND_BCC)
    return True


def hdl_wid_169(_: WIDParams):
    """
    Click OK. Then initiate an audio connection with WBS codec using the Codec Connection Setup procedure.
    """
    sleep(1)
    btp.hfp_control(defs.HFP_SEND_BCC_MSBC)
    return True


# def hdl_wid_170(params: WIDParams):
#     """
#     Click OK, then take action so that the network becomes unavailable to the IUT.
#     """
#     if params.test_case_name in ['HFP/AG/TCA/BV-06-C']:
#         btp.hfp_disable_network()
#     btp.hfp_make_sure_ag_registered_on_home_network()
#     return True
#
#
# def hdl_wid_171(_: WIDParams):
#     """
#     Make sure the IUT is registered on home network.
#     """
#     btp.hfp_make_sure_ag_registered_on_home_network()
#     return True


def hdl_wid_172(_: WIDParams):
    """
    Click OK. Then take action to make a change that normally would trigger a change in a non-mandatory indicator, e.g., force the AG to disable the presence of a cellular network.
    """
    btp.hfp_enable_network()
    return True


def hdl_wid_173(_: WIDParams):
    """
    Click OK. Then adjust the battery level on the AG to a level that should cause a battery level indication to be sent to HF.
    """
    btp.hfp_make_battery_full_charged()
    return True


def hdl_wid_175(params: WIDParams):
    """
    Click OK. Then, impair the signal to the AG so that a reduction in signal strength can be observed.
    """
    log("hdl_wid_175: Impair signal to AG for signal strength reduction")
    # , int(re.sub(r'\D', '', params.description[-2:]))
    btp.hfp_control(defs.HFP_IMPAIR_SIGNAL)
    return True


def hdl_wid_177(_: WIDParams):
    """
    Disable the control channel, such that the AG is de-registered. Then, click OK.
    """
    return True


def hdl_wid_187(_: WIDParams):
    """
    Prepare the IUT for a PTS-initiated AT+CHLD=3 operation, where the PTS will request the AG-IUT join the active and held calls into a conference, then Click OK
    """
    # btp.hfp_control(defs.HFP_JOIN_CONVERSATION_CALL)
    return True


def hdl_wid_188(_: WIDParams):
    btp.hfp_speaker_mic_volume_send(1, 15)
    return True


def hdl_wid_189(params: WIDParams):
    if params.test_case_name in ['HFP/AG/RSV/BV-02-C']:
        btp.hfp_speaker_mic_volume_send(0, 0)
    else:
        btp.hfp_speaker_mic_volume_send(1, 0)
    return True


def hdl_wid_190(_: WIDParams):
    btp.hfp_speaker_mic_volume_send(0, 15)
    return True


def hdl_wid_191(_: WIDParams):
    btp.hfp_speaker_mic_volume_send(0, 0)
    return True


def hdl_wid_193(_: WIDParams):
    """
    Perform the action in the IUT(AG) such that itsVoice Recognition audio input is activated.
    """
    return False


def hdl_wid_194(_: WIDParams):
    """
    Perform the action in the IUT(AG) such that itsVoice Recognition wants to send an audio ouput.
    """
    return True


def hdl_wid_197(_: WIDParams):
    """Perform the Test Procedure:
    1. Perform the action such that AG sends +BVRA with a valid 'textType' and any 'textID' value.
    2. Perform the action such that AG sends another +BVRA with a valid 'textType' other than before."""
    btp.hfp_ag_vre_text(1, 1)
    sleep(5)
    btp.hfp_ag_vre_text(2, 1)
    sleep(5)
    btp.hfp_ag_vre_text(3, 2)
    # btp.hfp_ag_vre_text(1, 1, 1, 1)
    # sleep(5)
    # btp.hfp_ag_vre_text(1, 2, 1, 1)
    # sleep(5)
    # btp.hfp_ag_vre_text(1, 3, 2, 1)
    return True


# def hdl_wid_198(_: WIDParams):
#     """Perform the Test Procedure:
#     1. Perform the action such that AG sends +BVRA with a valid 'textType' and any 'textID' value.
#     2. Perform the action such that AG sends another +BVRA with avalid 'textType' other than before,
#     the 'textID' other than before,and the 'textOperation' ID value 1."""
#     btp.hfp_ag_vre_text(2, 2, 2, 2)
#     # sleep(5)
#     btp.hfp_ag_vre_text(1, 1, 1,1)
#     # sleep(5)
#     # btp.hfp_ag_vre_text(3, 3, 2, 3)
#     return True

def hdl_wid_200(_: WIDParams):
    """Perform the Test Procedure:
    1. Perform the action such that AG sends +BVRA with a valid 'textType' and any 'textID' value.
    2. Perform the action such that AG sends another +BVRA with a valid 'textType' and 'textID'
    from before, and the 'textOperation' ID value 3."""
    btp.hfp_ag_vre_text(0, 1)
    sleep(10)
    btp.hfp_ag_vre_text(0, 3)
    return True


def hdl_wid_204(_: WIDParams):
    """Perform the action such that IUT it sends the resultcode +BVRA with 'vrect' value 1,
    a valid 'vrectstate', a valid'textID', the 'textType' ID value 3,
    a valid 'textOperation' ID,
    and the well formatted string with a textual representation of the input sentence."""
    btp.hfp_control(defs.HFP_ENABLE_VR)
    return True


def hdl_wid_219(_: WIDParams):
    """
    Place the Implementation Under Test (IUT) in a state
    which will allow a voice recognition deactivation from PTS, then click Ok.
    """
    btp.hfp_control(defs.HFP_DISABLE_VR)
    return True


def hdl_wid_220(_: WIDParams):
    """
    Is the IUT capable of establishing connection to an unpaired device?
    """
    log("hdl_wid_220: Confirming IUT can connect to unpaired device")

    btp.gap_set_conn()
    btp.gap_set_gendiscov()
    return False


def hdl_wid_222(_: WIDParams):
    """
    Using the Implementation Under Test (IUT), activate voice recognition. Then click OK.
    """
    sleep(5)
    btp.hfp_control(defs.HFP_ENABLE_VR)
    return True


def hdl_wid_223(_: WIDParams):
    """
    Verify IUT ignores unkown or unexpected indication code.
    """
    return True


def hdl_wid_230(_: WIDParams):
    """
    Click OK, then initiate an audio connection using the CVSD Codec and Connection Setup procedure.
    """
    btp.hfp_control(defs.HFP_SEND_BCC)
    return True


def hdl_wid_231(_: WIDParams):
    """
    Click OK, then initiate an audio connection with SWB codec using the Codec Connection Setup procedure.
    """
    sleep(1)
    btp.hfp_control(defs.HFP_SEND_BCC_SWB)
    return True


def hdl_wid_232(_: WIDParams):
    """
    Please confirm IUT received RFU bit field values after Supported Features exchange and ignored the RFU fields.
    """
    return True


def hdl_wid_233(_: WIDParams):
    """
    Please confirm the IUT stops alerting when the incoming call process is interrupted.
    """
    return True


def hdl_wid_246(params: WIDParams):
    """
    Place a call from an external line to the Implementation Under Test (IUT), or putting the current active call on hold.  When the call is active or hold, click Ok.
    """
    if params.test_case_name in ['HFP/AG/ECS/BV-02-C']:
        btp.hfp_ag_enable_call(defs.BTP_HFP_AG_ENABLE_CALL_FLAGS_ON_GOING_CALL)
    else:
        btp.hfp_ag_enable_call()
    return True


def hdl_wid_247(_: WIDParams):
    """
    Verify that the Implementation Under Test (IUT) interprets either held or active call signals, then click Ok.  If applicable, verify that the information is correctly displayed on the IUT, then click Ok.
    """
    return True


def hdl_wid_259(_: WIDParams):
    """
    Please confirm IUT successfully received 'No Home/Roam Network' available indicator.
    Click Ok, if it is received, otherwise click Cancel.
    """
    log("hdl_wid_259: Confirm IUT received No Home/Roam Network available indicator")

    return True


def hdl_wid_260(_: WIDParams):
    """
    Please confirm IUT successfully received 'Home/Roam Network' available indicator.
    Click Ok, if it is received, otherwise click Cancel.
    """
    log("hdl_wid_260: Confirm IUT received Home/Roam Network available indicator")

    # For other test cases, we can add specific handling if needed
    return True


def hdl_wid_561(_: WIDParams):
    """
    Verify that service level connection exists between the lower tester and IUT, then click Ok.
    """
    return True


def hdl_wid_606(_: WIDParams):
    """
    Disable service level connection, then click Ok.
    """
    log("hdl_wid_606: Disable service level connection")

    btp.hfp_disable_slc()
    return True


def hdl_wid_20000(_: WIDParams):
    """
    Please prepare IUT into a connectable mode in BR/EDR.
    Description: Verify that the Implementation Under Test (IUT) can accept GATT connect request from PTS.
    """
    log("hdl_wid_20000: Preparing IUT into connectable mode in BR/EDR")

    # Set device in discoverable and connectable mode
    btp.gap_set_conn()
    btp.gap_set_gendiscov()

    retur
