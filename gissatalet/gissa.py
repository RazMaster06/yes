#Denna uppgift ska vi öva variabler, vilkor och loopar
import random 
import os
os.system("cls" if os.name == "nt" else "clear")

print("-----------------------------------------------")
print(".:gissatalet:")

print("gissa ett tal mellan 1 - 10 och pröva lyckan, du får 3st försök!\n")

slumptal = random.randint(1, 10)
#print(slumptal)

i=0
hitta = False

#loopar


while i < 3:

    gissatal = input("mata in tal: ")

    if slumptal == int(gissatal):
        hitta = True
        print("\n Rätt svar! \n")
        break

    i += 1

    if i == 1:
        print("\n Två försök kvar")

    if i == 2:
        print("\n Sista försöket!")

if hitta:
    print("\n Bra jobbat, här får du en anka")

else:
    print("Bättre lycka nästa gång")

print("n\--------------------------------------------------")