#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2017, Intel Corporation.
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

"""L2CAP test cases"""

from autopts.client import get_unique_name
from autopts.ptsprojects.stack import get_stack
from autopts.ptsprojects.testcase import TestFunc
from autopts.ptsprojects.zephyr.ztestcase import ZTestCase
from autopts.pybtp import btp, defs
from autopts.pybtp.types import Addr, IOCap, L2CAPConnectionResponse
from autopts.wid import l2cap_wid_hdl

le_psm = 128
psm_unsupported = 241
le_initial_mtu = 120
le_initial_mtu_equal_mps = 96

br_psm = 0x1001
br_initial_mtu = 120


def set_pixits(ptses):
    """Setup L2CAP profile PIXITS for workspace. Those values are used for test
    case if not updated within test case.

    PIXITS always should be updated accordingly to project and newest version of
    PTS.

    ptses -- list of PyPTS instances"""

    pts = ptses[0]

    pts.set_pixit("L2CAP", "TSPX_bd_addr_iut", "DEADBEEFDEAD")
    pts.set_pixit("L2CAP", "TSPX_security_enabled", "FALSE")
    pts.set_pixit("L2CAP", "TSPX_delete_link_key", "FALSE")
    pts.set_pixit("L2CAP", "TSPX_pin_code", "0000")
    pts.set_pixit("L2CAP", "TSPX_delete_ltk", "FALSE")
    pts.set_pixit("L2CAP", "TSPX_l2ca_inmtu", "02A0")
    pts.set_pixit("L2CAP", "TSPX_iut_supported_max_channels", "5")
    pts.set_pixit("L2CAP", "TSPX_tester_mps", "0017")
    pts.set_pixit("L2CAP", "TSPX_tester_mtu", "02A0")
    pts.set_pixit("L2CAP", "TSPX_iut_role_initiator", "True")
    pts.set_pixit("L2CAP", "TSPX_spsm", "0000")
    pts.set_pixit("L2CAP", "TSPX_psm", "0001")
    pts.set_pixit("L2CAP", "TSPX_psm_unsupported", "0000")
    pts.set_pixit("L2CAP", "TSPX_psm_authentication_required", "00F2")
    pts.set_pixit("L2CAP", "TSPX_psm_authorization_required", "00F3")
    pts.set_pixit("L2CAP", "TSPX_psm_encryption_key_size_required", "00F4")
    pts.set_pixit("L2CAP", "TSPX_time_guard", "180000")
    pts.set_pixit("L2CAP", "TSPX_timer_rtx", "10000")
    pts.set_pixit("L2CAP", "TSPX_timer_rtx_max", "1000")
    pts.set_pixit("L2CAP", "TSPX_timer_rtx_min", "60000")
    pts.set_pixit("L2CAP", "TSPX_use_implicit_send", "TRUE")
    pts.set_pixit("L2CAP", "TSPX_use_dynamic_pin", "FALSE")
    pts.set_pixit("L2CAP", "TSPX_iut_SDU_size_in_bytes", "144")
    pts.set_pixit("L2CAP", "TSPX_secure_simple_pairing_pass_key_confirmation", "FALSE")
    pts.set_pixit("L2CAP", "TSPX_generate_local_busy", "TRUE")
    pts.set_pixit("L2CAP", "TSPX_l2ca_cbmps_min", "0040")
    pts.set_pixit("L2CAP", "TSPX_l2ca_cbmps_max", "0100")


