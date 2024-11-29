import requests
from concurrent.futures import ThreadPoolExecutor
import webbrowser
from colorama import init, Fore, Style
init(autoreset=True)

sites = {
    "Twitter": "https://twitter.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Github": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Tumblr": "https://{}.tumblr.com",
    "YouTube": "https://www.youtube.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Twitch": "https://www.twitch.tv/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Medium": "https://medium.com/@{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Goodreads": "https://www.goodreads.com/{}",
    "GitLab": "https://gitlab.com/{}"
}

def verifier_nom_utilisateur(site, url, nom_utilisateur):
    try:
        response = requests.get(url.format(nom_utilisateur))
        if response.status_code == 200:
            return (site, True, url.format(nom_utilisateur))
        else:
            return (site, False, None)
    except requests.RequestException:
        return (site, False, None)

def principal(nom_utilisateur):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(verifier_nom_utilisateur, site, url, nom_utilisateur) for site, url in sites.items()]
        results = [future.result() for future in futures]

    sites_trouves = []
    for site, existe, url in results:
        if existe:
            print(Fore.GREEN + f"[+] {nom_utilisateur} trouvé sur {site}")
            sites_trouves.append(url)
        else:
            print(Fore.RED + f"[-] {nom_utilisateur} non trouvé sur {site}")

    if sites_trouves:
        ouvrir_liens = input(Fore.RED + "[?] Voulez-vous ouvrir les liens ? (oui/non) : ").strip().lower()
        if ouvrir_liens == 'oui':
            for url in sites_trouves:
                webbrowser.open(url)
    else:
        print(Fore.YELLOW + "[!] Aucun lien à ouvrir.")

if __name__ == "__main__":
    nom_utilisateur = input(Fore.RED + "[=] Entrez le nom d'utilisateur à rechercher : ")
    principal(nom_utilisateur)
