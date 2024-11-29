import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init
init(autoreset=True)


class color:
    RED = Fore.RED
    WHITE = Fore.RED
    WAIT = Fore.RED
    INPUT = Fore.RED

def Continue():
    input(Style.BRIGHT + Fore.RED + "\nAppuyez sur Entrée pour continuer...")

def Reset():
    print(Style.RESET_ALL)

phone_number = input(f"{color.RED}\n{color.INPUT} Numéro de téléphone -> {Style.RESET_ALL}")
print(f"{color.RED}{color.WAIT} Récupération des informations...{Style.RESET_ALL}")
try:
    parsed_number = phonenumbers.parse(phone_number, None)
    if phonenumbers.is_valid_number(parsed_number):
        if phone_number.startswith("+"):
            country_code = "+" + phone_number[1:3] 
        else:
            country_code = "Aucun"
        operator = carrier.name_for_number(parsed_number, "fr")
        type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_info = timezones[0] if timezones else None
        country = phonenumbers.region_code_for_number(parsed_number)
        region = geocoder.description_for_number(parsed_number, "fr")
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        status = "Valide"
    else:
        formatted_number = "Aucun"
        region = "Aucun"
        country = "Aucun"
        operator = "Aucun"
        type_number = "Aucun"
        timezone_info = "Aucun"
        country_code = "Aucun"
        status = "Invalide"

    print(f"""
{color.RED}[{color.RED}+{color.RED}]{color.RED} Téléphone        : {color.RED}{phone_number}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Formaté          : {color.RED}{formatted_number}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Statut           : {color.RED}{status}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Code Pays        : {color.RED}{country_code}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Pays             : {color.RED}{country}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Région           : {color.RED}{region}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Fuseau Horaire   : {color.RED}{timezone_info}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Opérateur        : {color.RED}{operator}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Type de Numéro   : {color.RED}{type_number}{color.RED}
""")
finally:()