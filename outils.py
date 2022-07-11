#!/usr/bin/python3
import nmap
import os

sc = nmap.PortScanner()

print("""                       \n
   _____          __  .__                
  /     \ _____ _/  |_|  |__   ____  ____   
 /  \ /  \\__  \\   __\  |  \_/ __ \/  _ \  
/    Y    \/ __ \|  | |   Y  \  ___(  <_> ) 
\____|__  (____  /__| |___|  /\___  >____/  
        \/     \/          \/     \/        
  """)


def main(): # Permets de donner le choix à l'utilisateur de ce qu'il veut faire.
    n = input("1 - Scan Réseaux\n2- Vulnerabilités détection\n3- Exploit\n\nVeuillez entrer un nombre :")
    
    if n == '1':
        nmap()

    if n == '2':
        vuln()
    
    if n == '3':
        os.system('msfconsole')

    else:
        print("Veuillez choisir l'une des valeurs qui sont affichées 1-3")

def nmap(): #Permets de connaitre des informations sur l'ip renseigné
    print("**********************Bienvenue sur le mode Scan Réseaux*************************")
    print("*********************************************************************************")
    ip = input("\nVeuillez entrer l'adresse ip: ")
    sc.scan(ip, '1-1024') # Scan l'ip choisi et les ports de 1 a 1024
    print(sc.scaninfo()) # Affiche l'info du scan
    print(sc[ip]['tcp'].keys())

def vuln():
    print("**********************Bienvenue sur le mode Vulnérabilité*************************")
    print("*********************************************************************************")
    ip = input("\nVeuillez entrer l'adresse ip: ")
    print(os.system('nmap -sV --script=vulscan.nse  ' +ip))


if __name__ == "__main__": # Permet de dire que la fonction main et la première à être lancé celle-ci part défaut
    main()


