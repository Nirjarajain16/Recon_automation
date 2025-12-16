import socket
import subprocess

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "Unable to resolve IP"

def port_scan(ip):
    open_ports = []
    common_ports = [21, 22, 23, 80, 443, 3306]
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def whois_lookup(domain):
    try:
        result = subprocess.check_output(["whois", domain], universal_newlines=True)
        return result[:500]
    except:
        return "WHOIS not available"

target = input("Enter target domain: ")

ip = get_ip(target)
ports = port_scan(ip)
whois = whois_lookup(target)

with open("recon_report.txt", "w") as report:
    report.write(f"Target: {target}\n")
    report.write(f"IP Address: {ip}\n\n")
    report.write("Open Ports:\n")
    for p in ports:
        report.write(f"- Port {p} open\n")
    report.write("\nWHOIS Info:\n")
    report.write(whois)

print("Recon completed. Report saved as recon_report.txt")
