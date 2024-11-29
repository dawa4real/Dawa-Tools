import random
import os
import time
from datetime import datetime
from colorama import Fore, Style, init


now = datetime.now()
curtime = now.strftime("%H:%M")
author = "fullsafe."
path =os.getcwd () 
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def back():
    input(f"{curtime} Press enter to go back.")
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
[1] Generators
[2] Exit
    """)

    USER_OPTION = input(f"[=] Select the option:  ")

    if USER_OPTION == "1":
        clearcmd()
        generators()
    elif USER_OPTION == "2":
        clearcmd()
        quit()
    else:
        print(f"[-] Did not recognize input '{USER_OPTION}', Try again.")
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
[1] Amazon Giftcard Generator
[2] Netflix Giftcard Generator
[3] Roblox Giftcard Generator
[4] Apple Giftcard Generator
[5] Steam Giftcard Generator
[6] Google Play Giftcard Generator
[7] Spotify Giftcard Generator
[8] Exit
    """)

    USER_OPTION = input("[=] Select the option:  ")

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
        print(f"[-] Did not recognize input '{USER_OPTION}', Try again.")
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
    print(f"""{Fore.RED}     [ Made by {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Setting Up...")
    time.sleep(1)
    print(f"\nAmazon Giftcard Format is: {Fore.RED}XXXX-XXXXXX-XXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many tokens do you want to generate :  ")

    with open(fr"{path}\Dawa - Output\Generated/amazon.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(5)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} Giftcards")
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
    print(f"""{Fore.RED}     [ Made by {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Setting Up...")
    time.sleep(1)
    print(f"\nNetflix Giftcard Format is: {Fore.RED}XXXX-XXXXXX-XXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many tokens do you want to generate :  ")

    with open(fr"{path}\Dawa - Output\Generated/netflix.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} Giftcards in DAWA-TOOL\1 - Menu\Output\generated/netflix.txt")
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
    print(f"""{Fore.RED}     [ Made by {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Setting Up...")
    time.sleep(1)
    print(f"\nRoblox Giftcard Format is: {Fore.RED}XXXX-XXXX-XXXX-XXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many tokens do you want to generate :  ")

    with open(fr"{path}\Dawa - Output\Generated/roblox.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            fourthrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom + "-" + fourthrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} Giftcards in DAWA-TOOL\1 - Menu\Output\generated/roblox.txt")
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
    print(f"""{Fore.RED}     [ Made by {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Setting Up...")
    time.sleep(1)
    print(f"\nApple Giftcard Format is: {Fore.RED}XXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many tokens do you want to generate :  ")

    with open(fr"{path}\Dawa - Output\Generated/apple.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} Giftcards in DAWA-TOOL\1 - Menu\Output\generated/apple.txt")
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
    print(f"""{Fore.RED}     [ Made by {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Setting Up...")
    time.sleep(1)
    print(f"\nSteam Giftcard Format is: {Fore.RED}XXXXX-XXXXX-XXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many tokens do you want to generate ")

    with open("DAWA-TOOL\1 - Menu\Output\generated/steam.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} Giftcards in DAWA-TOOL\1 - Menu\Output\generated/steam.txt")
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
    print(f"""{Fore.RED}     [ Made by {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Setting Up...")
    time.sleep(1)
    print(f"\nGoogle Play Giftcard Format is: {Fore.RED}XXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many tokens do you want to generate ")

    with open(fr"{path}\Dawa - Output\Generated/googleplay.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} Giftcards in DAWA-TOOL\1 - Menu\Output\generated/googleplay.txt")
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
    print(f"""{Fore.RED}     [ Made by {Fore.RED}fullsafe. {Fore.RED}]{Fore.RED} DAWA-TOOL
  {Fore.RED}
  """)
    print(f"{Fore.RED}[*]{Fore.RED} Setting Up...")
    time.sleep(1)
    print(f"\Spotify Giftcard Format is: {Fore.RED}XXXX-XXXX-XXXX-XXXX-XXXX-XX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.RED}[?] How many tokens do you want to generate ")

    with open(fr"{path}\Dawa - Output\Generated/spotify.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.RED}[*]{Fore.RED} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.RED}[+]{Fore.RED} Successfully generated {Fore.RED}{howmany}{Fore.RED} Giftcards in DAWA-TOOL\1 - Menu\Output\generated/spotfiy.txt")
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
