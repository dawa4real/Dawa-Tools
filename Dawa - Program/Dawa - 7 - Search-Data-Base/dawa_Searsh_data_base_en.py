import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

INPUT = Fore.BLUE + "[INPUT] " + Fore.RESET
WAIT = Fore.YELLOW + "[WAIT] " + Fore.RESET
INFO = Fore.GREEN + "[INFO] " + Fore.RESET
ERROR = Fore.RED + "[ERROR] " + Fore.RESET
white = Fore.WHITE
red = Fore.RED
yellow = Fore.YELLOW

path = os.getcwd() 
folder_database_relative = os.path.join(path, "Dawa - Input", "DATA-BASE")
folder_database = os.path.abspath(folder_database_relative)


def Reset():
    global files_searched
    files_searched = 0

try:
    search = input(f"\n{INPUT} Search -> {Style.RESET_ALL}")
    print(f"{WAIT} Searching in DataBase..")

    files_searched = 0

    def check(folder):
        global files_searched
        results_found = False
        print(f"{WAIT} Searching in {white}{folder}")
        for element in os.listdir(folder):
            chemin_element = os.path.join(folder, element)
            if os.path.isdir(chemin_element):
                check(chemin_element)
            elif os.path.isfile(chemin_element):
                try:
                    with open(chemin_element, 'r', encoding='utf-8') as file:
                        line_number = 0
                        files_searched += 1
                        print(f"{files_searched} - {element}")
                        for line in file:
                            line_number += 1
                            if search in line:
                                results_found = True
                                line_info = line.strip().replace(search, f"{yellow}{search}{white}")
                                print(f"""{red}
- Folder : {white}{folder}{red}
- File   : {white}{element}{red}
- Line   : {white}{line_number}{red}
- Result : {white}{line_info}
""")
                except UnicodeDecodeError:
                    try:
                        with open(chemin_element, 'r', encoding='latin-1') as file:
                            files_searched += 1
                            line_number = 0
                            print(f"{files_searched} - {element}")
                            for line in file:
                                line_number += 1
                                if search in line:
                                    results_found = True
                                    line_info = line.strip().replace(search, f"{yellow}{search}{white}")
                                    print(f"""{red}
- Folder : {white}{folder}{red}
- File   : {white}{element}{red}
- Line   : {white}{line_number}{red}
- Result : {white}{line_info}
""")
                    except Exception as e:
                        print(f"{ERROR} Error reading file \"{white}{element}{red}\": {white}{e}")
                except Exception as e:
                    print(f"{ERROR} Error reading file \"{white}{element}{red}\": {white}{e}")
        return results_found

    results_found = check(folder_database)
    if not results_found:
        print(f"{INFO} No result found for \"{white}{search}{red}\".")

    print(f"{INFO} Total files searched: {white}{files_searched}")

except Exception as e:
    print(f"{ERROR} Error during search: {white}{e}")

Reset()  
