'''
terminaisons=['e','es','e','ons','ez','ent']
terminaisonsE=['e','es','e','eons','ez','ent']#pour le eons
pronoms=['je','tu','il/elle','nous','vous','ils/elles']
pronomj=["j'",'tu','il/elle','nous','vous','ils/elles']# pour le j'
voyelles=['a','e','i','o','u','y']

verbe=str(input("insérer votre verbe à l'indicatif  "))

depart = 0

for i in range(1,7):
    if verbe=="aller":
        print("verbe non supporté")
    elif(verbe[0:1]=='a' or 'e' or 'i' or 'o' or 'u' or 'y'):
         print("{0:10}{1:2}".format(pronomj[depart],(verbe[:-2])+terminaisons[depart]))
         depart += 1
    elif (verbe[-3:]=="ger") and verbe != "aller":
        print("{0:10}{1:2}".format(pronoms[depart],(verbe[:-2])+terminaisonsE[depart]))
        depart += 1
    elif (verbe[-2:]=="er") and verbe != "aller":
        print("{0:10}{1:2}".format(pronoms[depart],(verbe[:-2])+terminaisons[depart]))
        depart += 1
'''




#EX4.1
liste=["bonjour","ici","fleur","fleuve","informatique"]
def MotLePlusLong(liste):
    max = 0
    for i in range(0,len(liste)):
        if len(liste[i])>=(int(max)):
            max = liste[i]
    return max


print(MotLePlusLong(liste))
