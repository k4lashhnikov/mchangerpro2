import subprocess
import argparse
import os
import re
import random
from colorama import Fore, Style, init

init()

BANNER = '''
███╗   ███╗ ██████╗██████╗ ██████╗ 
████╗ ████║██╔════╝██╔══██╗╚════██╗
██╔████╔██║██║     ██████╔╝ █████╔╝
██║╚██╔╝██║██║     ██╔═══╝ ██╔═══╝ 
██║ ╚═╝ ██║╚██████╗██║     ███████╗
╚═╝     ╚═╝ ╚═════╝╚═╝     ╚══════╝

Author:💀💀 @k4lashhnikov 💀💀 | Security & Ethical Hacking
'''

def check_root():
    if os.geteuid() !=0:
        print(Fore.RED + "[!] You need root permissions to run this script." + Style.RESET_ALL)
        exit()

def get_user_input():
    parser = argparse.ArgumentParser(description="MAC Address Changer Pro V.2")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change MAC")
    parser.add_argument("-m", "--mac", dest="mac_address", help="New MAC address")
    parser.add_argument("-r", "--random", action="store_true", help="Generate random MAC")

    return parser.parse_args()

def random_mac():
    return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

def validate_mac(mac):
    pattern = r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$"
    return re.match(pattern, mac) is not None

def interface_exist(interface):
    try:
        subprocess.check_output(["ifconfig", interface])
        return True
    except subprocess.CalledProcessError:
        return False

def change_mac_address(interface, mac_address):
    print(Fore.YELLOW + f"[+] Changing MAC from {interface} to {mac_address}. . ." + Style.RESET_ALL)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    new_mac = re.search(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", ifconfig)
    return new_mac.group(0) if new_mac else None

if __name__ == "__main__":
    print(Fore.CYAN + BANNER + Style.RESET_ALL)
    check_root()
    user_input = get_user_input()

    if user_input.random:
        user_input.mac_address = random_mac()
        print(Fore.MAGENTA + f"[+] Random MAC Generated: {user_input.mac_address}" + Style.RESET_ALL)

    if not validate_mac(user_input.mac_address):
        print(Fore.RED + "[!] Invalid MAC address." + Style.RESET_ALL)
        exit()

    if not interface_exist(user_input.interface):
        print(Fore.RED + "[!] Interface does not exist." + Style.RESET_ALL)
        exit()

    change_mac_address(user_input.interface, user_input.mac_address)
    finalized_mac = control_new_mac(user_input.interface)

    if finalized_mac and finalized_mac.lower() == user_input.mac_address.lower():
        print(Fore.GREEN + "[+] MAC Changed Successfully!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "[!] Error: MAC address change failed. Check permissions or interface status." + Style.RESET_ALL)
