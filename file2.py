import nmap
import os

ip = '192.168.80.132'
port_range = '80'

scanner = nmap.PortScanner()

scanner.scan(ip, port_range)

file = open('report.txt', 'w')
file.write(scanner.get_nmap_last_output().decode())
file.close()

vulnerabilities = []

for host in scanner.all_hosts():
    for protocol in scanner[host].all_protocols():
        ports = scanner[host][protocol].keys()
        for port in ports:
            if scanner[host][protocol][port]['state'] == 'open':
                service = scanner[host][protocol][port]['name']
                product = scanner[host][protocol][port]['product']
                version = scanner[host][protocol][port]['version']
                if product == '' and version == '':
                    vulnerabilities.append(f'Port {port}: {service} - No product/version information available')
                elif product == '':
                    vulnerabilities.append(f'Port {port}: {service} - No product information available, version {version} detected')
                elif version == '':
                    vulnerabilities.append(f'Port {port}: {service} - Product {product} detected, no version information available')
                else:
                    vulnerabilities.append(f'Port {port}: {service} - {product} version {version} detected')

num_vulnerabilities = len(vulnerabilities)

if num_vulnerabilities > 0:
    print(f'{num_vulnerabilities} vulnerabilities found:')
    for vulnerability in vulnerabilities:
        print(vulnerability)
else:
    print('No vulnerabilities found.')
    
def get_vulnerabilities():
    return vulnerabilities, num_vulnerabilities