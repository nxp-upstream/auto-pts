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

from autopts.ptsprojects.stack.common import wait_for_event, wait_event_with_condition
from autopts.pybtp import defs

class HFP:
    def __init__(self):
        self.sco_connected = False
        self.need_check_sco_connection = False
        self.vr_need_terminate = False
        self.event_queues = {
            defs.BTP_HFP_EV_DUMMY_COMPLETED: [],
            defs.BTP_HFP_EV_SCO_CONNECTED: [],
            defs.BTP_HFP_EV_SCO_DISCONNECTED: [],
        }
        self.calls = {}

    def is_sco_connected(self):
        return self.sco_connected

    def event_received(self, event_type, event_data):
        self.event_queues[event_type].append(event_data)

    def wait_dummyevent_completed_ev(self, addr_type, addr, timeout, remove=True):
        return wait_event_with_condition(
            self.event_queues[defs.BTP_HFP_EV_DUMMY_COMPLETED],
            lambda _addr_type, _addr, *_:
            (addr_type, addr) == (_addr_type, _addr),
            timeout, remove)

    def wait_sco_connected_ev(self, timeout, remove=True):
        return wait_event_with_condition(
            self.event_queues[defs.BTP_HFP_EV_SCO_CONNECTED],
            lambda x: self.is_sco_connected,
            timeout, remove)

    def new_call(self, number, type, index, dir):
        status = defs.BTP_HFP_CALL_STATUS_DIALING
        if dir == defs.BTP_HFP_CALL_DIR_INCOMING:
            status = defs.BTP_HFP_CALL_STATUS_INCOMING
        call_info = {
            'number': number,
            'type': type,
            'dir': dir,
            'status': status
        }
        self.calls[index] = call_info

    def update_call(self, index, status):
        if index in self.calls:
            self.calls[index]['status'] = status

    def get_call_status(self, index):
        if index in self.calls:
            return self.calls[index]['status']
        return None

    def wait_call_status(self, index, status, timeout=5):
        return wait_for_event(timeout, lambda: self.get_call_status(index) is status)
