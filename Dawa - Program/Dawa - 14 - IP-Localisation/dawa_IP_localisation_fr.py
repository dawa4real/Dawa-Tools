import requests

def get_ip_location(ip_address):
    """Fonction pour récupérer les informations de localisation d'une adresse IP depuis ip-api.com."""
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        if response.status_code == 200:
            location_info = response.json()
            return location_info
        else:
            print(f"Erreur lors de la requête API : {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        return None

ip_address = input("[?] Entrez une adresse IP à localiser : ")
location_info = get_ip_location(ip_address)

if location_info:
    print("[+] Informations de localisation :")
    print(f"[+] Pays : {location_info['country']}")
    print(f"[+] Ville : {location_info['city']}")
    print(f"[+] Région : {location_info['regionName']}")
    print(f"[+] Code postal : {location_info['zip']}")
    print(f"[+] Latitude : {location_info['lat']}")
    print(f"[+] Longitude : {location_info['lon']}")
else:
    print("Impossible de récupérer les informations de localisation pour cette adresse IP.")
