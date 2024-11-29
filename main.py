from colorama import init, Fore, Back, Style  
import webbrowser
import subprocess
import os
from pystyle import System
import time

System.Title(">DAWA-TOOL<")

def close_cmd():
    subprocess.call('exit', shell=True)

path =os.getcwd () 
dawa_Name_finder_fr =fr"{path}\Dawa - Program\Dawa - 1 - Name-Tracker\dawa_Name_finder_fr.py"
dawa_Name_finder_en =fr"{path}\Dawa - Program\Dawa - 1 - Name-Tracker\dawa_Name_finder_en.py"
dawa_Email_osint_fr =fr"{path}\Dawa - Program\Dawa - 2 - Email-Tracker\dawa_Email_osint_fr.py"
dawa_Email_osint_en =fr"{path}\Dawa - Program\Dawa - 2 - Email-Tracker\dawa_Email_osint_en.py"
dawa_Email_info_fr =fr"{path}\Dawa - Program\Dawa - 3 - Email-Info\dawa_Email_info_fr.py"
dawa_Email_info_en =fr"{path}\Dawa - Program\Dawa - 3 - Email-Info\dawa_Email_info_en.py"
dawa_Number_info_fr =fr"{path}\Dawa - Program\Dawa - 4 - Number-Info\dawa_Number_info_fr.py"
dawa_Number_info_en =fr"{path}\Dawa - Program\Dawa - 4 - Number-Info\dawa_Number_info_en.py"
dawa_dox_fr =fr"{path}\Dawa - Program\Dawa - 5 - Dox-Creator\dawa_dox_fr.py"
dawa_dox_en =fr"{path}\Dawa - Program\Dawa - 5 - Dox-Creator\dawa_dox_en.py"
dawa_simple_dox_fr =fr"{path}\Dawa - Program\Dawa - 6 - Simple-Dox-Creator\dawa_simple_dox_fr.py"
dawa_simple_dox_en =fr"{path}\Dawa - Program\Dawa - 6 - Simple-Dox-Creator\dawa_simple_dox_en.py"
dawa_Searsh_data_base_fr =fr"{path}\Dawa - Program\Dawa - 7 - Search-Data-Base\dawa_Searsh_data_base_fr.py"
dawa_Searsh_data_base_en =fr"{path}\Dawa - Program\Dawa - 7 - Search-Data-Base\dawa_Searsh_data_base_en.py"
dawa_Ip_lookup_fr =fr"{path}\Dawa - Program\Dawa - 8 - Ip-Lookup\dawa_Ip_lookup_fr.py"
dawa_Ip_lookup_en =fr"{path}\Dawa - Program\Dawa - 8 - Ip-Lookup\dawa_Ip_lookup_en.py"
dawa_Email_bomber_fr =fr"{path}\Dawa - Program\Dawa - 9 - Email-Bomber\dawa_Email_bomber_fr.py"
dawa_Email_bomber_en =fr"{path}\Dawa - Program\Dawa - 9 - Email-Bomber\dawa_Email_bomber_en.py"
dawa_Email_spam_reset_fr =fr"{path}\Dawa - Program\Dawa - 10 - Email-Bomber-Reset\dawa_Email_spam_reset_fr.py"
dawa_Email_spam_reset_en =fr"{path}\Dawa - Program\Dawa - 10 - Email-Bomber-Reset\dawa_Email_spam_reset_en.py"
dawa_gen_en =fr"{path}\Dawa - Program\Dawa - 11 - Generator\dawa_gen_en.py"
dawa_gen_fr =fr"{path}\Dawa - Program\Dawa - 11 - Generator\dawa_gen_fr.py"
dawa_Nitro_gen_fr =fr"{path}\Dawa - Program\Dawa - 12 - Generator-Nitro\dawa_Nitro_gen_fr.py"
dawa_Nitro_gen_en =fr"{path}\Dawa - Program\Dawa - 12 - Generator-Nitro\dawa_Nitro_gen_en.py"
dawa_IP_all_lookup_fr =fr"{path}\Dawa - Program\Dawa - 13 - IP-All-Lookup\dawa_IP_all_lookup_fr.py"
dawa_IP_all_lookup_en =fr"{path}\Dawa - Program\Dawa - 13 - IP-All-Lookup\dawa_IP_all_lookup_en.py"
dawa_IP_localisation_fr =fr"{path}\Dawa - Program\Dawa - 14 - IP-Localisation\dawa_IP_localisation_fr.py"
dawa_IP_localisation_en =fr"{path}\Dawa - Program\Dawa - 14 - IP-Localisation\dawa_IP_localisation_en.py"
dawa_IP_operator_fr =fr"{path}\Dawa - Program\Dawa - 15 - IP-Operator\dawa_IP_operator_fr.py"
dawa_IP_operator_en =fr"{path}\Dawa - Program\Dawa - 15 - IP-Operator\dawa_IP_operator_en.py"
dawa_IP_openport_fr =fr"{path}\Dawa - Program\Dawa - 16 - IP-OpenPorts\dawa_IP_openport_fr.py"
dawa_IP_openport_en =fr"{path}\Dawa - Program\Dawa - 16 - IP-OpenPorts\dawa_IP_openport_en.py"
dawa_IP_pinger_fr =fr"{path}\Dawa - Program\Dawa - 17 - IP-Pinger\dawa_IP_pinger_fr.py"
dawa_IP_pinger_en =fr"{path}\Dawa - Program\Dawa - 17 - IP-Pinger\dawa_IP_pinger_en.py"
dawa_IP_gen_fr =fr"{path}\Dawa - Program\Dawa - 18 - IP-Generator\dawa_IP_gen_fr.py"
dawa_IP_gen_en =fr"{path}\Dawa - Program\Dawa - 18 - IP-Generator\dawa_IP_gen_en.py"

