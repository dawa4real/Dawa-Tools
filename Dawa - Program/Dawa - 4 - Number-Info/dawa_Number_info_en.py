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
    input(Style.BRIGHT + Fore.RED + "\nPress Enter to continue...")

def Reset():
    print(Style.RESET_ALL)

phone_number = input(f"{color.RED}\n{color.INPUT}[=] Phone Number -> {Style.RESET_ALL}")
print(f"{color.RED}{color.WAIT}[=] Retrieving Information...{Style.RESET_ALL}")
try:
    parsed_number = phonenumbers.parse(phone_number, None)
    if phonenumbers.is_valid_number(parsed_number):
        if phone_number.startswith("+"):
            country_code = "+" + phone_number[1:3] 
        else:
            country_code = "None"
        operator = carrier.name_for_number(parsed_number, "fr")
        type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixed"
        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_info = timezones[0] if timezones else None
        country = phonenumbers.region_code_for_number(parsed_number)
        region = geocoder.description_for_number(parsed_number, "en")
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        status = "Valid"
    else:
        formatted_number = "None"
        region = "None"
        country = "None"
        operator = "None"
        type_number = "None"
        timezone_info = "None"
        country_code = "None"
        status = "Invalid"

    print(f"""
{color.RED}[{color.RED}+{color.RED}]{color.RED} Phone Number     : {color.RED}{phone_number}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Formatted        : {color.RED}{formatted_number}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Status           : {color.RED}{status}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Country Code     : {color.RED}{country_code}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Country          : {color.RED}{country}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Region           : {color.RED}{region}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Timezone         : {color.RED}{timezone_info}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Operator         : {color.RED}{operator}{color.RED}
{color.RED}[{color.RED}+{color.RED}]{color.RED} Number Type      : {color.RED}{type_number}{color.RED}
""")
finally:
    pass
