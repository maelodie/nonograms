from methode_incomplete import *
from methode_complete import *
from config import *

type = input("Entrer sur 'I' pour la méthode incomplète et 'C' pour la méthode complète sur toutes les instances possibles.\nPour une instance particulière, appuyer 'A'\n")

if type == 'I':
    temps_exec = []            
    for i in range(17) :
        instance = ("instances/"+str(i)+".txt")
        debut = time.time()
        res = propagation_incomplete(instance)
        fin = time.time()
        temps_exec.append((fin - debut))
    print(timeFormat(temps_exec))

elif type == 'C':
    temps_exec = []            
    for i in range(17) :
        instance = ("instances/"+str(i)+".txt")
        debut = time.time()
        res = propagation_complete(instance)
        fin = time.time()
        temps_exec.append((fin - debut))
    print(timeFormat(temps_exec))

elif type ==  'A':
    methode = int(input("Entrer 0 pour la méthode incomplète et 1 pour la méthode complète\n"))
    instance_number = int(input("Entrer le numéro de l'instance\n"))
    if methode == 0:
        instance = ("instances/"+ str(instance_number) +".txt")
        debut = time.time()
        res = propagation_incomplete(instance)
        fin = time.time()
        exec = fin - debut
        print("Le temps d'exécution est:", timeFormat(exec))

    else:
        instance = ("instances/"+ str(instance_number) +".txt")
        debut = time.time()
        res = propagation_complete(instance)
        fin = time.time()
        exec = fin - debut
        print("Le temps d'exécution est:", timeFormat(exec))

