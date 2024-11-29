import dns.resolver
import requests
import re
from colorama import Fore, Style, init

init(autoreset=True)

def print_title(title):
    print(f"{Fore.GREEN}{Style.BRIGHT}{title}{Style.RESET_ALL}")

def fetch_email_details(email_address):
    details = {}
    try: full_domain = email_address.split('@')[-1]
    except: full_domain = None

    try: username = email_address.split('@')[0]
    except: username = None

    try: domain_name = re.search(r"@([^@.]+)\.", email_address).group(1)
    except: domain_name = None
    
    try: top_level_domain = f".{email_address.split('.')[-1]}"
    except: top_level_domain = None

    try: details["mx_servers"] = [str(record.exchange) for record in dns.resolver.resolve(full_domain, 'MX')]
    except dns.resolver.NoAnswer: details["mx_servers"] = None
    except dns.resolver.NXDOMAIN: details["mx_servers"] = None

    try: details["spf_records"] = [str(record) for record in dns.resolver.resolve(full_domain, 'SPF')]
    except dns.resolver.NoAnswer: details["spf_records"] = None
    except dns.resolver.NXDOMAIN: details["spf_records"] = None

    try: details["dmarc_records"] = [str(record) for record in dns.resolver.resolve(f'_dmarc.{full_domain}', 'TXT')]
    except dns.resolver.NoAnswer: details["dmarc_records"] = None
    except dns.resolver.NXDOMAIN: details["dmarc_records"] = None

    try: details["txt_records"] = [str(record) for record in dns.resolver.resolve(full_domain, 'TXT')]
    except dns.resolver.NoAnswer: details["txt_records"] = None
    except dns.resolver.NXDOMAIN: details["txt_records"] = None

    try: details["srv_records"] = [str(record) for record in dns.resolver.resolve(f"_sip._tcp.{full_domain}", 'SRV')]
    except dns.resolver.NoAnswer: details["srv_records"] = None
    except dns.resolver.NXDOMAIN: details["srv_records"] = None

    try:
        response = requests.get(f"https://email-reputation.api.useinsider.com/lookup/{email_address}")
        details["email_reputation"] = response.json()
    except Exception as err:
        details["email_reputation"] = {"error": str(err)}

    try: details["a_records"] = [str(record) for record in dns.resolver.resolve(full_domain, 'A')]
    except dns.resolver.NoAnswer: details["a_records"] = None
    except dns.resolver.NXDOMAIN: details["a_records"] = None

    try: details["aaaa_records"] = [str(record) for record in dns.resolver.resolve(full_domain, 'AAAA')]
    except dns.resolver.NoAnswer: details["aaaa_records"] = None
    except dns.resolver.NXDOMAIN: details["aaaa_records"] = None

    return details, full_domain, domain_name, top_level_domain, username

def verifier_email(email):
    api_key = '432dfd7cbfec2b733603e519786b4156a789bac3'
    url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}&format=1&type=1&reachable=1&score=1&disposable=1&webmail=1&mx_records=1&organization=1&country=1'
    try:
        response = requests.get(url, headers={'Accept': 'application/json'})
        data = response.json()

        if 'data' in data and 'status' in data['data']:
            if data['data']['status'] == 'valid':
                print(Fore.RED + f"[+] The email address {email} is valid.")
            else:
                print(Fore.RED + f"[-] The email address {email} is invalid.")
    except Exception as err:
        print(Fore.RED + f"Erreur lors de la vérification de l'email: {err}")

email_input = input(f"\n{Fore.RED}[=] Enter Email -> {Style.RESET_ALL}")

if not email_input:
    print(f"{Fore.RED}Email address cannot be empty.{Style.RESET_ALL}")
    exit()

print(f"{Fore.RED}[=] Retrieving Information...{Style.RESET_ALL}")
details, full_domain, domain_name, top_level_domain, username = fetch_email_details(email_input)

print(f"""
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Email         : {Fore.RED}{email_input}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Username      : {Fore.RED}{username}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Domain Name   : {Fore.RED}{domain_name}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} TLD           : {Fore.RED}{top_level_domain}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Full Domain   : {Fore.RED}{full_domain}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} SPF Records   : {Fore.RED}{', '.join(details.get("spf_records", [])) if isinstance(details.get("spf_records"), list) else details.get("spf_records", "N/A")}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} DMARC Records : {Fore.RED}{', '.join(details.get("dmarc_records", []))}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} TXT Records   : {Fore.RED}{','.join(details.get("txt_records", []))}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} SRV Records   : {Fore.RED}{', '.join(details.get("srv_records", [])) if isinstance(details.get("srv_records"), list) else details.get("srv_records", "N/A")}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Email Reputation : {Fore.RED}{details.get("email_reputation", {}).get("reputation", "N/A")}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} A Records     : {Fore.RED}{', '.join(details.get("a_records", []))}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} AAAA Records  : {Fore.RED}{', '.join(details.get("aaaa_records", []))}{Fore.RED}
{Style.RESET_ALL}""")

verifier_email(email_input)
