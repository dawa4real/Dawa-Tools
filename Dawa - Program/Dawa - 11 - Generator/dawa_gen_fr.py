import random
import os
import time
from datetime import datetime
from colorama import Fore, Style, init


path =os.getcwd () 
now = datetime.now()
curtime = now.strftime("%H:%M")
author = "fullsafe."

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def back():
    input(f"{curtime} Appuyez sur Entrée pour revenir en arrière.")
    clearcmd()

def options():
    clearcmd()
    print(Fore.RED + """
██████████████████████████████████████████████████████████████████████████████████████████████████
█▌                                                                                              ▐█
█▌            ██████╗  █████╗ ██╗    ██╗ █████╗           ██████╗ ███████╗███╗   ██╗            ▐█
█▌            ██╔══██╗██╔══██╗██║    ██║██╔══██╗         ██╔════╝ ██╔════╝████╗  ██║            ▐█
█▌            ██║  ██║███████║██║ █╗ ██║███████║ █████╗  ██║  ███╗█████╗  ██╔██╗ ██║            ▐█
█▌            ██║  ██║██╔══██║██║███╗██║██╔══██║ ╚════╝  ██║   ██║██╔══╝  ██║╚██╗██║            ▐█
█▌            ██████╔╝██║  ██║╚███╔███╔╝██║  ██║         ╚██████╔╝███████╗██║ ╚████║            ▐█
█▌            ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝          ╚═════╝ ╚══════╝╚═╝  ╚═══╝            ▐█
█▌                                                                                              ▐█
██████████████████████████████████████████████████████████████████████████████████████████████████""")

    print(Fore.RED + """
[1] Générateurs
[2] Exit
    """)

    USER_OPTION = input(f"[=] Sélectionnez une option :  ")

    if USER_OPTION == "1":
        clearcmd()
        generators()
    elif USER_OPTION == "2":
        clearcmd()
        quit()
    else:
        print(f"[-] N'a pas reconnu l'entrée '{USER_OPTION}', Essayer à nouveau.")
        time.sleep(1)
        back()
        options()


def generators():
    clearcmd()
    print(Fore.RED + """
██████████████████████████████████████████████████████████████████████████████████████████████████
█▌                                                                                              ▐█
█▌            ██████╗  █████╗ ██╗    ██╗ █████╗           ██████╗ ███████╗███╗   ██╗            ▐█
█▌            ██╔══██╗██╔══██╗██║    ██║██╔══██╗         ██╔════╝ ██╔════╝████╗  ██║            ▐█
█▌            ██║  ██║███████║██║ █╗ ██║███████║ █████╗  ██║  ███╗█████╗  ██╔██╗ ██║            ▐█
█▌            ██║  ██║██╔══██║██║███╗██║██╔══██║ ╚════╝  ██║   ██║██╔══╝  ██║╚██╗██║            ▐█
█▌            ██████╔╝██║  ██║╚███╔███╔╝██║  ██║         ╚██████╔╝███████╗██║ ╚████║            ▐█
█▌            ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝          ╚═════╝ ╚══════╝╚═╝  ╚═══╝            ▐█
█▌                                                                                              ▐█
██████████████████████████████████████████████████████████████████████████████████████████████████
          """)

    print(Fore.RED + """
[1] Générateur de cartes-cadeaux Amazon
[2] Générateur de cartes-cadeaux Netflix
[3] Générateur de cartes-cadeaux Roblox
[4] Générateur de cartes-cadeaux Apple
[5] Générateur de cartes cadeaux Steam
[6] Générateur de cartes-cadeaux Google Play
[7] Générateur de cartes cadeaux Spotify
[8] Exit
    """)

    USER_OPTION = input("[=] Sélectionnez une option :  ")

    if USER_OPTION == "8":
        clearcmd()
        quit()
    if USER_OPTION == "1":
        clearcmd()
        amazon()
    elif USER_OPTION == "2":
        clearcmd()
        netflix()
    elif USER_OPTION == "3":
        clearcmd()
        roblox()
    elif USER_OPTION == "4":
        clearcmd()
        apple()
    elif USER_OPTION == "5":
        clearcmd()
        steam()
    elif USER_OPTION == "6":
        clearcmd()
        googleplay()
    elif USER_OPTION == "7":
        clearcmd()
        spotify()
    elif USER_OPTION == "8":
        clearcmd()
        options()
    else:
        print(f"[-] N'a pas reconnu l'entrée '{USER_OPTION}', Essayer à nouveau.")
        time.sleep(1)
        back()
        generators()


