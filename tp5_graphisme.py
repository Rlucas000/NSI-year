'''
#exercice 0
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))



largeur,hauteur=img.size
draw=ImageDraw.Draw(img)
draw.line((0,0,largeur,hauteur),fill=(0,255,0))

draw.line((10,20,100,200),fill=(255,0,0))
img.show()
'''
#------------------------------------------------------
'''

#exercice 1
from PIL import Image,ImageDraw,ImageFont
ec=20
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    for i in range(1,nbDroites):
        draw.line((0+ecart,10,0+ecart,256),fill=(0,255,0))
        ecart=ecart+20
traceDroite(10,20)

img.show()
'''
#------------------------------------------------------
#exercice 2
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)


def tracecible():
    cercle(128,128,80,(0,0,255))
    cercle(128,128,60,(255,0,0))
    cercle(128,128,40,(255,255,0))
tracecible()
img.show()
