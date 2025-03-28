mchangerpro2

### Author: @k4lashhnikov | Security & Ethical Hacking

## Description
`mchangerpro2` is a powerful and user-friendly Python tool designed for changing the MAC address of network interfaces on Kali Linux. It provides the ability to set a specific MAC address or generate a random one for anonymity and security purposes. With a straightforward command-line interface, `mchangerpro2` is ideal for penetration testers, ethical hackers, and privacy enthusiasts looking to enhance their network privacy.

## Features
- Change MAC address to a specific value.
- Generate random MAC addresses.
- Check and validate MAC address changes.
- Simple and intuitive command-line interface.

## Requirements
- Python 3
- Kali Linux
- Python Modules: `subprocess`, `argparse`, `os`, `re`, `random`, `colorama`

### Install necessary modules:
```
pip install colorama
```

## Installation
1. Clone the repository:
```
git clone https://github.com/k4lashhnikov/mchangerpro2.git
```
2. Navigate to the directory:
```
cd mchangerpro2
```

## Usage

### Change MAC to a specific address
```
sudo python3 mchangerpro2.py -i wlan0 -m 00:11:22:33:44:55
```

### Change MAC to a randomly generated address
```
sudo python3 mchangerpro2.py -i wlan0 -r
```

## Note
- The script must be run with root permissions (`sudo`).
- `wlan0` should be replaced with the interface you wish to modify.


## Contact
- GitHub: [@k4lashhnikov](https://github.com/k4lashhnikov)
- LinkedIn: [@k4lashhnikov](https://www.linkedin.com/in/k4lashhnikov/)
- E-mail: fiftharmando@gmail.com
