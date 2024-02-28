from methode_incomplete import *
from methode_complete import *
from config import *
place_affichage = "Les affichages des solutions se trouvent dans le dossier /out sous le format methode/<n° instance>.<methode>.jpeg"
type = input("Entrer sur 'I' pour la méthode incomplète et 'C' pour la méthode complète sur toutes les instances possibles.\nPour une instance particulière, appuyer 'A'\n")

if type == 'I':
    temps_exec = []            
    for i in range(17) :
        debut = time.time()
        res = propagation_incomplete(i)
        fin = time.time()
        temps_exec.append((fin - debut))
    print(timeFormat(temps_exec))
    print(place_affichage)

elif type == 'C':
    temps_exec = []            
    for i in range(17) :
        debut = time.time()
        res = propagation_complete(i)
        fin = time.time()
        temps_exec.append((fin - debut))
    print(timeFormat(temps_exec))
    print(place_affichage)

elif type ==  'A':
    methode = int(input("Entrer 0 pour la méthode incomplète et 1 pour la méthode complète\n"))
    instance_number = int(input("Entrer le numéro de l'instance\n"))
    if methode == 0:
        debut = time.time()
        res = propagation_incomplete(instance_number)
        fin = time.time()
        exec = fin - debut
        print("Le temps d'exécution est:", timeFormatSeconds(exec), exec, "s")
        print(place_affichage)


    else:
        debut = time.time()
        res = propagation_complete(instance_number)
        fin = time.time()
        exec = fin - debut
        print("Le temps d'exécution est:", timeFormatSeconds(exec), exec, "s")
        print(place_affichage)