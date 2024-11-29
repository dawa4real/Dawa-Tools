import requests

def get_ip_operator(ip_address):
    try:
        response = requests.get(f'http://ipinfo.io/{ip_address}/org')
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Error in API request: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"

ip_address = input("[?] Enter an IP address to determine the ISP: ")

operator_info = get_ip_operator(ip_address)

print(f"[+] ISP associated with IP {ip_address}:")
print(operator_info)
