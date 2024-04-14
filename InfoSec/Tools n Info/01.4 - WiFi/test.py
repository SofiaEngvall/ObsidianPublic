#!/usr/bin/python3

from scapy.all import *


def WiFiEnumeration(packet):
    if packet.haslayer(Dot11Beacon):
        pass


if __name__ == "__main__":
    print(ifaces)
    # sniff(prn=WiFiEnumeration, iface="", timeout=5)