init(autoreset=True)

def clear_screen():
    subprocess.call('cls', shell=True)


import webbrowser
import os

discord_link = 'https://discord.gg/RDQtQQUbfC'
gif_path = fr"{path}\Dawa - Screen\Star !!.gif"
github_link = 'https://github.com/DAWA0/Dawa-Multitool'


if not os.path.isfile('first_execution.txt'):
    webbrowser.open(discord_link)
    webbrowser.open(github_link)
    time.sleep(0.5)
    os.startfile(gif_path)
    with open('first_execution.txt', 'w') as file:
        file.write('This file marks the first execution.')




def menu1():
    print(Fore.RED + '''
      

          
















          
████████████████████████████████████████████                      ╔═════════════════════════╗
█▌                                        ▐█                      ║       DISCORD           ║
█▌   ██████╗  █████╗ ██╗    ██╗ █████╗    ▐█╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╠═════════════════════════╣
█▌   ██╔══██╗██╔══██╗██║    ██║██╔══██╗   ▐█╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩║ x. fullysafe.           ║
█▌   ██║  ██║███████║██║ █╗ ██║███████║   ▐█                      ║ x. .gg/RDQtQQUbfC       ║
█▌   ██║  ██║██╔══██║██║███╗██║██╔══██║   ▐█                      ╚═════════════════════════╝
█▌   ██████╔╝██║  ██║╚███╔███╔╝██║  ██║   ▐█
█▌   ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ▐█╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
█▌                                        ▐█╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╠╠╠╠╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩║║║║
████████████████████████████████████████████                         ╠╣╠╣                                      ╠╣╠╣
╠╣╠╣                                                                 ╠╣╠╣                                      ╠╣╠╣
╠╣╠╣                                                                 ╠╣╠╣                                      ╠╣╠╣
╠╣╠╣                                                                 ╠╣╠╣                                      ╠╣╠╣
╠╣╠╣                                                                 ╠╣╠╣                                      ╠╣╠╣  
╠╣╠╣                      ╔═════════════════════════╗                ╠╣╠╣ ╔═════════════════════════╗          ╠╣╠╣
╠╣╠╣                      ║       GITHUB            ║                ╠╣╠╣ ║     IMPORTANT           ║          ╠╣╠╣
╠╬╠╠╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╠═════════════════════════╣                ╠╬╠╠╦╠═════════════════════════╣          ╠╣╠╣
╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩║ 1. Link Add stars       ║                ╚╩╩╩╩║ N. NEXT-PAGE            ║          ╠╣╠╣
                          ║    for more options     ║                     ║ B. BACK-PAGE            ║          ╠╣╠╣
                          ╚═════════════════════════╝                     ╚═════════════════════════╝          ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                                                                                                                     
''')


def main():
    while True:
        clear_screen()
        menu1()
        option = input(Fore.RED + '''
                                                                                                               ╠╣╠╣
  ┌──(user@dawa)-[~/Home]                                                                                      ╠╣╠╣
  │                                                                                                            ╠╣╠╣
  └─$ ''')               

        if option == "1":
            urlgithub = 'https://github.com/DAWA0/Dawa-Multitool'
            webbrowser.open(urlgithub)
            print(Fore.GREEN + "[+] Succès !")
        elif option == "N":
            menu2()

        elif option == "3":
            close_cmd()
            break




