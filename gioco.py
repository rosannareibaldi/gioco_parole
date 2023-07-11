import random
# Scelta del livello: facciamo selezionare da utente sia la difficoltà delle parole che il numero di tentativi con cui 
# giocare
livello = input("Scegli il livello di difficoltà fra 1, 2, 3:\n1->Facile\n2->Medio\n3->Difficile")
livello_diff = {
    "1": {"parole": ['ciao', 'bello', 'brutto', 'sole'], "n_tentativi": 8},
    "2": {"parole": ['castello', 'lampadina', 'scaffale', 'forbice', 'habitat'], "n_tentativi": 7},
    "3": {"parole": ["weekend", "bajour", "disarcivescovizzare"], "n_tentativi": 6}
}
lista_parole = livello_diff[livello]["parole"]
n_tentativi = livello_diff[livello]["n_tentativi"]