def amazon():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
 
     █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                   
    """)
    print(f"""{Fore.RED}     [ Crée par {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Configuration...")
    time.sleep(1)
    print(f"\nAmazon  Format: {Fore.RED}XXXX-XXXXXX-XXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] Combien de cartes souhaitez-vous générer :  ")

    with open(fr"{path}\Dawa - Output\Generated\amazon.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(5)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generation..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Généré avec succès {Fore.RED}{howmany}{Fore.RED} Giftcards")
    back()
    clearcmd()
    generators()
    pass


def netflix():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
 
    ███╗   ██╗███████╗████████╗███████╗██╗     ██╗██╗  ██╗     ██████╗ ███████╗███╗   ██╗
    ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ██╔██╗ ██║█████╗     ██║   █████╗  ██║     ██║ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║     ██║ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║
    ██║ ╚████║███████╗   ██║   ██║     ███████╗██║██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                            
    """)
    print(f"""{Fore.RED}     [ Crée par {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Configuration...")
    time.sleep(1)
    print(f"\nNetflix  Format: {Fore.RED}XXXX-XXXXXX-XXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] Combien de cartes souhaitez-vous générer :  ")

    with open(fr"{path}\Dawa - Output\Generated\netflix.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generation..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Généré avec succès {Fore.RED}{howmany}{Fore.RED} Giftcards in ./generated/netflix.txt")
    back()
    clearcmd()
    generators()
    pass


def roblox():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
 
    ██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║       
    ██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                       
    """)
    print(f"""{Fore.RED}     [ Crée par {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Configuration...")
    time.sleep(1)
    print(f"\nRoblox  Format: {Fore.RED}XXXX-XXXX-XXXX-XXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] Combien de cartes souhaitez-vous générer :  ")

    with open(fr"{path}\Dawa - Output\Generated\roblox.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            fourthrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom + "-" + fourthrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generation..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Généré avec succès {Fore.RED}{howmany}{Fore.RED} Giftcards in ./generated/roblox.txt")
    back()
    clearcmd()
    generators()
    pass


def apple():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
 
     █████╗ ██████╗ ██████╗ ██╗     ███████╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██████╔╝██████╔╝██║     █████╗      ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║     ██║     ███████╗███████╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                   
    """)
    print(f"""{Fore.RED}     [ Crée par {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Configuration...")
    time.sleep(1)
    print(f"\nApple  Format: {Fore.RED}XXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] Combien de cartes souhaitez-vous générer :  ")

    with open(fr"{path}\Dawa - Output\Generated\apple.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generation..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Généré avec succès {Fore.RED}{howmany}{Fore.RED} Giftcards in ./generated/apple.txt")
    back()
    clearcmd()
    generators()

    pass

def steam():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
 
    ███████╗████████╗███████╗ █████╗ ███╗   ███╗     ██████╗ ███████╗███╗   ██╗
    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║    ██╔════╝ ██╔════╝████╗  ██║
    ███████╗   ██║   █████╗  ███████║██╔████╔██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ╚════██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ███████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║    ╚██████╔╝███████╗██║ ╚████║
    ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                                               
    """)
    print(f"""{Fore.RED}     [ Crée par {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Configuration...")
    time.sleep(1)
    print(f"\nSteam  Format: {Fore.RED}XXXXX-XXXXX-XXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] Combien de cartes souhaitez-vous générer ")

    with open(fr"{path}\Dawa - Output\Generated\steam.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generation..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Généré avec succès {Fore.RED}{howmany}{Fore.RED} Giftcards in ./generated/steam.txt")
    back()
    clearcmd()
    generators()
    pass


def googleplay():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
 
     ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ██████╗      ██████╗ ███████╗███╗   ██╗
    ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║
    ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗█████╗██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║
    ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝╚════╝██╔═══╝     ██║   ██║██╔══╝  ██║╚██╗██║
    ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ██║         ╚██████╔╝███████╗██║ ╚████║                                                                                                                                                                                                                                                                                                                                                                                                                                       
    """)
    print(f"""{Fore.RED}     [ Crée par {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Configuration...")
    time.sleep(1)
    print(f"\nGoogle Play  Format: {Fore.RED}XXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] Combien de cartes souhaitez-vous générer ")

    with open(fr"{path}\Dawa - Output\Generated\googleplay.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generation..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Généré avec succès {Fore.RED}{howmany}{Fore.RED} Giftcards in ./generated/googleplay.txt")
    back()
    clearcmd()
    generators()
    pass


def spotify():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Fore.RED + """
 
    ███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ███████║██║     ╚██████╔╝   ██║   ██║██║        ██║       ╚██████╔╝███████╗██║ ╚████║
    ╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    """)
    print(f"""{Fore.RED}     [ Crée par {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Configuration...")
    time.sleep(1)
    print(f"\Spotify Format: {Fore.RED}XXXX-XXXX-XXXX-XXXX-XXXX-XX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] Combien de cartes souhaitez-vous générer ")

    with open(fr"{path}\Dawa - Output\Generated\spotify.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generation..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Généré avec succès {Fore.RED}{howmany}{Fore.RED} Giftcards in ./generated/spotfiy.txt")
    back()
    clearcmd()
    generators()
    pass


def main():
    try:
        clearcmd()
        options()
    except KeyboardInterrupt:
        print(f"{curtime} CTRL + C detected, Going back to the main menu!")
        time.sleep(1)
        options()

if __name__ == "__main__":
    main()