def menu2():
    while True:
        clear_screen()
        print(Fore.RED + r"""
              

                                                                                                               ╠╣╠╣
          ________________________________________________                                                     ╠╣╠╣
         //                     OSINT                     \\                                                   ╠╣╠╣
        ||    ___________________________________________  ||                                                  ╠╣╠╣
        ||   ||                                        ||  ||                                                  ╠╣╠╣
        ||   ||  C:\> 1. Doxbin                        ||  ||                                                  ╠╣╠╣
        ||   ||  C:\> 2. Osint-Framework               ||  ||                                                  ╠╣╠╣
        ||   ||  C:\> 3. Name-Finder                   ||  ||╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╣╣╠╣
        ||   ||  C:\> 4. Email-Tracker                 ||  ||╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╣╣╠╣
        ||   ||  C:\> 5. Email-Info                    ||  ||                                                  ╠╣╠╣
        ||   ||  C:\> 6. Number-Info                   ||  ||╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╣╣╠╣
        ||   ||  C:\> 7. Dox-Creator                   ||  ||╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╣╣╠╣
        ||   ||  C:\> 8. Simple Dox-Creator            ||  ||                                                  ╠╣╠╣
        ||   ||  C:\> 9. Search DataBase               ||  ||╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╣╣╠╣
        ||   ||  C:\> x. Star-for-unlock               ||  ||╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╣╣╠╣
        ||   ||  C:\> x. Star-for-unlock               ||  ||                                                  ╠╣╠╣
        ||   ||  C:\> x. Star-for-unlock               ||  ||                                                  ╠╣╠╣
        ||   ||________________________________________||  ||                                                  ╠╣╠╣
        ||                                                 ||                                                  ╠╣╠╣
        \\_________________________________________________//                                                  ╠╣╠╣
                \___________________________________/                                                          ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
        """)
        option = input(Fore.RED + r'''
                                                                                                               ╠╣╠╣
  ┌──(user@dawa)-[~/Menu1]                                                                                     ╠╣╠╣
  │                                                                                                            ╠╣╠╣
  └─$ ''')

        if option == "x":
            urlgithub = 'https://github.com/DAWA0/Dawa-Multitool'
            webbrowser.open(urlgithub)
            print(Fore.GREEN + "[+] Succès !")        

        
        if option == "1":
            urldoxbin = 'https://doxbin.com/'
            webbrowser.open(urldoxbin)
            print(Fore.GREEN + "[+] Succès !")

        if option == "2":
            urldoxbin = 'https://osintframework.com/'
            webbrowser.open(urldoxbin)
            print(Fore.GREEN + "[+] Succès !")


        if option == "3":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Name_finder_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Name_finder_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)


        if option == "4":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Email_osint_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Email_osint_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)

        if option == "5":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Email_info_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Email_info_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)

        if option == "6":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Number_info_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Number_info_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)

        if option == "7":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_dox_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_dox_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)           

        if option == "8":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_simple_dox_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_simple_dox_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)

        if option == "9":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Searsh_data_base_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Searsh_data_base_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
                
        if option == "10":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Ip_lookup_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Ip_lookup_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)


        if option == "N":
            menu3()
            break
       
        if option == "B":
            menu1()
            break






def menu3():
    while True:
        clear_screen()
        print(Fore.RED + '''
              

                                                                                                               ╠╣╠╣
                                   ╔══════════════════════════════════════════════════════════╗                ╠╣╠╣
  ╔═════════════╗                  ║ 88                                         88            ║                ╠╣╠╣
  ║ 3.DDOS-IP   ║╗                 ║ 88                                         88            ║                ╠╣╠╣
  ╚═════════════╝║                 ║ 88                                         88            ║╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╠╣╠╣
                 ║                 ║ 88,dPPYba,   ,adPPYba,  88,dPYba,,adPYba,  88,dPPYba,    ║╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╠╣╠╣
                 ║                 ║ 88P'    "8a a8"     "8a 88P'   "88"    "8a 88P'    "8a   ║                ╠╣╠╣
                 ╚═╗               ║ 88       d8 8b       d8 88      88      88 88       d8   ║                ╠╣╠╣
      ╔════════════╩═════╦╦╦╦╦╦╦╦╦╦╣ 88b,   ,a8" "8a,   ,a8" 88      88      88 88b,   ,a8"   ║                ╠╣╠╣
      ║ x.DDOS          ╔╩╩╩╩╩╩╩╩╩╩╣ 8Y"Ybbd8"'   `"YbbdP"'  88      88      88 8Y"Ybbd8"'    ║                ╠╣╠╣
      ╚═╦═╦═════════════╝          ║                                                          ║                ╠╣╠╣
        ║ ║                        ╚═════════════════════╦╦╦╦═════════════════════════════════╝                ╠╣╠╣
        ║ ║╔══════════════════╗                          ╠╣╠╣                  ╔═══════════════════════════╗   ╠╣╠╣
        ║ ╚╣ 4.DDOS-WebSite   ║                         ╔╠╣╠╣╗                ╔╣ 1.Email-Bomber(Gmail)     ║   ╠╣╠╣
        ║  ╚══════════════════╝                         ║╠╣╠╣║                ║╚═══════════════════════════╝   ╠╣╠╣
        ║                                 ╔═════════════╩╩╩╩╩╩═════╗          ║                                ╠╣╠╣
        ║                                 ║ x.Email-Bomber         ╠══════════╣                                ╠╣╠╣
        ║                                 ╚════════════════╦═══════╝          ║                                ╠╣╠╣
        ║                                                  ║                  ║╔═══════════════════════════╗   ╠╣╠╣
    ╔═══╩═════════════════════════════════╗                ║                  ╚╣ 2.Email-Bomber(Pass-Reset)║   ╠╣╠╣
    ║ A DDoS makes a website inaccessible.║                ║                   ╚═══════════════════════════╝   ╠╣╠╣
    ╚═════════════════════════════════════╝                ║                                                   ╠╣╠╣
                                        ╔══════════════════╩═══════════════════╗                               ╠╣╠╣
                                        ║ An email bomber saturates an mailbox ║                               ╠╣╠╣
                                        ╚══════════════════════════════════════╝                               ╠╣╠╣
        ''')
        option = input(Fore.RED + '''
                                                                                                               ╠╣╠╣
  ┌──(user@dawa)-[~/Menu2]                                                                                     ╠╣╠╣
  │                                                                                                            ╠╣╠╣
  └─$ ''')

        if option == "x":
            urlgithub = 'https://github.com/DAWA0/Dawa-Multitool'
            webbrowser.open(urlgithub)
            print(Fore.GREEN + "[+] Succès !")   

        if option == "N":
            menu4()
            break
       
        if option == "B":
            menu2()
            break


        if option == "1":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Email_bomber_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Email_bomber_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "2":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Email_spam_reset_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Email_spam_reset_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "3":
            webbrowser.open("https://stresser.zone/hub")
        if option == "4":
            webbrowser.open("https://stresser.zone/hub")

