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


ip_address = input("[?] Enter an IP address to check for open ports: ")

print("[~] Searching for open ports...")


ports_to_check = [80, 443, 21, 22, 25, 53, 110, 143, 3306, 5432, 6379, 27017, 8080]


open_ports = check_open_ports(ip_address, ports_to_check)


if open_ports:
    print(f"[+] Open ports for IP address {ip_address}:")
    for port in open_ports:
        print(f"Port {port}: Open")
else:
    print(f"[-] No open ports found for IP address {ip_address}.")
