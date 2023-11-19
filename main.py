from methode_incomplete import *
from config import *

temps_exec = []            # liste de temps de résolution de chaque instance
for i in range(10) :
    instance = ("instances/"+str(i)+".txt")
    debut = time.time()
    res = propagation(instance)
    fin = time.time()
    temps_exec.append((fin - debut))
  
print(temps_exec)
