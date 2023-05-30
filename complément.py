'''
#Exercice 1

brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for c in range(0,len(texte)):
        if texte[c]>=' ' and texte[c]<='Z':
            texteBraille+=brailles[ord(texte[c])-32]
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebaille(texte))
'''
#-------------------------------------------------------------------------------

#Exercice 2
def insertionTexte(texte):
    nouveauTexte=''
    for indice in range(len(texte)-1):
        nouveauTexte+=texte[indice] + "*"
    return nouveauTexte

texte = str(input("votre texte ? "))
print(insertionTexte(texte))









