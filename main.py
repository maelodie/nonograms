from methode_incomplete import *
from methode_complete import *
from config import *

type = int(input("Entrer sur 100 pour la méthode incomplète et 200 pour la méthode complète\nPour exécuter une instance particulière, donner son numéro\n"))

if type == 100:
    temps_exec = []            
    for i in range(11) :
        instance = ("instances/"+str(i)+".txt")
        debut = time.time()
        res = propagation_incomplete(instance)
        fin = time.time()
        temps_exec.append((fin - debut))
    print(timeFormat(temps_exec))

elif type == 100:
    temps_exec = []            
    for i in range(17) :
        instance = ("instances/"+str(i)+".txt")
        debut = time.time()
        res = propagation_complete(instance)
        fin = time.time()
        temps_exec.append((fin - debut))
    print(timeFormat(temps_exec))

else:
    methode = int(input("Entrer 0 pour la méthode incomplète et 1 pour la méthode complète\n"))
    if methode == 0:
        instance = ("instances/"+ type +".txt")
        debut = time.time()
        res = propagation_incomplete(instance)
        fin = time.time()
        exec = fin - debut
        print("Le temps d'exécution est:", exec)
    else:
        instance = ("instances/"+ type +".txt")
        debut = time.time()
        res = propagation_complete(instance)
        fin = time.time()
        exec = fin - debut
        print("Le temps d'exécution est:", exec)

