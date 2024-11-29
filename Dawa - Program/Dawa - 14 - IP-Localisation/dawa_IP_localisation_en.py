import requests

def get_ip_location(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        if response.status_code == 200:
            location_info = response.json()
            return location_info
        else:
            print(f"Error in API request: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None
ip_address = input("[?] Enter an IP address to locate: ")
location_info = get_ip_location(ip_address)

if location_info:
    print("[+] Location information:")
    print(f"[+] Country: {location_info['country']}")
    print(f"[+] City: {location_info['city']}")
    print(f"[+] Region: {location_info['regionName']}")
    print(f"[+] ZIP code: {location_info['zip']}")
    print(f"[+] Latitude: {location_info['lat']}")
    print(f"[+] Longitude: {location_info['lon']}")
else:
    print("Unable to retrieve location information for this IP address.")
