import subprocess

def ping_ip(ip_address):
    try:
        process = subprocess.Popen(['ping', '-n', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        output = stdout.decode('cp850', errors='ignore')

        if 'TTL' in output:
            return True, output
        else:
            return False, output
    except Exception as e:
        return False, str(e)

ip_address = input("[?] Entrez une adresse IP à pinger : ")

succes, resultat = ping_ip(ip_address)
if succes:
    print(f"[+] Ping réussi vers l'adresse IP {ip_address} :")
else:
    print(f"[-] Échec du ping vers l'adresse IP {ip_address} :")
print(resultat)