def menu4():
    while True:
        clear_screen()
        print(Fore.RED + """    

                 ·▄▄▄▄   ▄▄▄· ▄▄▌ ▐ ▄▌ ▄▄▄·                   ║                                                ╠╣╠╣
                 ██▪ ██ ▐█ ▀█ ██· █▌▐█▐█ ▀█                   ║                                                ╠╣╠╣
                 ▐█· ▐█▌▄█▀▀█ ██▪▐█ ▐▌▄█▀▀█  Nuker-Bot        ║                                                ╠╣╠╣
                 ██. ██ ▐█ ▪▐▌▐█▌██▐█▌▐█ ▪▐▌                  ║                                                ╠╣╠╣
                 ▀▀▀▀▀•  ▀  ▀  ▀▀▀▀ ▀▪ ▀  ▀                   ║                                                ╠╣╠╣
       Support Discord : https://discord.gg/tdTUvwVpMY        ║                                                ╠╣╠╣
                                                              ║                                                ╠╣╠╣
  >━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━< ║                                                ╠╣╠╣
                        $>1. Start                            ║                                                ╠╣╠╣
  >━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━< ║╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╣╣╠╣
       ╔═                                            ═╗       ║╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╣╣╠╣
        $>x. Config token>"\Dawa - Input\Discord-Nuker        ║                                                ╠╣╠╣
       ╚═                                            ═╝       ║                                                ╠╣╠╣
       ╔══════                                 ══════╗        ║                                                ╠╣╠╣
       ║ $>.  !mchannel    >Mass create channels<    ║        ║                                                ╠╣╠╣
       ║ $>.  !mspam       >Mass ping channel<       ║        ║                                                ╠╣╠╣
         $>.  !mrole       >Mass create roles<                ║                                                ╠╣╠╣
         $>.  !dchannel    >Delete all channels<              ║                                                ╠╣╠╣
         $>.  !drole       >Delete all roles<                 ║                                                ╠╣╠╣
         $>.  !demoji      >Delete all emotes<                ║                                                ╠╣╠╣
       ║ $>.  !mkick       >Mass kick<               ║        ║                                                ╠╣╠╣
       ║ $>.  !mban        >Mass ban<                ║        ║                                                ╠╣╠╣
       ╚══════                                 ══════╝        ║                                                ╠╣╠╣
              """)
        option = input(Fore.RED + r'''
                                                                                                               ╠╣╠╣
  ┌──(user@dawa)-[~/Menu1]                                                                                     ╠╣╠╣
  │                                                                                                            ╠╣╠╣
  └─$ ''')

        if option == '1':
            file_path = fr"{path}\Dawa - Program\Dawa - 19 - Discord-Nuker\index.js"
            subprocess.run(["node", file_path], shell=True)
        elif option.lower() == 'x':
            print("Configuration du token...")
        else:
            print("Option invalide, veuillez réessayer.")


        if option == "N":
            menu5()
            break
       
        if option == "B":
            menu3()
            break

