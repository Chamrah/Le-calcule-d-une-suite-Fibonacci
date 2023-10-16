#Programme qui demande à l'utilisateur de taper un entier n, supérieur à 2, jusqu'à ce que la réponse convienne, puis qui calcule et affiche tous les termes de la suite de Fibonacci, inférieurs ou égaux à n
while True:
     n=int(input("Veuillez entrer un entier supérieur a 2 : "))
     if(n>=2):
         break
uj=0
ui=1
for i in range(2,n+1):
    u=ui+uj
    print(u)
    uj=ui
    ui=u
