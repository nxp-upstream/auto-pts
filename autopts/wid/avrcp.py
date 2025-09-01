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
import time

from autopts.ptsprojects.stack import get_stack
from autopts.ptsprojects.testcase import MMI
from autopts.pybtp import btp, defs
from autopts.pybtp.types import (
    WIDParams,
    AVRCPSpecificOperation,
    AVRCPMediaContentNavigationScope,
    AVCTPPassThroughOperation,
    AVRCPNotificationEvents,
    AVRCPVendorUiqueOperationID
)
from autopts.wid import generic_wid_hdl

log = logging.debug


def avrcp_wid_hdl(wid, description, test_case_name):
    log(f'{avrcp_wid_hdl.__name__}, {wid}, {description}, {test_case_name}')
    return generic_wid_hdl(wid, description, test_case_name, [__name__])


# wid handlers section begin
def hdl_wid_1(params: WIDParams):
    # Example WID

    return True

def hdl_wid_12(_: WIDParams):
    """
    description: The IUT should reject the invalid Get Capabilities command sent by PTS.
    """
    return True

def hdl_wid_82(_: WIDParams):
    """
    description: Is the IUT capable of establishing connection to an unpaired device?
    """
    return True

def hdl_wid_83(_: WIDParams):
    """
    description: Delete the link key with PTS on the Implementation Under Test (IUT), and then click OK to continue...
    """
    return True

def hdl_wid_84(_: WIDParams):
    """
    description: Action: Place the IUT in connectable mode.
    """
    stack = btp.get_stack()
    btp.gap_set_conn()
    btp.gap_set_gendiscov()
    btp.gap_adv_ind_on(ad=stack.gap.ad)

    return True

def hdl_wid_85(_: WIDParams):
    """
    description: Using the Implementation Under Test(IUT), initiate ACL Create Connection Request to the PTS.
    """
    btp.gap_conn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
    btp.gap_wait_for_connection()

    return True

