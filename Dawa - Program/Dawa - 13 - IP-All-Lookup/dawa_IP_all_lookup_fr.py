import socket
import requests
from colorama import Fore, Style
import sys

def ErreurModule(e):
    print(f"{Fore.RED}[?] Erreur d'importation du module : {e}{Style.RESET_ALL}")

def Erreur(e):
    print(f"{Fore.RED}[-] Une erreur s'est produite : {e}{Style.RESET_ALL}")

def heure_actuelle():
    import time
    return time.strftime("%H:%M:%S")

try:
    def scan_domaine(url_site_web):
        domaine = url_site_web.replace("https://", "").replace("http://", "").split('/')[0]
        return domaine
    
    def scan_securise(url_site_web):
        return url_site_web.startswith("https://")

    def scan_statut(url_site_web):
        response = requests.get(url_site_web)
        return response.status_code

    def scan_ip(domaine):
        try:
            ip = socket.gethostbyname(domaine)
        except:
            ip = "Aucune"

        try:
            response = requests.get(f"https://{domaine}/api/ip/ip={ip}")
            api = response.json()
            statut = api.get('status', 'Invalide')
            hebergeur_isp = api.get('isp', 'Aucun')
            hebergeur_org = api.get('org', 'Aucun')
            hebergeur_as = api.get('as', 'Aucun')
        except:
            statut = "Invalide"
            hebergeur_isp = "Aucun"
            hebergeur_org = "Aucun"
            hebergeur_as = "Aucun"

        return ip, statut, hebergeur_isp, hebergeur_org, hebergeur_as
    
    def scan_port(ip):
        ports_ouverts = []
        ports_communs = {
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
        
        for port, service in ports_communs.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    ports_ouverts.append((port, service))
            except Exception as e:
                ErreurModule(e)
            finally:
                sock.close()

        return ' / '.join([f'{port}/{service}' for port, service in ports_ouverts])

    print(f"{Fore.RED}Exemple: https://discord.com{Style.RESET_ALL}")
    url_site_web = input(f"\n{heure_actuelle()} {Fore.RED}URL du site web -> {Style.RESET_ALL}")
    print(f"{heure_actuelle()} {Fore.RED}[+] Analyse en cours...\n{Style.RESET_ALL}")

    if "https://" not in url_site_web and "http://" not in url_site_web:
        url_site_web = "https://" + url_site_web

    print(f"{Fore.RED}[+] Site Web : {url_site_web}{Style.RESET_ALL}")

    domaine = scan_domaine(url_site_web)
    print(f"{Fore.RED}[+] Domaine : {domaine}{Style.RESET_ALL}")

    securise = scan_securise(url_site_web)
    print(f"{Fore.RED}[+] Sécurisé : {securise}{Style.RESET_ALL}")

    code_statut = scan_statut(url_site_web)
    print(f"{Fore.RED}[+] Code Statut : {code_statut}{Style.RESET_ALL}")

    ip, statut_ip, hebergeur_isp, hebergeur_org, hebergeur_as = scan_ip(domaine)
    print(f"{Fore.RED}[+] IP : {ip}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Statut IP : {statut_ip}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] ISP Hôte : {hebergeur_isp}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Organisation Hôte : {hebergeur_org}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] AS Hôte : {hebergeur_as}{Style.RESET_ALL}")

    ports_ouverts = scan_port(ip)
    print(f"{Fore.RED}[+] Ports Ouverts : {ports_ouverts}{Style.RESET_ALL}")

    print()

except Exception as e:
    Erreur(e)

sys.exit()
