import requests

def get_ip_operator(ip_address):
    try:
        response = requests.get(f'http://ipinfo.io/{ip_address}/org')
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Erreur lors de la requête API : {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Erreur de connexion : {e}"

ip_address = input("[?] Entrez une adresse IP pour déterminer le fournisseur de services Internet : ")

operator_info = get_ip_operator(ip_address)

print(f"[+] Fournisseur de services Internet associé à l'adresse IP {ip_address} :")
print(operator_info)
