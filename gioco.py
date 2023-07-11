import random


def replace_values(stringa, stringa_nascosta, char):
    """
    Funzione che sostituisce char nella stringa nascosta, nella posizione in cui char è presente in stringa.


    :param stringa: str. parola da indovinare.
    :param stringa_nascosta: list. parola contenitore delle lettere indovinate.
    :param char: str. lettera da sostituire agli _
    :return:
    """
    for i, l in enumerate(stringa):
        if l == char:
            stringa_nascosta[i] = char


# Scelta del livello: facciamo selezionare da utente sia la difficoltà delle parole che il numero di tentativi con cui
# giocare
livello = input("Scegli il livello di difficoltà fra 1, 2, 3:\n1->Facile\n2->Medio\n3->Difficile")
while livello not in ['1', '2', '3']:
    print("Hai inserito un valore non valido. Scegli un livello valido.")
    livello = input("Scegli il livello di difficoltà fra 1, 2, 3:\n1->Facile\n2->Medio\n3->Difficile")

livello_diff = {
    "1": {"parole": ['ciao', 'bello', 'brutto', 'sole'], "n_tentativi": 8},
    "2": {"parole": ['castello', 'lampadina', 'scaffale', 'forbice', 'habitat'], "n_tentativi": 7},
    "3": {"parole": ["weekend", "bajour", "disarcivescovizzare"], "n_tentativi": 6}
}


lista_parole = livello_diff[livello]["parole"]
n_tentativi = livello_diff[livello]["n_tentativi"]

# Scegliamo una parola a caso fra quelle della lista_parole
parola = random.choice(lista_parole)

# definiamo una parola che tiene traccia dei tentativi utente
parola_nascosta = list('_'*len(parola))

# Definisco un contatore per stoppare il gioco in caso di troppi tentativi
contatore = 0

# Ciclo while: continua finchè ho tentativi rimanenti e non ho indovinato la parola
while contatore < n_tentativi and '_' in parola_nascosta:
    print(f"parola da indovinare: {''.join(parola_nascosta)}")

    # Chiediamo di inserire una lettera all'utente
    lettera = input("Inserisci una lettera con cui giocare: ").lower()

    # Se la lettera è presente...
    if lettera in parola:
        # Cerchiamo gli indici e sostituiamo la lettera nella posizione dove è presente
        replace_values(parola, parola_nascosta, lettera)
        # for i, l in enumerate(parola):
        #     if l == lettera:
        #         parola_nascosta[i] = lettera
        print("Bravo, la lettera è presente nella parola!\n")

    else:
        contatore += 1
        print(f"Lettera non presente. Hai ancora {n_tentativi - contatore} tentativi.\n")


if parola_nascosta == list(parola):
    print(f"Ottimo, hai vinto! La parola era: {parola}")
else:
    print(f"Tentativi finiti, hai perso. La parola era: {parola}")