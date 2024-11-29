import requests
from colorama import Fore, Style, init
from pystyle import Box


init()


token = "691b5da3c2ffa2"
ip_address = input(Fore.RED + "Entrer l'adresse IP : ")
url = f"https://ipinfo.io/{ip_address}?token={token}"

response = requests.get(url)

if response.status_code == 200:
    ip_info = response.json()
    

    formatted_info = f"""
    Informations pour l'adresse IP {ip_address} :
    -------------------------------------------
    - IP: {ip_info.get('ip', 'N/A')}
    - Ville: {ip_info.get('city', 'N/A')}
    - Région: {ip_info.get('region', 'N/A')}
    - Pays: {ip_info.get('country', 'N/A')}
    - Code postal: {ip_info.get('postal', 'N/A')}
    - Latitude et Longitude: {ip_info.get('loc', 'N/A')}
    - Organisation: {ip_info.get('org', 'N/A')}
    - FAI: {ip_info.get('asn', {}).get('name', 'N/A')}
    - Fuseau horaire: {ip_info.get('timezone', 'N/A')}
    """
    

    box_content = Box.DoubleCube(formatted_info.strip())
    
  
    print(Fore.RED + box_content + Style.RESET_ALL)
else:
    print(Fore.RED + f"Adresse IP non valide ou informations non disponibles pour {ip_address}" + Style.RESET_ALL)
