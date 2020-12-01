def det_sexe(secu):
    '''
    renvoie le sexe d'un individu sous forme de string en fonction du numéro de sécu
    '''
    n = int(secu[0])
    if n == 1:
        return("Homme")
    elif n == 2:
        return("Femme")
    else:
        return("Non défini")


def page_patient(nom = "Durand", prenom = "Nathalie", date = "01/01/1992", mail = "nathalie.durand@orange.fr", mdp = "0000", secu = "118998", photo = "null"):
    
    source = open("../Ressources/squelette_patient.html", "r")
    squelette = source.read()
    source.close()

    fin = len(squelette)

    page = open("../Pages/" + secu + ".html", "w", encoding="utf-8")

    # on recopie le squelette jusqu'à tomber sur un symbole $

    sexe = det_sexe(secu)
    pointeur = 0

    while True: # on lit le squelette, caractère par caractère
        # tant que l'on est pas dans une zone d'édition (délimitée par des $), on recopie le squelette
        while (squelette[pointeur] != "$") and (pointeur != fin - 1):
            page.write(squelette[pointeur])
            pointeur += 1
            if pointeur == fin:
                break
        # on est dans une zone d'édition
        # on sélectionone le premier caractère de l'input demandé 
        input = ""
        pointeur += 1
        
        if pointeur == fin:
                break

        while (squelette[pointeur] != "$"):
            input += squelette[pointeur]
            pointeur += 1
        
        # a ce stade, le pointeur pointe sur un symbole $ et on veut ajouter au fichier la variable input
        try:
            page.write(eval(input))
        except:
            page.write("null")
        pointeur += 1

        if pointeur == fin:
            break

    
    page.close()


page_patient()

