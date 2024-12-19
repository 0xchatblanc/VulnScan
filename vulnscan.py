import asyncio
import socket
import requests
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Unknown"

async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.close()
        await writer.wait_closed()
        return port
    except:
        return None

def search_vulnerabilities(service):
    api_url = f"https://vulners.com/api/v3/search/lucene/"
    query = f"software:{service}"
    try:
        response = requests.get(api_url, params={"query": query})
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'documents' in data['data']:
                return [vuln['title'] for vuln in data['data']['documents']]
    except Exception as e:
        return []
    return []

def chunk_ports(start, end, chunk_size):
    return [range(i, min(i + chunk_size, end + 1)) for i in range(start, end + 1, chunk_size)]

async def scan_ports(ip, ports):
    tasks = [scan_port(ip, port) for port in ports]
    results = await asyncio.gather(*tasks)
    open_ports = [port for port in results if port]
    return open_ports

async def scan_all_ports(ip, start_port, end_port, chunk_size=1000):
    open_ports = []
    port_chunks = chunk_ports(start_port, end_port, chunk_size)
    for chunk in port_chunks:
        print(Fore.GREEN + f"[+] Scanning ports {chunk.start} to {chunk.stop - 1}...")
        chunk_open_ports = await scan_ports(ip, chunk)
        open_ports.extend(chunk_open_ports)
    return open_ports

def print_banner():
    color_box = Fore.LIGHTBLACK_EX
    color_banner = Fore.LIGHTRED_EX
    color_credit = Fore.LIGHTRED_EX
    banner_lines = [
        "██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗",
        "██║   ██║██║   ██║██║     ████╗  ██║██╔════╝██╔════╝██╔══██╗████╗  ██║",
        "██║   ██║██║   ██║██║     ██╔██╗ ██║███████╗██║     ███████║██╔██╗ ██║",
        "╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║╚════██║██║     ██╔══██║██║╚██╗██║",
        " ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████║╚██████╗██║  ██║██║ ╚████║",
        "  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝"
    ]
    print(color_box + "╔" + "═" * 72 + "╗")
    for line in banner_lines:
        print(color_box + "║ " + color_banner + line + color_box + " ║")
    print(color_box + "║ " + "╔" + "═" * 23 + "╗" + " " * 44 + "  ║")
    print(color_box + "║ " + f"║  {color_credit}Github : 0xtheghost{color_box}  ║" + " " * 44 + "  ║")
    print(color_box + "║ " + f"║ {color_credit}Discord : 0xchatblanc{color_box} ║" + " " * 44 + "  ║")
    print(color_box + "║ " + "╚" + "═" * 23 + "╝" + " " * 44 + "  ║")
    print(color_box + "╚" + "═" * 72 + "╝")

async def main():
    print_banner()
    try:
        target_ip = input(Fore.LIGHTBLACK_EX + "Enter target IP address : " + Style.RESET_ALL).strip()
        start_port = int(input(Fore.LIGHTBLACK_EX + "Enter start port (default 1) : " + Style.RESET_ALL) or 1)
        end_port = int(input(Fore.LIGHTBLACK_EX + "Enter end port (default 65535) : " + Style.RESET_ALL) or 65535)

        print(Fore.LIGHTGREEN_EX + "\n[+] Scanning in progress...")
        open_ports = await scan_all_ports(target_ip, start_port, end_port)

        table = PrettyTable(["Port", "Status", "Service", "Known Vulnerabilities"])
        for port in open_ports:
            service = get_service_name(port)
            vulnerabilities = search_vulnerabilities(service)
            vuln_summary = ", ".join(vulnerabilities[:3]) if vulnerabilities else "None"
            table.add_row([
                Fore.CYAN + str(port) + Style.RESET_ALL,
                Fore.GREEN + "Open" + Style.RESET_ALL,
                Fore.YELLOW + service + Style.RESET_ALL,
                Fore.RED + vuln_summary + Style.RESET_ALL if vulnerabilities else Fore.GREEN + "None" + Style.RESET_ALL
            ])

        print(table)

    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interruption by the user. Goodbye!")
    except ValueError:
        print(Fore.RED + "[!] Error: Please enter valid numbers for the ports.")
    except Exception as e:
        print(Fore.RED + f"[!] An error has occurred : {e}")

if __name__ == "__main__":
    asyncio.run(main())