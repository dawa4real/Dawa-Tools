import os
import colorama
from colorama import Fore, Style
username = os.getlogin()
colorama.init(autoreset=True)
INPUT = Fore.BLUE + "[ENTRÉE] " + Fore.RESET
WAIT = Fore.YELLOW + "[ATTENTE] " + Fore.RESET
INFO = Fore.GREEN + "[INFO] " + Fore.RESET
ERROR = Fore.RED + "[ERREUR] " + Fore.RESET
blanc = Fore.WHITE
rouge = Fore.RED
jaune = Fore.YELLOW
path = os.getcwd()

dossier_base_relative = os.path.join(path, "Dawa - Input", "DATA-BASE")
dossier_base = os.path.abspath(dossier_base_relative)
recherche = input("Entrez votre recherche : ")
print("Recherche dans la base de données...")
print(f"Le dossier base absolu est : {dossier_base}")

try:
    fichiers_recherches = 0

    def vérifier(dossier):
        global fichiers_recherches
        résultats_trouvés = False
        print(f"{WAIT} Recherche dans {blanc}{dossier}")
        for élément in os.listdir(dossier):
            chemin_element = os.path.join(dossier, élément)
            if os.path.isdir(chemin_element):
                vérifier(chemin_element)
            elif os.path.isfile(chemin_element):
                try:
                    with open(chemin_element, 'r', encoding='utf-8') as fichier:
                        numéro_ligne = 0
                        fichiers_recherches += 1
                        print(f"{fichiers_recherches} - {élément}")
                        for ligne in fichier:
                            numéro_ligne += 1
                            if recherche in ligne:
                                résultats_trouvés = True
                                info_ligne = ligne.strip().replace(recherche, f"{jaune}{recherche}{blanc}")
                                print(f"""{rouge}
- Dossier : {blanc}{dossier}{rouge}
- Fichier : {blanc}{élément}{rouge}
- Ligne   : {blanc}{numéro_ligne}{rouge}
- Résultat : {blanc}{info_ligne}
""")
                except UnicodeDecodeError:
                    try:
                        with open(chemin_element, 'r', encoding='latin-1') as fichier:
                            fichiers_recherches += 1
                            numéro_ligne = 0
                            print(f"{fichiers_recherches} | {élément}")
                            for ligne in fichier:
                                numéro_ligne += 1
                                if recherche in ligne:
                                    résultats_trouvés = True
                                    info_ligne = ligne.strip().replace(recherche, f"{jaune}{recherche}{blanc}")
                                    print(f"""{rouge}
- Dossier : {blanc}{dossier}{rouge}
- Fichier : {blanc}{élément}{rouge}
- Ligne   : {blanc}{numéro_ligne}{rouge}
- Résultat : {blanc}{info_ligne}
""")
                    except Exception as e:
                        print(f"{ERROR} Erreur lors de la lecture du fichier \"{blanc}{élément}{rouge}\": {blanc}{e}")
                except Exception as e:
                    print(f"{ERROR} Erreur lors de la lecture du fichier \"{blanc}{élément}{rouge}\": {blanc}{e}")
        return résultats_trouvés

    résultats_trouvés = vérifier(dossier_base)
    if not résultats_trouvés:
        print(f"{INFO} Aucun résultat trouvé pour \"{blanc}{recherche}{rouge}\".")

    print(f"{INFO} Total des fichiers recherchés : {blanc}{fichiers_recherches}")

except Exception as e:
    print(f"{ERROR} Erreur pendant la recherche : {blanc}{e}")

