import requests
from socket import *


def Backgroundinfosladen():
    Backgroundinfo = open('Informationenback.txt', 'r')
    Informationen = []
    for line in Backgroundinfo:
        Informationen.append(Backgroundinfo.readline().strip())
    Backgroundinfo.close()
    URL = Informationen[0]
    return URL


def Nutzerdatenladen():
    Nutzerdaten = open('Nutzerdaten.txt', 'r')
    Nutzerdaten1 = Nutzerdaten.read()
    Nutzerdaten.close()
    return Nutzerdaten1


def Fragebogenabrufen(URL,Nutzerdaten1):
    Fragebogen = requests.get('{URL}/questions.json'.format(URL=URL), data=Nutzerdaten1)
    Fragebogendatei = open('Fragebogen.json','w')
    Fragebogendatei.write(Fragebogen)
    Fragebogendatei.close()
    return Fragebogen.json()



def Antwortsenden(URL, Nutzerdaten1):
    Antwortsendung = requests.post('{URL}/response.json'.format(URL=URL),data=json.dumps(Nutzerdaten1))# ToDo Ändern


URL = Backgroundinfosladen()
Nutzerdaten1 = Nutzerdatenladen()
Fragebogen = Fragebogenabrufen(URL,Nutzerdaten1)
Antwortsendung = Antwortsenden(URL,Nutzerdaten1)
print('FERTIG')
