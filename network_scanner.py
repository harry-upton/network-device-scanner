import scapy.all as scapy
from scapy.layers.inet import IP, ICMP

ip_range="192.168.0.1/24"  # ip address range to scan in CIDR notation.
device_mac="ff:ff:ff:ff:ff:ff" # mac address of device you want to see if connected to network.

def createPacket(ip):
    arp_request = scapy.ARP(pdst=ip)  # create a ARP request object by scapy
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # We have set the destination
    arp_request_broadcast = broadcast / arp_request # Combine the arp request packet with ethernet frame.
    return (arp_request_broadcast)

def transmitPacket(packet):
    success_list, failure_list = scapy.srp(packet, timeout=1) # Send out packets and store answered packets.
    return success_list

def parseResponse(success_list):
    targets = []
    for success in success_list:
        entry = {'ip': success[1].psrc, 'mac': success[1].hwsrc} # Create a key-value pair of ip and mac address.
        targets.append(entry)
    return targets

def deviceConnected(ip, mac):
    broadcast_packets = createPacket(ip_range)
    success_packets = transmitPacket(broadcast_packets)
    results = parseResponse(success_packets)
    for e in results:
        if e['mac'].lower() == mac:
            return True
    return False

print(deviceConnected(ip_range, device_mac))