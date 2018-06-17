import requests
from socket import *
import json
import webbrowser

Results = []
Nutzerdaten1 = Results

def Backgroundinfosladen():
    Backgroundinfo = open('Informationenback.txt', 'r')
    Informationen = []
    for line in Backgroundinfo:
        Informationen.append(Backgroundinfo.readline().strip())
    Backgroundinfo.close()
    URL = Informationen[0]
    return URL

def Fragebogenabrufen(URL):
    Fragebogen = requests.get('{URL}/questions.json'.format(URL=URL))
    Fragebogen1 = Fragebogen.text
    Fragebogendatei = open('Fragebogen.json','w')
    Fragebogendatei.write(Fragebogen1)
    Fragebogendatei.close()
    return Fragebogen.json()



def Antwortsenden(URL,Nutzerdaten1):
    Antworten = [Nutzerdaten1]
    Antwortsendung = requests.post('{URL}/api_scoring.php'.format(URL=URL),data=json.dumps(Antworten))
    return Antwortsendung.text
def Namensendenspeichern(URL,Nutzerdaten1):
    Antworten = [Nutzerdaten1]
    #Name = 'Paulpaase'
    Datei = open('Nutzerdaten.txt','r',encoding= 'utf-8')
    Name = Datei.read()
    Datei.close()
    Sendung = requests.post('{URL}/api_scoring_save.php'.format(URL=URL),data={'name':Name,'response':json.dumps(Antworten)})
    return Sendung.text,Name

def Punktezahlvergleich(URl,Name):
   URL1 = 'https://jhffm01.uber.space/umweltserver/login.php?user='+str(Name)
   E = webbrowser.open(URL1)
   return E



URL = Backgroundinfosladen()
Fragebogen = Fragebogenabrufen(URL)
Antwortsendung = Antwortsenden(URL,Nutzerdaten1)
Punktestand,Name = Namensendenspeichern(URL,Nutzerdaten1)
Scorerpunkt_User = str(Punktestand)
Punktezahlvergleich(URL,Name)
