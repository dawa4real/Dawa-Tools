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

def check_username(site, url, username):
    try:
        response = requests.get(url.format(username))
        if response.status_code == 200:
            return (site, True, url.format(username))
        else:
            return (site, False, None)
    except requests.RequestException:
        return (site, False, None)

def main(username):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_username, site, url, username) for site, url in sites.items()]
        results = [future.result() for future in futures]

    found_sites = []
    for site, exists, url in results:
        if exists:
            print(Fore.GREEN + f"[+] {username} found on {site}")
            found_sites.append(url)
        else:
            print(Fore.RED + f"[-] {username} not found on {site}")

    if found_sites:
        open_links = input(Fore.RED + "[?] Do you want to open the links? (yes/no): ").strip().lower()
        if open_links == 'yes':
            for url in found_sites:
                webbrowser.open(url)
    else:
        print(Fore.YELLOW + "[!] No links to open.")

if __name__ == "__main__":
    username = input(Fore.RED + "[=] Enter the username to search: ")
    main(username)
