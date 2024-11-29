import socket
import requests
from colorama import Fore, Style
import sys

def ErrorModule(e):
    print(f"{Fore.RED}[?] Module import error: {e}{Style.RESET_ALL}")

def Error(e):
    print(f"{Fore.RED}[-] An error occurred: {e}{Style.RESET_ALL}")

def current_time():
    import time
    return time.strftime("%H:%M:%S")

try:
    def scan_domain(url_website):
        domain = url_website.replace("https://", "").replace("http://", "").split('/')[0]
        return domain
    
    def scan_secure(url_website):
        return url_website.startswith("https://")

    def scan_status(url_website):
        response = requests.get(url_website)
        return response.status_code

    def scan_ip(domain):
        try:
            ip = socket.gethostbyname(domain)
        except:
            ip = "None"

        try:
            response = requests.get(f"https://{domain}/api/ip/ip={ip}")
            api = response.json()
            status = api.get('status', 'Invalid')
            isp_provider = api.get('isp', 'None')
            org_provider = api.get('org', 'None')
            as_provider = api.get('as', 'None')
        except:
            status = "Invalid"
            isp_provider = "None"
            org_provider = "None"
            as_provider = "None"

        return ip, status, isp_provider, org_provider, as_provider
    
    def scan_port(ip):
        open_ports = []
        common_ports = {
            80: "HTTP",
            443: "HTTPS",
            21: "FTP",
            22: "SSH",
            25: "SMTP",
            53: "DNS",
            110: "POP3",
            143: "IMAP",
            3306: "MySQL",
            5432: "PostgreSQL",
            6379: "Redis",
            27017: "MongoDB",
            8080: "HTTP-alt"
        }
        
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append((port, service))
            except Exception as e:
                ErrorModule(e)
            finally:
                sock.close()

        return ' / '.join([f'{port}/{service}' for port, service in open_ports])

    print(f"{Fore.RED}Example: https://discord.com{Style.RESET_ALL}")
    url_website = input(f"\n{current_time()} {Fore.RED}Website URL -> {Style.RESET_ALL}")
    print(f"{current_time()} {Fore.RED}[+] Analysis in progress...\n{Style.RESET_ALL}")

    if "https://" not in url_website and "http://" not in url_website:
        url_website = "https://" + url_website

    print(f"{Fore.RED}[+] Website : {url_website}{Style.RESET_ALL}")

    domain = scan_domain(url_website)
    print(f"{Fore.RED}[+] Domain : {domain}{Style.RESET_ALL}")

    secure = scan_secure(url_website)
    print(f"{Fore.RED}[+] Secure : {secure}{Style.RESET_ALL}")

    status_code = scan_status(url_website)
    print(f"{Fore.RED}[+] Status Code : {status_code}{Style.RESET_ALL}")

    ip, ip_status, isp_provider, org_provider, as_provider = scan_ip(domain)
    print(f"{Fore.RED}[+] IP : {ip}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] IP Status : {ip_status}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] ISP Provider : {isp_provider}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Organization Provider : {org_provider}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] AS Provider : {as_provider}{Style.RESET_ALL}")

    open_ports = scan_port(ip)
    print(f"{Fore.RED}[+] Open Ports : {open_ports}{Style.RESET_ALL}")

    print()

except Exception as e:
    Error(e)

sys.exit()
