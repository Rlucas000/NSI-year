new_message =""     # initialise new_message avec un message vide
message = input("Veuillez saisir un texte en MAJUSCULE et terminer par ENTER")
print("Vous avez saisi ",message)  # Affiche le message saisi

for n in message:               # pour chaque caractère n dumessage saisi (de la chaine message)
    code_initial = ord(n)       # la variable code_initial prend le code (Unicode)
    code_minuscule = code_initial+32  # calcul le codecorrespondant au caractère minuscule
    car_minuscule = chr(code_minuscule) # car_minuscule prend le caractère/symbole correspondant
    print(car_minuscule)      # Affiche le caractère obtenu
    new_message = new_message + car_minuscule  # ajoute le caractère obtenu à new_message

print (new_message)    # Affiche le nouveau message