def menu5():
    while True:
        clear_screen()
        print(Fore.RED + fr'''
              
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                             ╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╣║╠╣
                                                             ╠╣╠╣╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╣║╠╣
                ╔════════════════════════════════════════════╩╩╩╩═════════════════════════╗                    ╠╣╠╣
                ║                                                                         ║                    ╠╣╠╣
                ║   ╔═══════════╗      ___ ____       _____            _       _ _        ║                    ╠╣╠╣
                ║   ║   / _ \   ║     |_ _|  _ \     | ____|_  ___ __ | | ___ (_) |_      ║                    ╠╣╠╣
                ║   ║ \_\(_)/_/ ║      | || |_) |____|  _| \ \/ / '_ \| |/ _ \| | __|     ║                    ╠╣╠╣
                ║   ║  _//o\\_  ║      | ||  __/_____| |___ >  <| |_) | | (_) | | |_      ║                    ╠╣╠╣
                ║   ║   /   \   ║     |___|_|        |_____/_/\_\ .__/|_|\___/|_|\__|     ║                    ╠╣╠╣
                ║   ╚═══════════╝                               |_|                       ║                    ╠╣╠╣
                ║                                                                         ║                    ╠╣╠╣
                ╚══════════════════╦══════════════════════════════════════════════════════╝                    ╠╣╠╣
                                   ║                                                                           ╠╣╠╣
                                   ║                                                                           ╠╣╠╣
                                 ╔═╩════════════════╗     ╔════════════════════╗     ╔════════════════╗        ╠╣╠╣
                                 ║ 1. Web-Lookup    ╠═════╣ 2. IP-Localisation ╠═════╣ 3. IP-Operator ║        ╠╣╠╣
                                 ╚══════════════════╝     ╚════════════════════╝     ╚═════════╦══════╝        ╠╣╠╣
                                                                                               ║               ╠╣╠╣
       ╔════════════════╗     ╔════════════╗     ╔══════════════╗      ╔══════════════════╗    ║               ╠╣╠╣
       ║7. IP-Generator ╠═════╣ 6. IP-Ddos ╠═════╣ 5. IP-Pinger ╠══════╣ 4. IP-OpenPorts  ╠════╝               ╠╣╠╣
       ╚════════════════╝     ╚════════════╝     ╚══════════════╝      ╚══════════════════╝                    ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
        ''')
        option = input(Fore.RED + '''
                                                                                                               ╠╣╠╣
  ┌──(user@dawa)-[~/Menu3]                                                                                     ╠╣╠╣
  │                                                                                                            ╠╣╠╣
  └─$ ''')
        
        if option == "x":
            urlgithub = 'https://github.com/DAWA0/Dawa-Multitool'
            webbrowser.open(urlgithub)
            print(Fore.GREEN + "[+] Succès !")   

        if option == "N":
            menu6()
            break
       
        if option == "B":
            menu4()
            break


        if option == "6":
            webbrowser.open("https://stresser.zone/hub")
        if option == "1":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_IP_all_lookup_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_IP_all_lookup_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)        
        
        if option == "2":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_IP_localisation_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_IP_localisation_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "3":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_IP_operator_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_IP_operator_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "4":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_IP_openport_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_IP_openport_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "5":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_IP_pinger_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_IP_pinger_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)

        if option == "7":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_IP_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_IP_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)