def hdl_wid_650(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[SELECT] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_651(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[UP] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_652(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[DOWN] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_653(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[LEFT] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_654(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[RIGHT] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_655(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[RIGHT UP] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_656(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[RIGHT DOWN] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_657(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[LEFT UP] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_658(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[LEFT DOWN] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_659(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[ROOT MENU] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_660(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[SETUP MENU] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_661(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[CONTENTS MENU] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_662(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[FAVORITE MENU] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_663(_: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[EXIT]
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True

def hdl_wid_664(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[0] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_665(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[1] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_666(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[2] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_667(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[3] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_668(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[4] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_669(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[5] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_670(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[6] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_671(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[7] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_672(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[8] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_673(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[9] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_674(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[Dot] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_675(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[Enter] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_676(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[Clear] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_677(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[CHANNEL UP] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_678(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[CHANNEL DOWN] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_679(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[PREVIOUS CHANNEL] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_680(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[SOUND SELECT] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_681(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[INPUT SELECT] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_682(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[DISPLAY INFO] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_683(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[HELP] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True

def hdl_wid_684(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[PAGE UP] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True

def hdl_wid_685(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[PAGE DOWN] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True

def hdl_wid_686(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[POWER] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_687(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[VOLUME UP] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_688(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[VOLUME DOWN] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_689(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[MUTE] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_690(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[PLAY] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_691(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[STOP] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_692(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[PAUSE] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_693(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[RECORD] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_694(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[REWIND] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_695(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[FAST FOWARD] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_696(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[EJECT] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_697(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[FORWARD] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_698(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[BACKWARD] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_699(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[ANGLE] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_700(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[SUBPICTURE] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_701(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[F1] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_702(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[F2] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_703(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[F3] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_704(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[F4] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_705(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[F5] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_706(params: WIDParams):
    """
    description: Press 'YES' if the IUT indicated receiving the[VEMDPR UNIQUE] command.Press 'NO' otherwise.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH_REQ)
    return True


def hdl_wid_739(params: WIDParams):
    """
    description: Press and hold [0] for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_0, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_0, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_740(_: WIDParams):
    """
    description: Press and hold [1] for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_1, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_1, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_741(_: WIDParams):
    """
    description: Press and hold [2] for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_2, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_2, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_742(_: WIDParams):
    """
    description: Press and hold [3] for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_3, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_3, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_743(_: WIDParams):
    """
    description: Press and hold [4] for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_4, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_4, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_744(_: WIDParams):
    """
    description: Press and hold [5] for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_5, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_5, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_745(_: WIDParams):
    """
    description: Press and hold [6] for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_6, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_6, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_746(_: WIDParams):
    """
    description: Press and hold [7] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_7, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_7, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_747(_: WIDParams):
    """
    description: Press and hold [8] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_8, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_8, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_748(_: WIDParams):
    """
    description: Press and hold [9] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_9, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_9, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_749(_: WIDParams):
    """
    description: Press and hold [Dot] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Dot, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Dot, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_750(_: WIDParams):
    """
    description: Press and hold [Enter] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Enter, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Enter, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_751(_: WIDParams):
    """
    description: Press and hold [Clear] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Clear, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Clear, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_755(_: WIDParams):
    """
    description: Press and hold [SOUND SELECT] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Sound_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Sound_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_756(_: WIDParams):
    """
    description: Press and hold [INPUT SELECT] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Input_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Input_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_757(_: WIDParams):
    """
    description: Press and hold [DISPLAY INFO] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Display_Information, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Display_Information, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_758(_: WIDParams):
    """
    description: Press and hold [HELP] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Help, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Help, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_761(_: WIDParams):
    """
    description: Press and hold [POWER] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Power, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Power, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_765(_: WIDParams):
    """
    description: Press and hold [PLAY] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Play, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Play, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_766(_: WIDParams):
    """
    description: Press and hold [STOP] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Stop, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Stop, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_767(_: WIDParams):
    """
    description: Press and hold [PAUSE] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Pause, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Pause, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_768(_: WIDParams):
    """
    description: Press and hold [RECORD] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Record, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Record, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_769(_: WIDParams):
    """
    description: Press and hold [REWIND] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Rewind, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Rewind, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_770(_: WIDParams):
    """
    description: Press and hold [FAST FOWARD] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Fast_Forward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Fast_Forward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_771(_: WIDParams):
    """
    description: Press and hold [EJECT] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Eject, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Eject, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_772(_: WIDParams):
    """
    description: Press and hold [FORWARD] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Forward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Forward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_773(_: WIDParams):
    """
    description: Press and hold [BACKWARD] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Backward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Backward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_774(_: WIDParams):
    """
    description: Press and hold [ANGLE] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Angle, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Angle, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_775(_: WIDParams):
    """
    description: Press and hold [SUBPICTURE] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Subpicture, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Subpicture, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_776(_: WIDParams):
    """
    description: Press and hold [F1] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F1, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F1, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_777(_: WIDParams):
    """
    description: Press and hold [F2] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F2, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F2, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_778(_: WIDParams):
    """
    description: Press and hold [F3] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F3, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F3, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_779(_: WIDParams):
    """
    description: Press and hold [F4] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F4, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F4, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_780(_: WIDParams):
    """
    description: Press and hold [F5] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F5, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F5, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_781(_: WIDParams):
    """
    description: Press and hold [VEMDPR UNIQUE] passthrough for at least three seconds.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Vendor_Unique, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Vendor_Unique, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_800(_: WIDParams):
    """
    description: Send a [SELECT] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Select, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_801(_: WIDParams):
    """
    description: Send a [UP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Up, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Up, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_802(_: WIDParams):
    """
    description: Send a [DOWN] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Down, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Down, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_803(_: WIDParams):
    """
    description: Send a [LEFT] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Left, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Left, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_804(_: WIDParams):
    """
    description: Send a [RIGHT] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Right, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Right, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_805(_: WIDParams):
    """
    description: Send a [RIGHT UP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Right_Up, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Right_Up, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_806(_: WIDParams):
    """
    description: Send a [RIGHT DOWN] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Right_Down, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Right_Down, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_807(_: WIDParams):
    """
    description: Send a [LEFT UP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Left_Up, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Left_Up, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_808(_: WIDParams):
    """
    description: Send a [LEFT DOWN] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Left_Down, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Left_Down, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_809(_: WIDParams):
    """
    description: Send a [ROOT MENU] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Root_Menu, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Root_Menu, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_810(_: WIDParams):
    """
    description: Send a [SETUP MENU] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Setup_Menu, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Setup_Menu, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_811(_: WIDParams):
    """
    description: Send a [CONTENTS MENU] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Contents_Menu, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Contents_Menu, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_812(_: WIDParams):
    """
    description: Send a [FAVORITE MENU] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Favorite_Menu, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Favorite_Menu, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_813(_: WIDParams):
    """
    description: Send a [EXIT] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Exit, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Exit, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_814(_: WIDParams):
    """
    description: Send a [0] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_0, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_0, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_815(_: WIDParams):
    """
    description: Send a [1] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_1, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_1, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_816(_: WIDParams):
    """
    description: Send a [2] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_2, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_2, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_817(_: WIDParams):
    """
    description: Send a [3] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_3, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_3, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_818(_: WIDParams):
    """
    description: Send a [4] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_4, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_4, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_819(_: WIDParams):
    """
    description: Send a [5] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_5, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_5, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_820(_: WIDParams):
    """
    description: Send a [6] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_6, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_6, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_821(_: WIDParams):
    """
    description: Send a [7] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_7, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_7, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_822(_: WIDParams):
    """
    description: Send a [8] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_8, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_8, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_823(_: WIDParams):
    """
    description: Send a [9] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_9, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_9, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_824(_: WIDParams):
    """
    description: Send a [Dot] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Dot, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Dot, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_825(_: WIDParams):
    """
    description: Send a [Enter] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Enter, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Enter, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_826(_: WIDParams):
    """
    description: Send a [Clear] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Clear, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Clear, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_827(_: WIDParams):
    """
    description: Send a [CHANNEL UP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Channel_Up, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Channel_Up, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_828(_: WIDParams):
    """
    description: Send a [CHANNEL DOWN] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Channel_Down, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Channel_Down, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_829(_: WIDParams):
    """
    description: Send a [PREVIOUS CHANNEL] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Previous_Channel, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Previous_Channel, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_830(_: WIDParams):
    """
    description: Send a [SOUND SELECT] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Sound_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Sound_Select, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_831(_: WIDParams):
    """
    description: Send a [INPUT SELECT] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Input_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Input_Select, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True
	
	
def hdl_wid_832(_: WIDParams):
    """
    description: Send a [DISPLAY INFO] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Display_Information, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Display_Information, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_833(_: WIDParams):
    """
    description: Send a [HELP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Help, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Help, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_834(_: WIDParams):
    """
    description: Send a [HELP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Page_Up, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Page_Up, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_835(_: WIDParams):
    """
    description: Send a [HELP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Page_Down, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Page_Down, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_836(_: WIDParams):
    """
    description: Send a [HELP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Power, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Power, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_837(_: WIDParams):
    """
    description: Send a [VOLUME UP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Volume_Up, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Volume_Up, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_838(_: WIDParams):
    """
    description: Send a [VOLUME DOWN] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Volume_Down, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Volume_Down, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_839(_: WIDParams):
    """
    description: Send a [MUTE] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Mute, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Mute, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_840(_: WIDParams):
    """
    description: Send a [PLAY] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Play, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Play, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_841(_: WIDParams):
    """
    description: Send a [STOP] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Stop, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Stop, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_842(_: WIDParams):
    """
    description: Send a [PAUSE] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Pause, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Pause, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_843(_: WIDParams):
    """
    description: Send a [RECORD] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Record, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Record, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_844(_: WIDParams):
    """
    description: Send a [REWIND] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Rewind, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Rewind, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_845(_: WIDParams):
    """
    description: Send a [FAST FORWARD] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Fast_Forward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Fast_Forward, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_846(_: WIDParams):
    """
    description: Send a [EJECT] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Eject, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Eject, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_847(_: WIDParams):
    """
    description: Send a [FORWARE] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Forward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Forward, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_848(_: WIDParams):
    """
    description: Send a [BACKWARD] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Backward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Backward, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_849(_: WIDParams):
    """
    description: Send a [ANGLE] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Angle, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Angle, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_850(_: WIDParams):
    """
    description: Send a [SUBPICTURE] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Subpicture, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Subpicture, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_851(_: WIDParams):
    """
    description: Send a [F1] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F1, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F1, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_852(_: WIDParams):
    """
    description: Send a [F2] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F2, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F2, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_853(_: WIDParams):
    """
    description: Send a [F3] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F3, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F3, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_854(_: WIDParams):
    """
    description: Send a [F4] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F4, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F4, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_855(_: WIDParams):
    """
    description: Send a [F5] passthrough press and release to PTS.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F5, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F5, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_856(_: WIDParams):
    """
    description: Send a [VEMDPR UNIQUE] passthrough press and release to PTS.
    """
    payload = b'\x00\x19\x58\x00\x00' # Company Id = 0x001958(Bluetooth SIG, Inc), Vendor Dependent Information = 0x0000
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Vendor_Unique, 0, payload)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Vendor_Unique, 1, payload)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_889(_: WIDParams):
    """
    description: Quickly press and release the [0] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_0, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_0, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_890(_: WIDParams):
    """
    description: Quickly press and release the [1] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_1, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_1, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_891(_: WIDParams):
    """
    description: Quickly press and release the [2] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_2, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_2, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_892(_: WIDParams):
    """
    description: Quickly press and release the [3] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_3, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_3, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_893(_: WIDParams):
    """
    description: Quickly press and release the [4] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_4, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_4, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_894(_: WIDParams):
    """
    description: Quickly press and release the [5] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_5, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_5, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_895(_: WIDParams):
    """
    description: Quickly press and release the [6] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_6, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_6, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_896(_: WIDParams):
    """
    description: Quickly press and release the [7] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_7, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_7, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_897(_: WIDParams):
    """
    description: Quickly press and release the [8] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_8, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_8, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_898(_: WIDParams):
    """
    description: Quickly press and release the [9] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_9, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_9, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_899(_: WIDParams):
    """
    description: Quickly press and release the [Dot] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Dot, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Dot, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_900(_: WIDParams):
    """
    description: Quickly press and release the [Enter] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Enter, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Enter, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_901(_: WIDParams):
    """
    description: Quickly press and release the [Clear] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Clear, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Clear, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_905(_: WIDParams):
    """
    description: Quickly press and release the [SOUND SELECT] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Sound_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Sound_Select, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_906(_: WIDParams):
    """
    description: Quickly press and release the [INPUT SELECT] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Input_Select, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Input_Select, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_907(_: WIDParams):
    """
    description: Quickly press and release the [DISPLAY INFO] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Display_Information, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Display_Information, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_908(_: WIDParams):
    """
    description: Quickly press and release the [HELP] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Help, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Help, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_911(_: WIDParams):
    """
    description: Quickly press and release the [POWER] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Power, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Power, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_915(_: WIDParams):
    """
    description: Quickly press and release the [PLAY] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Play, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Play, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_916(_: WIDParams):
    """
    description: Quickly press and release the [STOP] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Stop, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Stop, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_917(_: WIDParams):
    """
    description: Quickly press and release the [PAUSE] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Pause, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Pause, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_918(_: WIDParams):
    """
    description: Quickly press and release the [RECORD] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Record, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Record, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_919(_: WIDParams):
    """
    description: Quickly press and release the [REWIND] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Rewind, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Rewind, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_920(_: WIDParams):
    """
    description: Quickly press and release the [FAST FOWARD] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Fast_Forward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Fast_Forward, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_921(_: WIDParams):
    """
    description: Quickly press and release the [EJECT] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Eject, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Eject, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_922(_: WIDParams):
    """
    description: Quickly press and release the [FORWARD] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Forward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Forward, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_923(_: WIDParams):
    """
    description: Quickly press and release the [BACKWARD] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Backward, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Backward, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_924(_: WIDParams):
    """
    description: Quickly press and release the [ANGLE] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Angle, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Angle, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_925(_: WIDParams):
    """
    description: Quickly press and release the [SUBPICTURE] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Subpicture, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Subpicture, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_926(_: WIDParams):
    """
    description: Quickly press and release the [F1] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F1, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F1, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_927(_: WIDParams):
    """
    description: Quickly press and release the [F2] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F2, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F2, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_928(_: WIDParams):
    """
    description: Quickly press and release the [F3] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F3, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F3, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_929(_: WIDParams):
    """
    description: Quickly press and release the [F4] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F4, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F4, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_930(_: WIDParams):
    """
    description: Quickly press and release the [F5] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F5, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_F5, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True


def hdl_wid_931(_: WIDParams):
    """
    description: Quickly press and release the [VEMDPR UNIQUE] passthrough command.
    """
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Vendor_Unique, 0)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    time.sleep(0.1)
    btp.avrcp_pass_through(AVCTPPassThroughOperation.Operation_Vendor_Unique, 1)
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_PASS_THROUGH)
    return True

def hdl_wid_1002(_: WIDParams):
    """
    description: If necessary, take action to accept the AVDTP Signaling Channel Connection initiated by the tester.
    """
    btp.a2dp_wait_for_command_rsp(defs.BTP_A2DP_EV_CONNECTED)

    return True

def hdl_wid_1004(_: WIDParams):
    """
    description: If necessary, take action to accept the AVDTP Discover operation initiated by the tester.
    """
    return True

def hdl_wid_1006(_: WIDParams):
    """
    description: If necessary, take action to accept the AVDTP Open operation initiated by the tester.
    """
    return True

def hdl_wid_1009(_: WIDParams):
    """
    description: If necessary, take action to accept the AVDTP Set Configuration operation initiated by the tester.
    """
    return True

def hdl_wid_1010(params: WIDParams):
    """
    description: If necessary, take action to accept the AVDTP Start operation initiated by the tester.
    """
    return True

def hdl_wid_1012(params: WIDParams):
    """
    description: If necessary, take action to accept the AVDTP Suspend operation initiated by the tester.
    """
    return True

def hdl_wid_1016(_: WIDParams):
    """
    description: Create an AVDTP signaling channel.
    """
    btp.gap_wait_for_connection()
    btp.a2dp_connect(None)

    return True

def hdl_wid_1042(_: WIDParams):
    """
    description: Take action to accept transport channels for the recently configured media stream.
    """
    return True

def hdl_wid_2001(_: WIDParams):
    """
    description: Please wait while PTS creates an AVCTP browsing channel connection.
    """
    btp.avrcp_wait_for_connection(defs.BTP_AVRCP_EV_BROWSING_CONNECTED)

    return True

def hdl_wid_2002(_: WIDParams):
    """
    description: Please wait while PTS creates an AVCTP control channel connection.
    """
    btp.avrcp_wait_for_connection(defs.BTP_AVRCP_EV_CONTROL_CONNECTED)

    return True

def hdl_wid_2003(_: WIDParams):
    """
    description: Please wait while PTS disconnects the AVCTP browsing channel connection.
    """
    btp.avrcp_wait_for_disconnection(defs.BTP_AVRCP_EV_BROWSING_CONNECTED)

    return True

def hdl_wid_2004(_: WIDParams):
    """
    description: Please wait while PTS disconnects the AVCTP control channel connection.
    """
    btp.avrcp_wait_for_disconnection(defs.BTP_AVRCP_EV_CONTROL_CONNECTED)

    return True

def hdl_wid_2005(_: WIDParams):
    """
    description: Take action to initiate a browsing channel connection by sending a connection request to the PTS from the IUT.
    """
    btp.avrcp_browsing_connect()

    return True

def hdl_wid_2006(_: WIDParams):
    """
    description: Take action to initiate a control channel connection by sending a connection request to the PTS from the IUT.
    """
    btp.avrcp_control_connect()

    return True

def hdl_wid_2007(_: WIDParams):
    """
    description: Take action to disconnect the AVCTP browsing channel.
    """
    stack = get_stack()
    if stack.avrcp.is_connected(btp.pts_addr_get(None), defs.BTP_AVRCP_EV_BROWSING_CONNECTED):
        btp.avrcp_browsing_disconnect()

    return True

def hdl_wid_2008(_: WIDParams):
    """
    description: Take action to disconnect the AVCTP control channel.
    """
    stack = get_stack()
    if stack.avrcp.is_connected(btp.pts_addr_get(None), defs.BTP_AVRCP_EV_BROWSING_CONNECTED):
        btp.avrcp_browsing_disconnect()
    btp.avrcp_control_disconnect()

    return True

def hdl_wid_3004(_: WIDParams):
    """
    description: Take action to send a valid response to the [Get Capabilities] command sent by the PTS.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_VENDOR_DEPENDENT_REQ)
    return True

def hdl_wid_3024(_: WIDParams):
    """
    description: Take action to send a valid response to the [Subunit Info] command sent by the PTS.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_SUBUNIT_INFO_REQ)
    return True

def hdl_wid_3025(_: WIDParams):
    """
    description: Take action to send a valid response to the [Unit Info] command sent by the PTS.
    """
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_UNIT_INFO_REQ)
    return True

def hdl_wid_3032(_: WIDParams):
    """
    description: Take action to send a [Get Capabilities] command to the PTS from the IUT.
    """
    # COMPANY_ID (0x2)
    btp.avrcp_vendor_dependent(AVRCPSpecificOperation.Get_Capabilities, b'\x02')
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_VENDOR_DEPENDENT)
    return True

def hdl_wid_3035(_: WIDParams):
    """
    description: Take action to send a [Set Addressed Player] command to the PTS from the IUT.
    """

    return True

def hdl_wid_3036(_: WIDParams):
    """
    description: Take action to send a [Set Browsed Player] command to the PTS from the IUT.
    """

    return True

def hdl_wid_3037(_: WIDParams):
    """
    description: Take action to send a [Get Folder Items] command with the scope of <Media Player List> to the PTS from the IUT.
    """

    return True

def hdl_wid_3088(_: WIDParams):
    """
    description: Take action to send a SUBUNIT INFO command to the PTS from the IUT.
    """
    btp.avrcp_subunit_info()
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_SUBUNIT_INFO)

    return True

def hdl_wid_3089(_: WIDParams):
    """
    description: Take action to send a UNIT INFO command to the PTS from the IUT.
    """
    btp.avrcp_unit_info()
    btp.avrcp_rx_data_get(defs.BTP_AVRCP_EV_UNIT_INFO)

    return True

def hdl_wid_20000(_: WIDParams):
    """
    description: Please prepare IUT into a connectable mode in BR/EDR.
    """
    stack = btp.get_stack()
    btp.gap_set_conn()
    btp.gap_set_gendiscov()
    btp.gap_adv_ind_on(ad=stack.gap.ad)

    return True