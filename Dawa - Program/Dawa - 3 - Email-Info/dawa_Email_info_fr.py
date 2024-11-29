import dns.resolver
import requests
import re
from colorama import Fore, Style, init
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

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
                print(Fore.RED + f"[+] L'adresse email {email} est valide.")
            else:
                print(Fore.RED + f"[-] L'adresse email {email} est invalide.")
    except Exception as err:
        print(Fore.RED + f"Erreur lors de la vérification de l'email: {err}")

email_input = input(f"\n{Fore.RED}[=] Entrez l'email -> {Style.RESET_ALL}")

if not email_input:
    print(f"{Fore.RED}L'adresse email ne peut pas être vide.{Style.RESET_ALL}")
    exit()

print(f"{Fore.RED}[=] Récupération des informations...{Style.RESET_ALL}")
details, full_domain, domain_name, top_level_domain, username = fetch_email_details(email_input)

print(f"""
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Email         : {Fore.RED}{email_input}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Nom d'utilisateur      : {Fore.RED}{username}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Nom de domaine   : {Fore.RED}{domain_name}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} TLD           : {Fore.RED}{top_level_domain}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Domaine complet   : {Fore.RED}{full_domain}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Enregistrements SPF   : {Fore.RED}{', '.join(details.get("spf_records", [])) if isinstance(details.get("spf_records"), list) else details.get("spf_records", "N/A")}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Enregistrements DMARC : {Fore.RED}{', '.join(details.get("dmarc_records", []))}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Enregistrements TXT   : {Fore.RED}{','.join(details.get("txt_records", []))}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Enregistrements SRV   : {Fore.RED}{', '.join(details.get("srv_records", [])) if isinstance(details.get("srv_records"), list) else details.get("srv_records", "N/A")}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Réputation de l'email : {Fore.RED}{details.get("email_reputation", {}).get("reputation", "N/A")}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Enregistrements A     : {Fore.RED}{', '.join(details.get("a_records", []))}{Fore.RED}
{Fore.RED}[{Fore.RED}+{Fore.RED}]{Fore.RED} Enregistrements AAAA  : {Fore.RED}{', '.join(details.get("aaaa_records", []))}{Fore.RED}
{Style.RESET_ALL}""")


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://epieos.com")

try:
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search-input'))
    )
    search_input.clear()
    search_input.send_keys(email_input)

    tos_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "tos-checkbox"))
    )
    tos_checkbox.click()

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/main/div[6]/div[2]/div[5]/div[2]/button/span'))
    )
    search_button.click()

    time.sleep(5)

    print(Fore.YELLOW + "[!] Veuillez résoudre le captcha !")

    while True:
        if len(driver.window_handles) == 0:
            break
        captcha_resolu = input(Fore.YELLOW + "[!] Fermer la page chrome pour retourner au menu.").lower()
finally:
    driver.quit()
    exit()  
