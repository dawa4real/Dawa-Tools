import socket

def check_open_ports(ip_address, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
    return open_ports


ip_address = input("[?] Entrez une adresse IP pour vérifier les ports ouverts : ")

print("[~] Recherche de ports ouverts en cours... ")

ports_to_check = [80, 443, 21, 22, 25, 53, 110, 143, 3306, 5432, 6379, 27017, 8080]

open_ports = check_open_ports(ip_address, ports_to_check)

if open_ports:
    print(f"[+] Ports ouverts pour l'adresse IP {ip_address} :")
    for port in open_ports:
        print(f"[+] Port {port} : Ouvert")
else:
    print(f"[-] Aucun port ouvert trouvé pour l'adresse IP {ip_address}.")