def test_cases(ptses):
    """Returns a list of L2CAP test cases
    ptses -- list of PyPTS instances"""

    pts = ptses[0]

    pts_bd_addr = pts.q_bd_addr

    stack = get_stack()

    iut_device_name = get_unique_name(pts)
    stack.gap_init(iut_device_name)

    common = [TestFunc(btp.core_reg_svc_gap),
              TestFunc(btp.core_reg_svc_l2cap),
              TestFunc(btp.gap_read_ctrl_info),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_bd_addr_iut",
                  stack.gap.iut_addr_get_str())),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_spsm", format(le_psm, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_psm_authentication_required", format(le_psm, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_psm_authorization_required", format(le_psm, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_psm_encryption_key_size_required", format(le_psm, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_psm_encryption_required", format(le_psm, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_psm_unsupported", format(psm_unsupported, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_iut_supported_max_channels", "2")),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_l2ca_num_concurrent_credit_based_connections", "2")),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_l2ca_cbmps_min", format(64, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_l2ca_cbmps_max", format(256, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_l2ca_cbmtu_min", format(64, '04x'))),
              TestFunc(lambda: pts.update_pixit_param(
                  "L2CAP", "TSPX_l2ca_cbmtu_max", format(256, '04x'))),
              TestFunc(btp.set_pts_addr, pts_bd_addr, Addr.le_public)]

    pre_conditions = common + [TestFunc(stack.l2cap_init, le_psm, le_initial_mtu)]
    pre_conditions_success = common + [TestFunc(stack.l2cap_init, le_psm, le_initial_mtu),
                                       TestFunc(btp.l2cap_le_listen, le_psm, le_initial_mtu,
                                                L2CAPConnectionResponse.success)]
    pre_conditions_authen = common + [TestFunc(stack.l2cap_init, le_psm, le_initial_mtu),
                                      TestFunc(btp.l2cap_le_listen, le_psm, le_initial_mtu,
                                               L2CAPConnectionResponse.insufficient_authentication)]
    pre_conditions_keysize = common + [TestFunc(stack.l2cap_init, le_psm, le_initial_mtu),
                                       TestFunc(btp.l2cap_le_listen, le_psm, le_initial_mtu,
                                                L2CAPConnectionResponse.insufficient_encryption_key_size)]
    pre_conditions_author = common + [TestFunc(stack.l2cap_init, le_psm, le_initial_mtu),
                                      TestFunc(btp.l2cap_le_listen, le_psm, le_initial_mtu,
                                               L2CAPConnectionResponse.insufficient_authorization)]

    br_pre_cond = common + [
        TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_psm", format(br_psm, '04x'))),
        TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_delete_link_key", "FALSE")),
        TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_delete_ltk", "FALSE")),
        TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_iut_role_initiator", "False")),
        TestFunc(btp.gap_set_io_cap, IOCap.no_input_output),
    ]

    br_l2cap = br_pre_cond + [
        TestFunc(stack.l2cap_init, br_psm, br_initial_mtu),
    ]

    br_l2cap_success = br_l2cap + [
        TestFunc(btp.l2cap_br_listen, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption),
    ]

    br_l2cap_success_ret = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_RET),
    ]

    br_l2cap_success_fc = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_FC),
    ]

    br_l2cap_success_eret = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_ERET),
    ]

    br_l2cap_success_stream = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_STREAM),
    ]

    br_l2cap_success_eret_no_fcs = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_ERET,
                 defs.L2CAP_LISTEN_V2_OPT_NO_FCS),
    ]

    br_l2cap_success_stream_no_fcs = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_STREAM,
                 defs.L2CAP_LISTEN_V2_OPT_NO_FCS),
    ]

    br_l2cap_success_eret_hold_credit = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_ERET,
                 defs.L2CAP_LISTEN_V2_OPT_HOLD_CREDIT),
    ]

    br_l2cap_success_eret_optional = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_ERET,
                 defs.L2CAP_LISTEN_V2_OPT_MODE_OPTIONAL),
    ]

    br_l2cap_success_stream_optional = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_STREAM,
                 defs.L2CAP_LISTEN_V2_OPT_MODE_OPTIONAL),
    ]

    br_l2cap_success_eret_extended_control = br_l2cap + [
        TestFunc(btp.l2cap_br_listen_v2, br_psm, br_initial_mtu,
                 L2CAPConnectionResponse.insufficient_encryption, defs.L2CAP_LISTEN_V2_MODE_ERET,
                 defs.L2CAP_LISTEN_V2_OPT_EXT_WIN_SIZE),
    ]

    custom_test_cases = [
        ZTestCase("L2CAP", "L2CAP/LE/CFC/BV-04-C",
                  pre_conditions +
                  [TestFunc(lambda: stack.l2cap.psm_set(psm_unsupported))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/LE/CFC/BV-11-C",
                  pre_conditions_authen,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/LE/CFC/BV-13-C",
                  pre_conditions_author,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/LE/CFC/BV-15-C",
                  pre_conditions_keysize,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/LE/CFC/BV-25-C",
                  pre_conditions_authen,
                  generic_wid_hdl=l2cap_wid_hdl),
        # Enhanced Credit Based Flow Control Channel
        ZTestCase("L2CAP", "L2CAP/COS/ECFC/BV-04-C",
                  pre_conditions +
                  [TestFunc(lambda: stack.l2cap.initial_mtu_set(le_initial_mtu_equal_mps))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BV-11-C",
                  pre_conditions_authen,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BV-13-C",
                  pre_conditions_author,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BV-15-C",
                  pre_conditions_keysize,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BV-24-C",
                  pre_conditions_success +
                  [TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_l2ca_cbmps_max", format(64, '04x')))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BV-25-C",
                  pre_conditions_success +
                  [TestFunc(lambda: stack.l2cap.num_channels_set(1))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BV-29-C",
                  pre_conditions_success +
                  [TestFunc(lambda: stack.l2cap.num_channels_set(1))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BV-32-C",
                  pre_conditions_authen,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BI-01-C",
                  pre_conditions_success +
                  [TestFunc(lambda: stack.l2cap.num_channels_set(1))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BI-02-C",
                  pre_conditions_success +
                  [TestFunc(lambda: stack.l2cap.num_channels_set(1)),
                   TestFunc(lambda: stack.l2cap.hold_credits_set(1))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECFC/BI-07-C",
                  pre_conditions_success +
                  [TestFunc(lambda: stack.l2cap.hold_credits_set(1))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/TIM/BV-03-C",
                  pre_conditions_success +
                  [TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_iut_role_initiator", "False")),
                   TestFunc(btp.core_reg_svc_gatt)],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-07-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-08-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-09-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-01-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-01-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-02-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-03-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-11-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-12-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-14-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-08-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-03-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-06-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-07-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-04-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-08-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-10-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-12-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-14-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-15-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BI-03-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-04-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/ECH/BV-02-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/ECH/BV-01-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/IEX/BV-01-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/IEX/BV-02-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/EXF/BV-07-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-10-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/RTX/BV-01-C",
                  br_l2cap_success_ret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/RTX/BV-02-C",
                  br_l2cap_success_ret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/RTX/BV-03-C",
                  br_l2cap_success_ret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-10-C",
                  br_l2cap_success_fc,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/FLC/BV-01-C",
                  br_l2cap_success_fc,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/FLC/BV-02-C",
                  br_l2cap_success_fc,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/FLC/BV-03-C",
                  br_l2cap_success_fc,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/FLC/BV-04-C",
                  br_l2cap_success_fc,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-13-C",
                  br_l2cap_success_fc,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-01-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-02-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-01-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-02-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-03-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-08-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-09-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-10-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-11-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-12-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-18-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-19-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-20-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-04-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-05-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/STM/BV-01-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/STM/BV-02-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/FOC/BV-06-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/FOC/BV-08-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/FOC/BV-01-C",
                  br_l2cap_success_eret_no_fcs,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/FOC/BV-02-C",
                  br_l2cap_success_eret_no_fcs,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/FOC/BV-03-C",
                  br_l2cap_success_eret_no_fcs,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/FOC/BV-05-C",
                  br_l2cap_success_eret_no_fcs,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/OFS/BV-05-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/OFS/BV-06-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/OFS/BV-01-C",
                  br_l2cap_success_eret_no_fcs,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/OFS/BV-02-C",
                  br_l2cap_success_eret_no_fcs,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/OFS/BV-07-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/OFS/BV-08-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/OFS/BV-03-C",
                  br_l2cap_success_stream_no_fcs,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/OFS/BV-04-C",
                  br_l2cap_success_stream_no_fcs,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-07-C",
                  br_l2cap_success_eret_hold_credit +
                  [TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_generate_local_busy", "False"))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-22-C",
                  br_l2cap_success_eret_hold_credit +
                  [TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_generate_local_busy", "False"))],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-16-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BI-01-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BI-01-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BI-02-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-12-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BI-03-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BI-04-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-13-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-03-C",
                  br_l2cap_success_eret_optional,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-07-C",
                  br_l2cap_success_eret_optional,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-10-C",
                  br_l2cap_success_eret_optional,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-06-C",
                  br_l2cap_success_stream_optional,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-08-C",
                  br_l2cap_success_stream_optional,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-11-C",
                  br_l2cap_success_stream_optional,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-23-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/STM/BV-03-C",
                  br_l2cap_success_stream,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-09-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BI-05-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BI-06-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-14-C",
                  br_l2cap_success_stream_optional,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/CMC/BV-15-C",
                  br_l2cap_success_stream_optional,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-05-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-06-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-13-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BI-03-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BI-04-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BI-05-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-14-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ERM/BV-15-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/EWC/BV-01-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/EWC/BV-02-C",
                  br_l2cap_success_eret,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/EWC/BV-03-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECF/BV-01-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECF/BV-02-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECF/BV-03-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECF/BV-04-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECF/BV-05-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECF/BV-06-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECF/BV-07-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/ECF/BV-08-C",
                  br_l2cap_success_eret_extended_control,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CFD/BV-09-C",
                  br_l2cap_success +
                  [TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_iut_role_initiator", "True")),],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-01-C",
                  br_l2cap_success +
                  [TestFunc(lambda: pts.update_pixit_param("L2CAP", "TSPX_iut_role_initiator", "True")),],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-12-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/COS/CED/BV-11-C",
                  br_l2cap_success,
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/LE/CID/BV-01-C",
                  br_pre_cond + [TestFunc(stack.l2cap_init, le_psm, le_initial_mtu)],
                  generic_wid_hdl=l2cap_wid_hdl),
        ZTestCase("L2CAP", "L2CAP/LE/CID/BV-02-C",
                  br_l2cap_success +
                  [TestFunc(stack.l2cap_init, le_psm, le_initial_mtu),
                   TestFunc(btp.l2cap_le_listen, le_psm, le_initial_mtu,
                            L2CAPConnectionResponse.success)],
                  generic_wid_hdl=l2cap_wid_hdl),
    ]

    test_case_name_list = pts.get_test_case_list('L2CAP')
    tc_list = []

    for tc_name in test_case_name_list:
        instance = ZTestCase('L2CAP', tc_name,
                             pre_conditions_success,
                             generic_wid_hdl=l2cap_wid_hdl)

        for custom_tc in custom_test_cases:
            if tc_name == custom_tc.name:
                instance = custom_tc
                break

        tc_list.append(instance)

    return tc_list
