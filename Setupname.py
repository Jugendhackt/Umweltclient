Name = input('Bitte gebe deinen Namen für das Setup an ')
Data = open('Nutzerdaten.txt','w')
Data.write(Name)
Data.close()
print('Setup beendet')