#!/usr/bin/python3
# By - Dxm42
# utiliza threads para realizar o processamento da wordlist caso ela seja muito grande

import queue
import threading, socket, sys

art = """
   ___       ____ ___    ___  _  ______
  / _ \__ __/ / /|_  |  / _ \/ |/ / __/
 / // /\ \ /_  _/ __/  / // /    /\ \  
/____//_\_\ /_//____/ /____/_/|_/___/  
"""
gitHub  = "\t\thttps://github.com/Dxm42\n"

WHITE = '\033[0m'
GREEN = '\033[1;32m'
CYAN = '\033[1;36m'
MAGENTA = '\033[1;35m'
YELLOW = '\033[1;33m'

def printDx(banner,cor):
        return print(f"{cor}{banner}{WHITE}")

def printColor(text1, cor1, text2, cor2):

    return print(f"{cor1}{text1}: {WHITE}{cor2}{text2}{WHITE}")

try:
    dominio = sys.argv[1] 
    wordlist = sys.argv[2]
except:
    printColor(f"Modo de Uso {sys.argv[0]}",CYAN," Dominio Wordlist", YELLOW)
    sys.exit()

printDx(art, CYAN)
printDx(gitHub, GREEN)


printColor("Buscando por Subdominios no host",MAGENTA, dominio,CYAN)
printColor("Wordlist",MAGENTA, wordlist,CYAN)
print("\n")

def forca_bruta():
    while True:
        DNS = q.get() + "." +  dominio
        try:
            printColor(DNS,YELLOW, socket.gethostbyname(DNS),GREEN)
        except socket.gaierror:
            pass
        q.task_done()
    
q = queue.Queue()

threading.Thread(target=forca_bruta, daemon=True).start()

try:
    with open(wordlist) as lista:
        while True:
            nome = lista.readline().strip()

            if not nome:
                break

            q.put(nome)
except:
    printDx("Erro ao Abrir Wordlist", YELLOW)
    sys.exit()

q.join()

printDx("Mapeamento completo", MAGENTA)

sys.exit()
