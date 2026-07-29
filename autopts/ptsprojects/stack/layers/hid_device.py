#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright 2026, NXP.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#

import logging

from autopts.ptsprojects.stack.common import wait_for_event

log = logging.debug


class HIDDevice:
    """
    HID Device (Human Interface Device Profile) layer implementation
    """
    def __init__(self):
        """Initialize HID Device layer"""
        log(f"{self.__init__.__name__}")
        self.connected = False
        self.connected_addr = None
        self.connected_addr_type = None

    def wait_for_connection(self, timeout=30):
        """
        Wait for HID Device connection to be established.

        Args:
            timeout (int): Maximum time to wait in seconds (default: 30)

        Returns:
            bool: True if connection established, False otherwise
        """
        logging.debug("%s timeout=%d", self.wait_for_connection.__name__, timeout)

        return wait_for_event(timeout, lambda: self.connected is True)

    def wait_for_disconnection(self, timeout=30):
        """
        Wait for HID Device connection to be closed.

        Args:
            timeout (int): Maximum time to wait in seconds (default: 30)

        Returns:
            bool: True if disconnection completed, False otherwise
        """
        logging.debug("%s timeout=%d", self.wait_for_disconnection.__name__, timeout)

        return wait_for_event(timeout, lambda: self.connected is False)

    def set_connected(self, addr, addr_type):
        """
        Set the connection information when a HID Device connection is established.

        Args:
            addr (str): Bluetooth address of the connected device
            addr_type (int): Address type
        """
        self.connected = True
        self.connected_addr = addr
        self.connected_addr_type = addr_type

    def set_disconnected(self, addr, addr_type):
        """
        Update state when a HID Device connection is closed.

        Args:
            addr (str): Bluetooth address of the disconnected device
            addr_type (int): Address type
        """
        self.connected = False
        self.connected_addr = addr
        self.connected_addr_type = addr_type

    def cleanup(self):
        """Cleanup HID Device resources"""
        log(f"{self.cleanup.__name__}")
        self.connected = False
        self.connected_addr = None
        self.connected_addr_type = None
