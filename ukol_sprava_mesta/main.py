from utulek import prijmout_zvire
from nemocnice import vypis_pacienty
from radnice import pozdravit_obcana



print("Zvolte si budovu: utulek(1), nemocnice(2), radnice(3)")
volba = int(input())

if volba == (1):
    prijmout_zvire(input("Napište jméno zvířete. "))
elif volba == (2):
    vypis_pacienty()
elif volba == (3):
    pozdravit_obcana(input("Napište Vaše jméno. "))
else:
    print("Neplatná volba!")