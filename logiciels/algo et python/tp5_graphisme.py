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
'''
#exercice 2
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)


def tracecible():
    cercle(128,128,85,(0,0,255))
    cercle(128,128,60,(255,0,0))
    cercle(128,128,30,(255,255,0))
tracecible()
img.show()
'''
#-----------------------------------------------------
'''
#exercice 3

from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(255,255,255))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def rectangle(x,y,largeur,hauteur,couleur):
    draw.rectangle((x,y,x+largeur, y+hauteur),fill=couleur)

def traceEffetVisuel():
    for y in range(0,14):
        for x in range(0,14):
            convy = y*20
            convx = x*20
            rectangle(convx,convy,10,10,(0,0,0))




traceEffetVisuel()
img.show()
img.save("effet.png")
'''

#-----------------------------------------------------
'''
#exercice 4

from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(0,0+x,0))
img.show()
img.save("degrade_rouge.jpg")
'''
#-----------------------------------------------------

#exercice 5

from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(0,0+x,0))

img.show()
img.save("degrade_bicolor.jpg")








