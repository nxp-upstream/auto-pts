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

from autopts.ptsprojects.stack import get_stack
from autopts.ptsprojects.testcase import TestFunc
from autopts.ptsprojects.zephyr.ztestcase import ZTestCase
from autopts.pybtp import btp
from autopts.ptsprojects.zephyr.hfp_wid import hfp_wid_hdl
from autopts.client import get_unique_name
from autopts.pybtp.types import Addr


def set_pixits(ptses):
    pts = ptses[0]

    pts.set_pixit("HFP", "TSPX_time_guard", "180000")
    pts.set_pixit("HFP", "TSPX_delete_link_key", "TRUE")
    pts.set_pixit("HFP", "TSPX_secure_simple_pairing_pass_key_confirmation", "FALSE")
    pts.set_pixit("HFP", "TSPX_use_implicit_send", "TRUE")
    pts.set_pixit("HFP", "TSPX_server_channel_tester", "01")


def test_cases(ptses):
    """
    Returns a list of HFP test cases
    ptses -- list of PyPTS instances
    """

    pts = ptses[0]
    pts_bd_addr = pts.q_bd_addr
    iut_device_name = get_unique_name(pts)
    stack = get_stack()

    # Generic preconditions for all test case in the profile
    pre_conditions = [
        TestFunc(btp.core_reg_svc_gap),
        TestFunc(btp.core_reg_svc_l2cap),
        TestFunc(stack.gap_init, iut_device_name),
        TestFunc(btp.gap_read_ctrl_info),
        TestFunc(lambda: pts.update_pixit_param(
            "HFP", "TSPX_bd_addr_iut",
            stack.gap.iut_addr_get_str())),
        TestFunc(btp.set_pts_addr, pts_bd_addr, Addr.le_public),
        # TestFunc(btp.core_reg_svc_gatt),
        # TestFunc(stack.gatt_init),
        TestFunc(btp.core_reg_svc_hfp),
        TestFunc(stack.hfp_init)
    ]

    custom_test_cases = [
        ZTestCase("HFP", "HFP/HF/TRS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/PSI/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/PSI/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/PSI/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/PSI/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/PSI/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BV-07-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BV-09-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BV-12-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BI-13-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BV-15-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACS/BV-17-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACR/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACR/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/CLI/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICA/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICA/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICA/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICA/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICA/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICA/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICA/BV-07-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICR/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICR/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RSV/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RSV/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RSV/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RMV/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RMV/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RMV/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TCA/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TCA/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TCA/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TCA/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATH/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATH/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATH/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATH/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/OCN/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/OCM/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/OCM/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/OCL/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/OCL/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),

        ZTestCase("HFP", "HFP/HF/TWC/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TWC/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TWC/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TWC/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TWC/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TWC/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/CIT/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ENO/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/VTG/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TDC/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ECC/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ECC/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ECC/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/NUM/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/NUM/BI-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/VRA/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/VRA/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/VRA/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/VRD/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ECS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ECS/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ECS/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/SDP/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RHH/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RHH/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RHH/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RHH/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RHH/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RHH/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RHH/BV-07-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/RHH/BV-08-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/PSI/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATA/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATA/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATA/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/HFI/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/DIS/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATH/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATH/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATH/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATH/BV-09-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ATAH/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/HFI/BI-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-08-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-09-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-10-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SLC/BV-11-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SDP/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SDP/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/CGSIT/SFC/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SGSIT/ATTR/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SGSIT/ATTR/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SGSIT/ATTR/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SGSIT/OFFS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/SGSIT/SERR/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/OCA/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/IIA/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ICA/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-08-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-09-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-07-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-10-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-11-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-12-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/ACC/BV-13-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/WBS/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/WBS/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/WBS/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/TDS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/OOR/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/HF/OOR/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_hf_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/DIS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/VRA/BI-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/TDS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/ICA/BV-07-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/ATH/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/ATH/BV-09-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/WBS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/ENO/BV-02-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/CGSIT/SFC/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/SGSIT/SERR/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/SGSIT/OFFS/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/SGSIT/ATTR/BV-06-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/SGSIT/ATTR/BV-01-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/SGSIT/ATTR/BV-05-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/SGSIT/ATTR/BV-03-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov)],
                  generic_wid_hdl=hfp_wid_hdl),
        ZTestCase("HFP", "HFP/AG/TWC/BV-04-C",
                  cmds=pre_conditions +
                       [TestFunc(btp.hfp_ag_register),
                        TestFunc(btp.gap_set_conn),
                        TestFunc(btp.gap_set_gendiscov),
                        TestFunc(btp.hfp_set_ongoing_calls, "1234567", 0, 1, 1),
                        TestFunc(btp.hfp_set_ongoing_calls, "7654321", 0, 0, 0, True)],
                  generic_wid_hdl=hfp_wid_hdl),
    ]

    test_case_name_list = pts.get_test_case_list('HFP')
    tc_list = []

    # Use the same preconditions and MMI/WID handler for all test cases of the profile
    for tc_name in test_case_name_list:
        instance = ZTestCase('HFP', tc_name, cmds=pre_conditions,
                             generic_wid_hdl=hfp_wid_hdl)
        for custom_tc in custom_test_cases:
            if tc_name == custom_tc.name:
                instance = custom_tc
                break

        tc_list.append(instance)


    return tc_list
