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
    return input("[?] Enter the Discord webhook URL: ").strip()


def get_number_of_ips():
    while True:
        try:
            num_ips = int(input("[?] Enter the number of IP addresses to generate: "))
            if num_ips > 0:
                return num_ips
            else:
                print("[!] Please enter a number greater than zero.")
        except ValueError:
            print("[!] Invalid input. Please enter a valid number.")


def main():
    num_ips_to_generate = get_number_of_ips()
    webhook_url = get_discord_webhook_url()

    generated_ips = 0
    valid_ips = []

    while generated_ips < num_ips_to_generate:
        ip = generate_random_ip()
        if is_valid_ip(ip):
            print(f"[+] Valid IP address generated: {ip}")
            valid_ips.append(ip)
            generated_ips += 1

    for ip in valid_ips:
        payload = {'content': f"[+] New valid IP address generated: `{ip}`"}
        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code == 204:
                print("[+] IP address successfully sent to Discord webhook.")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error sending IP address to Discord webhook: {e}")


if __name__ == "__main__":
    main()