def menu6():
    while True:
        clear_screen()
        print(Fore.RED + '''
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                             o                                                                                 ╠╣╠╣
                          o^/|\^o                                                                              ╠╣╠╣
                       o_^|\/*\/|^_o                                                                           ╠╣╠╣
                      o\*`'.\|/.'`*/o                                                                          ╠╣╠╣
                       \\\\\\\\\\\|//////                                                                           ╠╣╠╣
                        {><><@><><}                                                                            ╠╣╠╣
                        `"""""""""`                                                                            ╠╣╠╣
       ╔══════════════════════════════════════════════════════════════════════╗                                ╠╣╠╣
       ║                                                                      ║                                ╠╣╠╣
       ║ ██████   █████  ██     ██  █████         ██████  ███████ ███    ██   ╠╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╣╣╠╣
       ║ ██   ██ ██   ██ ██     ██ ██   ██       ██       ██      ████   ██   ╠╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣
       ║ ██   ██ ███████ ██  █  ██ ███████ █████ ██   ███ █████   ██ ██  ██   ╠╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣╠╣
       ║ ██   ██ ██   ██ ██ ███ ██ ██   ██       ██    ██ ██      ██  ██ ██   ║╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╣╣╠╣
       ║ ██████  ██   ██  ███ ███  ██   ██        ██████  ███████ ██   ████   ║                                ╠╣╠╣
       ╚══════════════════════════════════════════════════════════════════════╝                                ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠║╠╣
                    ╔═════════════════════════════════════════╗                                                ╠║╠╣
                    ║ <1.Discord-Nitro>    <5.Apple Giftcard> ║                                                ╠╣╠╣
                    ║ <2.Amazon Giftcard>  <6.Steam Giftcard> ╠╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╣╣╠╣
                    ║ <3.Netflix Giftcard> <7.Google Play>    ╠╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╣╣╠╣
                    ║ <4.Roblox Giftcard>  <8.Spotify Gift>   ║                                                ╠╣╠╣
                    ╚═════════════════════════════════════════╝                                                ╠╣╠╣
                                                                                                               ╠╣╠╣
        ''')
        option = input(Fore.RED + '''
                                                                                                               ╠╣╠╣
  ┌──(user@dawa)-[~/Menu4]                                                                                     ╠╣╠╣
  │                                                                                                            ╠╣╠╣
  └─$ ''')
        if option == "1":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_Nitro_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_Nitro_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)        
        
        if option == "2":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "3":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "4":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "5":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "6":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "7":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)
        if option == "8":
            try:
                langue = input("""[?] Are you French or English (fr, en)? : """)
                if langue == "fr":
                    subprocess.run(["python", dawa_gen_fr])
                elif langue == "en":
                    subprocess.run(["python", dawa_gen_en])
                input(Fore.YELLOW + "[!] Press enter to continue ...")  
            except FileNotFoundError:
                print("The specified file can not be found.")
            except Exception as e:
                print("An error has occurred :", e)


        if option == "N":
            menu7()
            break

        if option == "B":
            menu5()
            break

        if option == "x":
            urlgithub = 'https://github.com/DAWA0/Dawa-Multitool'
            webbrowser.open(urlgithub)
            print(Fore.GREEN + "[+] Succès !")   


