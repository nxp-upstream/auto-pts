#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright 2026 NXP
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

"""HID11 Host-only test cases (PTS workspace project HID11, /HOS/ subset)."""

from autopts.client import get_unique_name
from autopts.ptsprojects.stack import get_stack
from autopts.ptsprojects.testcase import TestFunc
from autopts.ptsprojects.zephyr.hid_host_wid import hid_host_wid_hdl
from autopts.ptsprojects.zephyr.ztestcase import ZTestCase
from autopts.pybtp import btp
from autopts.pybtp.types import Addr


def set_pixits(ptses):
    """Setup HID11 profile PIXITS for workspace.

    Those values are used for the test case if not updated within the test
    case itself.  Always keep them in sync with the project and the newest
    version of PTS.

    ptses -- list of PyPTS instances
    """
    pts = ptses[0]

    pts.set_pixit("HID11", "TSPX_time_guard", "180000")
    pts.set_pixit("HID11", "TSPX_use_implicit_send", "TRUE")
    pts.set_pixit("HID11", "TSPX_delete_link_key", "TRUE")
    # PTS builds the HIDDeviceSubclass attribute of its emulated HID device
    # from TSPX_Tester_DID_ProductID. HID1.1 requires bits 1 and 0 of
    # HIDDeviceSubclass to be zero, so the PTS default of 1 makes
    # IOPT/HID11/HOS/CGSIT/SFC/BV-01-I end as Indecisive right after the SDP
    # records are registered, before any WID is sent to the IUT.
    # 0xC0 (192) selects the keyboard subclass and keeps bits 1:0 zero.
    pts.set_pixit("HID11", "TSPX_Tester_DID_ProductID", "192")


def test_cases(ptses):
    """Return a list of HID11 Host test cases.

    Only /HOS/ test cases are selected from the HID11 PTS project.

    ptses -- list of PyPTS instances
    """
    pts = ptses[0]
    pts_bd_addr = pts.q_bd_addr
    iut_device_name = get_unique_name(pts)
    stack = get_stack()

    pre_conditions = [
        TestFunc(btp.core_reg_svc_gap),
        TestFunc(stack.gap_init, iut_device_name),
        TestFunc(btp.gap_read_controller_info),
        TestFunc(lambda: pts.update_pixit_param(
            "HID11", "TSPX_bd_addr_iut",
            stack.gap.iut_addr_get_str())),
        TestFunc(btp.set_pts_addr, pts_bd_addr, Addr.le_public),
        TestFunc(btp.core_reg_svc_hid_host),
        TestFunc(stack.hid_host_init),
    ]

    # Only take Host-role (/HOS/) cases from the HID11 project.
    test_case_name_list = [tc for tc in pts.get_test_case_list('HID11')
                           if '/HOS/' in tc]
    tc_list = []

    for tc_name in test_case_name_list:
        instance = ZTestCase('HID11', tc_name, cmds=pre_conditions,
                             generic_wid_hdl=hid_host_wid_hdl)
        tc_list.append(instance)

    return tc_list
