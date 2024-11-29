import requests
from colorama import Fore, Style, init
from pystyle import Box
init()

token = "691b5da3c2ffa2"
ip_address = input(Fore.RED + "Enter the IP address: ")
url = f"https://ipinfo.io/{ip_address}?token={token}"

response = requests.get(url)

if response.status_code == 200:
    ip_info = response.json()
    
    formatted_info = f"""
    Information for IP address {ip_address}:
    ----------------------------------------
    - IP: {ip_info.get('ip', 'N/A')}
    - City: {ip_info.get('city', 'N/A')}
    - Region: {ip_info.get('region', 'N/A')}
    - Country: {ip_info.get('country', 'N/A')}
    - Postal Code: {ip_info.get('postal', 'N/A')}
    - Latitude and Longitude: {ip_info.get('loc', 'N/A')}
    - Organization: {ip_info.get('org', 'N/A')}
    - ISP: {ip_info.get('asn', {}).get('name', 'N/A')}
    - Timezone: {ip_info.get('timezone', 'N/A')}
    """
    box_content = Box.DoubleCube(formatted_info.strip())
    print(Fore.RED + box_content + Style.RESET_ALL)
else:
    print(Fore.RED + f"Invalid IP address or information not available for {ip_address}" + Style.RESET_ALL)