def menu7():
    while True:
        clear_screen()
        print(Fore.RED + '''
              

                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╠╣╠╣
                                                                                                               ╠╣╠╣
 +--^----------,--------,-----,--------^-,    ▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀    █     █░▓█████  ▄▄▄▄       ╠╣╠╣
 | |||||||||   `--------'     |          O    ▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▓█░ █ ░█░▓█   ▀ ▓█████▄     ╠╣╠╣
 `+---------------------------^----------|    ░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▒█░ █ ░█ ▒███   ▒██▒ ▄██    ╠╣╠╣
   `\_,---------,---------,--------------'    ░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀      ╠╣╠╣
      / XXXXXX /'|       /'                   ░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ░░██▒██▓ ░▒████▒░▓█  ▀█▓    ╠╣╠╣
     / XXXXXX /  `\    /'                      ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒    ╠╣╠╣
    / XXXXXX /`-------'                        ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░     ▒ ░ ░   ░ ░  ░▒░▒   ░     ╠╣╠╣
   / XXXXXX /                                  ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░      ░   ░     ░    ░    ░     ╠╣╠╣
  / XXXXXX /                                     ░          ░  ░   ░     ░  ░          ░       ░  ░ ░          ╠╣╠╣
 (________(                                    ░                                                         ░     ╠╣╠╣
  `------'                                                                                                     ╠╣╠╣
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
           1  Mail2Tor              2  The Wiki              3  Publica               4   DuckGo               ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
           5 SecureDrop             6  Sci-Hub               7  The CIA               8 Hidden Answers         ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
          9  DDoSNow               10 IPLogger              11 Grabify              12  Whatstheirip           ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         13  Doxbin                14 OSINT Industries      15 Epieos              16 Nuwber                   ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         17 OSINT Framework         18 Whatsmyname           19 DDoSNow               20 Stresser.zone         ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         21 Stresse.ru              22 Stresse.cat          23 StarkStresser        24 DDoS.services           ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         25 Spylink               26 IPInfo                 27 Torch                  28 Danex                 ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         29 Sentor                 30 Dark Mixer             31 Mixabit               32 EasyCoin              ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         33 Onionwallet            34 VirginBitcoin          35 Stresser              36 Deep Market           ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         37 DrChronic              38 TomAndJerry            39 420prime              40 Can*abisUK            ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         41 DeDope                 42 AccMarket              43 Cardshop              44 Darkmining            ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗          ╔══         ══╗           ╠╣╠╣
         45 MobileStore            46 EuroGuns              47 UKpassports            48 ccPal                 ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝          ╚══         ══╝           ╠╣╠╣
                                                                                                               ╠╣╠╣
          ╔══         ══╗          ╔══         ══╗                                                             ╠╣╠╣
         49 Webuybitcoins          50 Database                                                                 ╠╣╠╣
          ╚══         ══╝          ╚══         ══╝                                                             ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╠╣╠╣
                                                                                                               ╠╣╠╣
 +--^----------,--------,-----,--------^-,    ▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀    █     █░▓█████  ▄▄▄▄       ╠╣╠╣
 | |||||||||   `--------'     |          O    ▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▓█░ █ ░█░▓█   ▀ ▓█████▄     ╠╣╠╣
 `+---------------------------^----------|    ░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▒█░ █ ░█ ▒███   ▒██▒ ▄██    ╠╣╠╣
   `\_,---------,---------,--------------'    ░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀      ╠╣╠╣
      / XXXXXX /'|       /'                   ░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ░░██▒██▓ ░▒████▒░▓█  ▀█▓    ╠╣╠╣
     / XXXXXX /  `\    /'                      ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒    ╠╣╠╣
    / XXXXXX /`-------'                        ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░     ▒ ░ ░   ░ ░  ░▒░▒   ░     ╠╣╠╣
   / XXXXXX /                                  ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░      ░   ░     ░    ░    ░     ╠╣╠╣
  / XXXXXX /                                     ░          ░  ░   ░     ░  ░          ░       ░  ░ ░          ╠╣╠╣
 (________(                                    ░                                                         ░     ╠╣╠╣
  `------'                                                                                                     ╠╣╠╣
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╠╣╠╣
              ''')
        option = input(Fore.RED + '''
                                                                                                               ╠╣╠╣
  ┌──(user@dawa)-[~/Menu5]                                                                                     ╠╣╠╣
  │                                                                                                            ╠╣╠╣
  └─$ ''')


        if option == "N":
            menu8()
            break
       
        if option == "B":
            menu6()
            break

        if option == '1':
            print(Fore.RED + "+ Mail2Tor: http://mail2tor2zyjdctd.onion/")
        elif option == '2':
            print(Fore.RED + "+ The Hidden Wiki: http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page")
        elif option == '3':
            print(Fore.RED + "+ ProPublica: https://www.propub3r6espa33w.onion/")
        elif option == '4':
            print(Fore.RED + "+ DuckDuckGo: http://3g2upl4pq6kufc4m.onion/")
        elif option == '5':
            print(Fore.RED + "+ SecureDrop: https://secrdrop5wyphb5x.onion/")
        elif option == '6':
            print(Fore.RED + "+ Sci-Hub: http://scihub22266oqcxt.onion/")
        elif option == '7':
            print(Fore.RED + "+ The CIA: http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/")
        elif option == '8':
            print(Fore.RED + "+ Hidden Answers: http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/")
        elif option == '9':
            print(Fore.RED + "+ DDoSNow: https://ddosnow.com/")
        elif option == '10':
            print(Fore.RED + "+ IPLogger: https://iplogger.org/")
        elif option == '11':
            print(Fore.RED + "+ Grabify: https://grabify.link/")
        elif option == '12':
            print(Fore.RED + "+ Whatstheirip: https://whatstheirip.tech/")
        elif option == '13':
            print(Fore.RED + "+ Doxbin: https://doxbin.net/")
        elif option == '14':
            print(Fore.RED + "+ OSINT Industries: https://osint.industries/")
        elif option == '15':
            print(Fore.RED + "+ Epieos: https://epieos.com/")
        elif option == '16':
            print(Fore.RED + "+ Nuwber: https://nuwber.fr/")
        elif option == '17':
            print(Fore.RED + "+ OSINT Framework: https://osintframework.com/")
        elif option == '18':
            print(Fore.RED + "+ Whatsmyname: https://whatsmyname.app/")
        elif option == '19':
            print(Fore.RED + "+ DDoSNow: https://ddosnow.com/")
        elif option == '20':
            print(Fore.RED + "+ Stresser.zone: https://stresser.zone/")
        elif option == '21':
            print(Fore.RED + "+ Stresse.ru: https://stresse.ru/")
        elif option == '22':
            print(Fore.RED + "+ Stresse.cat: https://stresse.cat/")
        elif option == '23':
            print(Fore.RED + "+ StarkStresser: https://starkstresser.net/")
        elif option == '24':
            print(Fore.RED + "+ DDoS.services: https://ddos.services/")
        elif option == '25':
            print(Fore.RED + "+ Spylink: https://www.spylink.net/")
        elif option == '26':
            print(Fore.RED + "+ IPInfo: https://ipinfo.io/")
        elif option == '27':
            print(Fore.RED + "+ Torch: http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/")
        elif option == '28':
            print(Fore.RED + "+ Danex: http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/")
        elif option == '29':
            print(Fore.RED + "+ Sentor: http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/")
        elif option == '30':
            print(Fore.RED + "+ Dark Mixer: http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/")
        elif option == '31':
            print(Fore.RED + "+ Mixabit: http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/")
        elif option == '32':
            print(Fore.RED + "+ EasyCoin: http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/")
        elif option == '33':
            print(Fore.RED + "+ Onionwallet: http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/")
        elif option == '34':
            print(Fore.RED + "+ VirginBitcoin: http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/")
        elif option == '35':
            print(Fore.RED + "+ Stresser: http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/")
        elif option == '36':
            print(Fore.RED + "+ Deep Market: http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/")
        elif option == '37':
            print(Fore.RED + "+ DrChronic: http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/")
        elif option == '38':
            print(Fore.RED + "+ TomAndJerry: http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/")
        elif option == '39':
            print(Fore.RED + "+ 420prime: http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/")
        elif option == '40':
            print(Fore.RED + "+ Can*abisUK: http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/")
        elif option == '41':
            print(Fore.RED + "+ DeDope: http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/")
        elif option == '42':
            print(Fore.RED + "+ AccMarket: http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/")
        elif option == '43':
            print(Fore.RED + "+ Cardshop: http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/")
        elif option == '44':
            print(Fore.RED + "+ Darkmining: http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/")
        elif option == '45':
            print(Fore.RED + "+ MobileStore: http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/")
        elif option == '46':
            print(Fore.RED + "+ EuroGuns: http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/")
        elif option == '47':
            print(Fore.RED + "+ UKpassports: http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/")
        elif option == '48':
            print(Fore.RED + "+ ccPaypal: http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/")
        elif option == '49':
            print(Fore.RED + "+ Webuybitcoins: http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/")
        elif option == '50':
            print(Fore.RED + "+ Data-Base: https://discord.gg/GgXq3nJ7QZ")
        input(Fore.YELLOW + "[!] Press enter to continue ...")
    
        if option == "x":
            urlgithub = 'https://github.com/DAWA0/Dawa-Multitool'
            webbrowser.open(urlgithub)
            print(Fore.GREEN + "[+] Succès !")   


