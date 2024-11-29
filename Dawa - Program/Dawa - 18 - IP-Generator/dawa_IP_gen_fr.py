import random
import socket
import requests


def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"


def is_valid_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False


def get_discord_webhook_url():
    return input("[?] Entrez l'URL du webhook Discord : ").strip()


def get_number_of_ips():
    while True:
        try:
            num_ips = int(input("[?] Entrez le nombre d'adresses IP à générer : "))
            if num_ips > 0:
                return num_ips
            else:
                print("[!] Veuillez entrer un nombre supérieur à zéro.")
        except ValueError:
            print("[!] Entrée invalide. Veuillez entrer un nombre valide.")


def main():
    num_ips_to_generate = get_number_of_ips()
    webhook_url = get_discord_webhook_url()

    generated_ips = 0
    valid_ips = []

    while generated_ips < num_ips_to_generate:
        ip = generate_random_ip()
        if is_valid_ip(ip):
            print(f"[+] Adresse IP valide générée : {ip}")
            valid_ips.append(ip)
            generated_ips += 1

    for ip in valid_ips:
        payload = {'content': f"[+] Nouvelle adresse IP valide générée : `{ip}`"}
        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code == 204:
                print("[+] Adresse IP envoyée avec succès au webhook Discord.")
        except requests.exceptions.RequestException as e:
            print(f"[-] Erreur lors de l'envoi de l'adresse IP au webhook Discord : {e}")


if __name__ == "__main__":
    main()
