# network-device-scanner
Scans network and checks if a mac address is connected.

Set the IP range to scan and the mac address of the device you are looking for. The "deviceConnected" function will return true if the device is currently on the network.
The function can be called regularly in a loop, if it returns true some other code can be executed.

- The script requires root permissions. If on linux: `sudo python3 network_scanner.py`
- IP address range is given using **CIDR** notation. [An explanation](https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking).
- Inspired by [this article](https://medium.com/hacking-hunter/creating-own-network-scanner-using-python-f11a50a5ff77) and using code from [this repository](https://github.com/rcvaram/BNS-scanner).

### Dependencies
- **Scapy**, install from your distro's repository: e.g. `sudo apt-get install python-scapy` or `sudo pacman -S python-scapy` for Debian/Ubuntu and Arch respectively.