def menu8():
    while True:
        clear_screen()
        print(Fore.RED + r"""
              

                                                                                                               ╠╣╠╣
                               _____ _          ___                    _                                       ╠╣╠╣
                              |_   _| |_ _ _   |  _|___ ___    _ _ ___|_|___ ___                               ╠╣╠╣
                                | | |   |_'_|  |  _| . |  _|  | | |_ -| |   | . |                              ╠╣╠╣
                                |_| |_|_|_,_|  |_| |___|_|    |___|___|_|_|_|_  |                              ╠╣╠╣
                                                                            |___|                              ╠╣╠╣
                                                                                                               ╠╣╠╣
                   ██████╗  █████╗ ██╗    ██╗ █████╗               ████████╗ ██████╗  ██████╗ ██╗              ╠╣╠╣
                   ██╔══██╗██╔══██╗██║    ██║██╔══██╗              ╚══██╔══╝██╔═══██╗██╔═══██╗██║              ╠╣╠╣
                   ██║  ██║███████║██║ █╗ ██║███████║    █████╗       ██║   ██║   ██║██║   ██║██║              ╠╣╠╣
                   ██║  ██║██╔══██║██║███╗██║██╔══██║    ╚════╝       ██║   ██║   ██║██║   ██║██║              ╠╣╠╣
                   ██████╔╝██║  ██║╚███╔███╔╝██║  ██║                 ██║   ╚██████╔╝╚██████╔╝███████╗         ╠╣╠╣
                   ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝                 ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝         ╠╣╠╣
                                                                                                               ╠╣╠╣
                                            ╔══════════════════════════╗                                       ╠╣╠╣
                                            ║ 1. STAR FOR MORE OPTION  ║                                       ╠╣╠╣
                                            ╚══════════════════════════╝                                       ╠╣╠╣
                                                                                                               ╠╣╠╣
                                                                                                               ╠╣╠╣
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣╣╠╣
                                                                                                               ╠╣╠╣
Github : https://github.com/DAWA0/Dawa-Multitool                                             60  Star for v2.0 ╠╣╠╣
Discord : https://discord.gg/GgXq3nJ7QZ                                                      DAWA-TOOL         ╠╣╠╣
Created by >fullsafe.<                                                                       Version:     v1.0 ╠╣╠╣
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣╣╠╣
        """)
        option = input(Fore.RED + r'''
                                                                                                               ╠╣╠╣
  ┌──(user@dawa)-[~/Menu1]                                                                                     ╠╣╠╣
  │                                                                                                            ╠╣╠╣
  └─$ ''')

        if option == "1":
            urlgithub = 'https://github.com/DAWA0/Dawa-Multitool'
            webbrowser.open(urlgithub)
            print(Fore.GREEN + "[+] Succès !")   


        if option == "B":
            menu7()
            break
        if option == "b":
            menu7()
            break



if __name__ == "__main__":
 main()
