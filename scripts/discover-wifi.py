import argparse
from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt

# Set to store previously found networks (SSID and BSSID)
found_networks = set()

def packet_handler(pkt):
    if pkt.haslayer(Dot11Beacon):
        ssid = pkt[Dot11Elt].info.decode('utf-8', errors='ignore')
        bssid = pkt[Dot11].addr2.upper()  # Convert BSSID to uppercase
        channel = int(ord(pkt[Dot11Elt:3].info))
        
        # Create a unique identifier for each network
        network_id = (ssid, bssid)

        if network_id not in found_networks:
            found_networks.add(network_id)
            # Print in the desired format: SSID, BSSID, Channel
            if ssid == "":
                print(f"{bssid}, {channel}")
            else: 
                print(f"{ssid}, {bssid}, {channel}")

def scan(interface, timeout=10):
    print(f"Scanning on interface {interface}...")
    sniff(iface=interface, prn=packet_handler, store=0, timeout=timeout)

def main():
    parser = argparse.ArgumentParser(description="Wi-Fi network scanner")
    parser.add_argument("interface", help="Monitor mode interface to scan with")
    args = parser.parse_args()

    # Run the scan with the interface provided via the command line
    scan(args.interface)

if __name__ == "__main__":
    main()
