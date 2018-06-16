import requests
from socket import *


def Backgroundinfosladen():
    Backgroundinfo = open('Informationenback.txt', 'r')
    Informationen = []
    for line in Backgroundinfo:
        Informationen.append(Backgroundinfo.readline().strip())
    Backgroundinfo.close()
    IP = Informationen[0]
    serverport = Informationen[1]
    SERVER_PORT = int(serverport)
    return IP, SERVER_PORT


def Nutzerdatenladen():
    Nutzerdaten = open('Nutzerdaten.txt', 'r')
    Nutzerdaten1 = Nutzerdaten.read()
    Nutzerdaten.close()
    return Nutzerdaten1


def Fragebogenabrufen(IP,SERVER_PORT,Nutzerdaten1):
    Servermitteilung = requests.post('http://{IP}:{Port}'.format(IP=IP, Port=SERVER_PORT),
                                     data=Nutzerdaten1)  # ToDo Ändern
    return Servermitteilung.json()


def Antwortsenden(IP,SERVER_PORT,Nutzerdaten1):
    Servermitteilung = requests.post('http://{IP}:{Port}'.format(IP=IP, Port=SERVER_PORT), data=Nutzerdaten1)

IP,SERVER_PORT = Backgroundinfosladen()
Nutzerdaten1 = Nutzerdatenladen()
Servermitteilung = Fragebogenabrufen(IP,SERVER_PORT,Nutzerdaten1)
Antwortsenden(IP,SERVER_PORT,Nutzerdaten1)

