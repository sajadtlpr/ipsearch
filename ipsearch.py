import argparse
import requests
import sys

# Colors
RED = '\033[31m'  
GREEN = '\033[32m'
YELLOW = '\033[33m'
CLEAR = '\033[0m'

# Banners 
banner = f"""
{RED}

  _____                               _               
 |_   _|                             | |              
   | |  _ __  ___  ___  __ _ _ __ ___| |__   ___ _ __ 
   | | | '_ \/ __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__|
  _| |_| |_) \__ \  __/ (_| | | | (__| | | |  __/ |   
 |_____| .__/|___/\___|\__,_|_|  \___|_| |_|\___|_|   
       | |                                            
       |_|                                            
{CLEAR}
"""

banner2 = f"""{GREEN}
<=== [[Developed by Sajadtlpr]] ===>  
<---(( Greets to all HITLOS SQUAD MEMBERS ))-->
{CLEAR}"""

print(banner)
print(banner2)

parser = argparse.ArgumentParser()
parser.add_argument("-v", help="target IP address", dest='target', required=True)
args = parser.parse_args()  

if not args.target:
    print(f"{RED}Error: IP address is required{CLEAR}")
    parser.print_help()
    sys.exit(1)

ip = args.target

try:
    data = requests.get(f"http://ip-api.com/json/{ip}").json()

    print(f"{GREEN}[Victim]: {data['query']}{CLEAR}")
    print(f"{YELLOW}[ISP]: {data['isp']}{CLEAR}")
    print(f"{GREEN}[Organisation]: {data['org']}{CLEAR}")
    print(f"{YELLOW}[City]: {data['city']}{CLEAR}")
    print(f"{GREEN}[Region]: {data['region']}{CLEAR}")
    print(f"{YELLOW}[Longitude]: {data['lon']}{CLEAR}")
    print(f"{GREEN}[Latitude]: {data['lat']}{CLEAR}")
    print(f"{YELLOW}[Time zone]: {data['timezone']}{CLEAR}")
    print(f"{GREEN}[Zip code]: {data['zip']}{CLEAR}")

except requests.exceptions.ConnectionError:
    print(f"{RED}Error: Check your internet connection!{CLEAR}")
    sys.exit(1)