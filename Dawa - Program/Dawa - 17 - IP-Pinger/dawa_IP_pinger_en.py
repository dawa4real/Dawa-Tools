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

ip_address = input("[?] Enter an IP address to ping: ")

success, result = ping_ip(ip_address)
if success:
    print(f"[+] Ping successful to IP address {ip_address} :")
else:
    print(f"[-] Ping failed to IP address {ip_address} :")
print(result)
