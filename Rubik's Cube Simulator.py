# Créé par gober, le 10/12/2024 en Python 3.7

from graphics import *
from Affichage import *
from time import *

#La résolution de la fenêtre graphique DOIT correspondre à celle de votre ordinateur :
haut=1080
long=1920
timer=False

f=init_graphics(long, haut)

#Séparation de l'écran en deux parties égales :
draw_line((long/2,0),(long/2,haut/1.125),blanc,f)
attendre(35)

#Création du cadre de la face visible du cube sur le droit de l'écran :
draw_rectangle((long//2+long//16,haut//1.125//8),(long-long//16,haut//1.125-haut//1.125//8),blanc,f)
attendre(35)
draw_line((0.6875*long,haut//1.125//8),(0.6875*long,haut//1.125-haut//1.125//8),blanc,f)
attendre(35)
draw_line((0.8125*long,haut//1.125//8),(0.8125*long,haut//1.125-haut//1.125//8),blanc,f)
attendre(35)
draw_line((long//2+long//16,0.3333*haut),(long-long//16,0.3333*haut),blanc,f)
attendre(35)
draw_line((long//2+long//16,0.5555*haut),(long-long//16,0.5555*haut),blanc,f)
attendre(35)



#Création du patron du cube sur le côté gauche de l'écran :
draw_rectangle((0.21875*long,0.1111*haut),(0.2890625*long,0.23611*haut),blanc,f)
attendre(35)
draw_line((0.2421875*long,0.1111*haut),(0.2421875*long,0.23333*haut),blanc,f)
attendre(35)
draw_line((0.2421875*long+0.0234375*long,0.1111*haut),(0.2421875*long+0.0234375*long,0.23333*haut),blanc,f)
attendre(35)
draw_line((0.21875*long,0.1111*haut+0.041666*haut),(0.2880625*long,0.1111*haut+0.041666*haut),blanc,f)
attendre(35)
draw_line((0.21875*long,0.1111*haut+(2*0.041666*haut)),(0.2880625*long,0.1111*haut+(0.041666*haut*2)),blanc,f)
attendre(35)


draw_rectangle((0.21875*long,0.29167*haut),(0.2890625*long,0.416667*haut),blanc,f)
attendre(35)
draw_line((0.2421875*long,0.29167*haut),(0.2421875*long,0.413*haut),blanc,f)
attendre(35)
draw_line((0.2421875*long+0.0234375*long,0.29167*haut),(0.2421875*long+0.0234375*long,0.413*haut),blanc,f)
attendre(35)
draw_line((0.21875*long,0.29167*haut+0.041666*haut),(0.2880625*long,0.29167*haut+0.041666*haut),blanc,f)
attendre(35)
draw_line((0.21875*long,0.29167*haut+(2*0.041666*haut)),(0.2880625*long,0.29167*haut+(0.041666*haut*2)),blanc,f)
attendre(35)

draw_rectangle((0.21875*long,0.4722*haut),(0.2890625*long,0.59722*haut),blanc,f)
attendre(35)
draw_line((0.2421875*long,0.4722*haut),(0.2421875*long,0.59422*haut),blanc,f)
attendre(35)
draw_line((0.2421875*long+0.0234375*long,0.4722*haut),(0.2421875*long+0.0234375*long,0.59422*haut),blanc,f)
attendre(35)
draw_line((0.21875*long,0.4722*haut+0.041666*haut),(0.2880625*long,0.4722*haut+0.041666*haut),blanc,f)
attendre(35)
draw_line((0.21875*long,0.4722*haut+(2*0.041666*haut)),(0.2880625*long,0.4722*haut+(0.041666*haut*2)),blanc,f)
attendre(35)

draw_rectangle((0.21875*long,0.652778*haut),(0.2890625*long,0.777778*haut),blanc,f)
attendre(35)
draw_line((0.2421875*long,0.652778*haut),(0.2421875*long,0.774445*haut),blanc,f)
attendre(35)
draw_line((0.2421875*long+0.0234375*long,0.652778*haut),(0.2421875*long+0.0234375*long,0.774445*haut),blanc,f)
attendre(35)
draw_line((0.21875*long,0.652778*haut+0.041666*haut),(0.2880625*long,0.652778*haut+0.041666*haut),blanc,f)
attendre(35)
draw_line((0.21875*long,0.652778*haut+(2*0.041666*haut)),(0.2880625*long,0.652778*haut+(0.041666*haut*2)),blanc,f)
attendre(35)

draw_rectangle((0.1171875*long,0.291667*haut),(0.1875*long,0.416667*haut),blanc,f)
attendre(35)
draw_line((0.1171875*long+0.0234375*long,0.29167*haut),(0.1171875*long+0.0234375*long,0.415333*haut),blanc,f)
attendre(35)
draw_line((0.1171875*long+(2*0.0234375*long),0.29167*haut),(0.1171875*long+(0.0234375*long*2),0.415333*haut),blanc,f)
attendre(35)
draw_line((0.1171875*long,0.29167*haut+0.041666*haut),(0.1865*long,0.29167*haut+0.041666*haut),blanc,f)
attendre(35)
draw_line((0.1171875*long,0.29167*haut+(2*0.041666*haut)),(0.1865*long,0.29167*haut+(0.041666*haut*2)),blanc,f)
attendre(35)

draw_rectangle((0.3203125*long,0.291667*haut),(0.390625*long,0.416667*haut),blanc,f)
attendre(35)
draw_line((0.3203125*long+0.0234375*long,0.29167*haut),(0.3203125*long+0.0234375*long,0.415333*haut),blanc,f)
attendre(35)
draw_line((0.3203125*long+(2*0.0234375*long),0.29167*haut),(0.3203125*long+(2*0.0234375*long),0.415333*haut),blanc,f)
attendre(35)
draw_line((0.3203125*long,0.29167*haut+0.041666*haut),(0.389*long,0.29167*haut+0.041666*haut),blanc,f)
attendre(35)
draw_line((0.3203125*long,0.29167*haut+(2*0.041666*haut)),(0.389*long,0.29167*haut+(0.041666*haut*2)),blanc,f)
attendre(35)

#Création des différentes touches en bas de l'écran :
for i in range(16) :
    draw_rectangle((0.0625*long*i,haut//1.125),(0.0625*long*i+0.0625*long,haut),gris,f)
    attendre(35)

ecrire("U",(0.009375*long,0.89444*haut),0.05625*long,blanc,f)
attendre(35)
ecrire("U'",(0.009375*long+(0.0625*long),0.89444*haut),0.05625*long,blanc,f)
attendre(35)
ecrire("R",(0.009375*long+(0.0625*long*2),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("R'",(0.009375*long+(0.0625*long*3),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("L",(0.009375*long+(0.0625*long*4),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("L'",(0.009375*long+(0.0625*long*5),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("D",(0.009375*long+(0.0625*long*6),0.9*haut),0.05625*long,blanc,f)
attendre(35)
ecrire("D'",(0.009375*long+(0.0625*long*7),0.9*haut),0.05625*long,blanc,f)
attendre(35)
ecrire("F",(0.009375*long+(0.0625*long*8),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("F'",(0.009375*long+(0.0625*long*9),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("B",(0.009375*long+(0.0625*long*10),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("B'",(0.009375*long+(0.0625*long*11),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("M",(0.007595*long+(0.0625*long*12),0.90555*haut),0.05125*long,blanc,f)
attendre(35)
ecrire("M'",(0.007595*long+(0.0625*long*13),0.90555*haut),0.05125*long,blanc,f)
attendre(35)
ecrire("E",(0.009375*long+(0.0625*long*14),0.88888*haut),0.0625*long,blanc,f)
attendre(35)
ecrire("E'",(0.009375*long+(0.0625*long*15),0.88888*haut),0.0625*long,blanc,f)
attendre(35)


#Création des valeurs de chaques faces du cube :
FaceF = {
    "un":rouge,
    "deux":rouge,
    "trois":rouge,
    "quatre":rouge,
    "cinq":rouge,
    "six":rouge,
    "sept":rouge,
    "huit":rouge,
    "neuf":rouge
}

FaceD = {
    "un":bleu,
    "deux":bleu,
    "trois":bleu,
    "quatre":bleu,
    "cinq":bleu,
    "six":bleu,
    "sept":bleu,
    "huit":bleu,
    "neuf":bleu
}

FaceR = {
    "un":blanc,
    "deux":blanc,
    "trois":blanc,
    "quatre":blanc,
    "cinq":blanc,
    "six":blanc,
    "sept":blanc,
    "huit":blanc,
    "neuf":blanc
}

FaceB = {
    "un":orange,
    "deux":orange,
    "trois":orange,
    "quatre":orange,
    "cinq":orange,
    "six":orange,
    "sept":orange,
    "huit":orange,
    "neuf":orange
}

FaceU = {
    "un":vert,
    "deux":vert,
    "trois":vert,
    "quatre":vert,
    "cinq":vert,
    "six":vert,
    "sept":vert,
    "huit":vert,
    "neuf":vert
}

FaceL = {
    "un":jaune,
    "deux":jaune,
    "trois":jaune,
    "quatre":jaune,
    "cinq":jaune,
    "six":jaune,
    "sept":jaune,
    "huit":jaune,
    "neuf":jaune
}



#Création de la case Escape
draw_rectangle((long-0.0625*long,0.111111*haut),(long,0),blanc,f)
ecrire("ESC",(long-0.0625*long,0),0.03125*long,blanc,f)

#Création de la case Reset
draw_rectangle((long/2,0),(long/2+0.0625*long,0.111111*haut),blanc,f)
ecrire("RES",(long/2,0),0.03125*long,blanc,f)

#Création de la case scramble
draw_rectangle((long/2-0.0625*long,0),(long/2,0.111111*haut),blanc,f)
ecrire("SCR",(long/2-0.0625*long,0),0.03125*long,blanc,f)

#Création des listes d'algorithmes :
draw_rectangle((0,0.7777*haut),(0.0625*long,0.8888*haut),blanc,f)
ecrire("ALG",(0,0.78888*haut),0.03125*long,blanc,f)




changement={"un":"","deux":"","trois":"","quatre":"","cinq":"","six":""}
#Création des fonctions commandes :
def U(Face) :
    if Face==FaceU :
        B(FaceF)
    elif Face==FaceD :
        F(FaceF)
    elif Face==FaceB :
        D(FaceF)
    elif Face==FaceL :
        U(FaceF)
    elif Face==FaceR :
        U(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceF["un"]
        changement["deux"]=FaceF["deux"]
        changement["trois"]=FaceF["trois"]
        changement["quatre"]=FaceU["un"]
        changement["cinq"]=FaceU["deux"]
        FaceF["un"]=FaceR["un"]
        FaceF["deux"]=FaceR["deux"]
        FaceF["trois"]=FaceR["trois"]
        FaceR["un"]=FaceB["neuf"]
        FaceR["deux"]=FaceB["huit"]
        FaceR["trois"]=FaceB["sept"]
        FaceB["neuf"]=FaceL["un"]
        FaceB["huit"]=FaceL["deux"]
        FaceB["sept"]=FaceL["trois"]
        FaceL["un"]=changement["un"]
        FaceL["deux"]=changement["deux"]
        FaceL["trois"]=changement["trois"]
        FaceU["un"]=FaceU["sept"]
        FaceU["sept"]=FaceU["neuf"]
        FaceU["neuf"]=FaceU["trois"]
        FaceU["trois"]=changement["quatre"]
        FaceU["deux"]=FaceU["quatre"]
        FaceU["quatre"]=FaceU["huit"]
        FaceU["huit"]=FaceU["six"]
        FaceU["six"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)

def UU(Face) :
    if Face==FaceU :
        BB(FaceF)
    elif Face==FaceD :
        FF(FaceF)
    elif Face==FaceB :
        DD(FaceF)
    elif Face==FaceL :
        UU(FaceF)
    elif Face==FaceR :
        UU(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceF["un"]
        changement["deux"]=FaceF["deux"]
        changement["trois"]=FaceF["trois"]
        changement["quatre"]=FaceU["un"]
        changement["cinq"]=FaceU["deux"]
        FaceF["un"]=FaceL["un"]
        FaceF["deux"]=FaceL["deux"]
        FaceF["trois"]=FaceL["trois"]
        FaceL["un"]=FaceB["neuf"]
        FaceL["deux"]=FaceB["huit"]
        FaceL["trois"]=FaceB["sept"]
        FaceB["neuf"]=FaceR["un"]
        FaceB["huit"]=FaceR["deux"]
        FaceB["sept"]=FaceR["trois"]
        FaceR["un"]=changement["un"]
        FaceR["deux"]=changement["deux"]
        FaceR["trois"]=changement["trois"]
        FaceU["un"]=FaceU["trois"]
        FaceU["trois"]=FaceU["neuf"]
        FaceU["neuf"]=FaceU["sept"]
        FaceU["sept"]=changement["quatre"]
        FaceU["deux"]=FaceU["six"]
        FaceU["six"]=FaceU["huit"]
        FaceU["huit"]=FaceU["quatre"]
        FaceU["quatre"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def R(Face) :
    if Face==FaceU :
        R(FaceF)
    elif Face==FaceD :
        R(FaceF)
    elif Face==FaceB :
        R(FaceF)
    elif Face==FaceL :
        F(FaceF)
    elif Face==FaceR :
        B(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceF["trois"]
        changement["deux"]=FaceF["six"]
        changement["trois"]=FaceF["neuf"]
        changement["quatre"]=FaceR["un"]
        changement["cinq"]=FaceR["deux"]
        FaceF["trois"]=FaceD["trois"]
        FaceF["six"]=FaceD["six"]
        FaceF["neuf"]=FaceD["neuf"]
        FaceD["trois"]=FaceB["trois"]
        FaceD["six"]=FaceB["six"]
        FaceD["neuf"]=FaceB["neuf"]
        FaceB["trois"]=FaceU["trois"]
        FaceB["six"]=FaceU["six"]
        FaceB["neuf"]=FaceU["neuf"]
        FaceU["trois"]=changement["un"]
        FaceU["six"]=changement["deux"]
        FaceU["neuf"]=changement["trois"]
        FaceR["un"]=FaceR["sept"]
        FaceR["sept"]=FaceR["neuf"]
        FaceR["neuf"]=FaceR["trois"]
        FaceR["trois"]=changement["quatre"]
        FaceR["deux"]=FaceR["quatre"]
        FaceR["quatre"]=FaceR["huit"]
        FaceR["huit"]=FaceR["six"]
        FaceR["six"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def RR(Face) :
    if Face==FaceU :
        RR(FaceF)
    elif Face==FaceD :
        RR(FaceF)
    elif Face==FaceB :
        RR(FaceF)
    elif Face==FaceL :
        FF(FaceF)
    elif Face==FaceR :
        BB(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceF["trois"]
        changement["deux"]=FaceF["six"]
        changement["trois"]=FaceF["neuf"]
        changement["quatre"]=FaceR["un"]
        changement["cinq"]=FaceR["deux"]
        FaceF["trois"]=FaceU["trois"]
        FaceF["six"]=FaceU["six"]
        FaceF["neuf"]=FaceU["neuf"]
        FaceU["trois"]=FaceB["trois"]
        FaceU["six"]=FaceB["six"]
        FaceU["neuf"]=FaceB["neuf"]
        FaceB["trois"]=FaceD["trois"]
        FaceB["six"]=FaceD["six"]
        FaceB["neuf"]=FaceD["neuf"]
        FaceD["trois"]=changement["un"]
        FaceD["six"]=changement["deux"]
        FaceD["neuf"]=changement["trois"]
        FaceR["un"]=FaceR["trois"]
        FaceR["trois"]=FaceR["neuf"]
        FaceR["neuf"]=FaceR["sept"]
        FaceR["sept"]=changement["quatre"]
        FaceR["deux"]=FaceR["six"]
        FaceR["six"]=FaceR["huit"]
        FaceR["huit"]=FaceR["quatre"]
        FaceR["quatre"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)




def L(Face) :
    if Face==FaceU :
        L(FaceF)
    elif Face==FaceD :
        L(FaceF)
    elif Face==FaceB :
        L(FaceF)
    elif Face==FaceL :
        B(FaceF)
    elif Face==FaceR :
        F(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceF["un"]
        changement["deux"]=FaceF["quatre"]
        changement["trois"]=FaceF["sept"]
        changement["quatre"]=FaceL["un"]
        changement["cinq"]=FaceL["deux"]
        FaceF["un"]=FaceU["un"]
        FaceF["quatre"]=FaceU["quatre"]
        FaceF["sept"]=FaceU["sept"]
        FaceU["un"]=FaceB["un"]
        FaceU["quatre"]=FaceB["quatre"]
        FaceU["sept"]=FaceB["sept"]
        FaceB["un"]=FaceD["un"]
        FaceB["quatre"]=FaceD["quatre"]
        FaceB["sept"]=FaceD["sept"]
        FaceD["un"]=changement["un"]
        FaceD["quatre"]=changement["deux"]
        FaceD["sept"]=changement["trois"]
        FaceL["un"]=FaceL["sept"]
        FaceL["sept"]=FaceL["neuf"]
        FaceL["neuf"]=FaceL["trois"]
        FaceL["trois"]=changement["quatre"]
        FaceL["deux"]=FaceL["quatre"]
        FaceL["quatre"]=FaceL["huit"]
        FaceL["huit"]=FaceL["six"]
        FaceL["six"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def LL(Face) :
    if Face==FaceU :
        LL(FaceF)
    elif Face==FaceD :
        LL(FaceF)
    elif Face==FaceB :
        LL(FaceF)
    elif Face==FaceL :
        BB(FaceF)
    elif Face==FaceR :
        FF(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceF["un"]
        changement["deux"]=FaceF["quatre"]
        changement["trois"]=FaceF["sept"]
        changement["quatre"]=FaceL["un"]
        changement["cinq"]=FaceL["deux"]
        FaceF["un"]=FaceD["un"]
        FaceF["quatre"]=FaceD["quatre"]
        FaceF["sept"]=FaceD["sept"]
        FaceD["un"]=FaceB["un"]
        FaceD["quatre"]=FaceB["quatre"]
        FaceD["sept"]=FaceB["sept"]
        FaceB["un"]=FaceU["un"]
        FaceB["quatre"]=FaceU["quatre"]
        FaceB["sept"]=FaceU["sept"]
        FaceU["un"]=changement["un"]
        FaceU["quatre"]=changement["deux"]
        FaceU["sept"]=changement["trois"]
        FaceL["un"]=FaceL["trois"]
        FaceL["trois"]=FaceL["neuf"]
        FaceL["neuf"]=FaceL["sept"]
        FaceL["sept"]=changement["quatre"]
        FaceL["deux"]=FaceL["six"]
        FaceL["six"]=FaceL["huit"]
        FaceL["huit"]=FaceL["quatre"]
        FaceL["quatre"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)



def D(Face) :
    if Face==FaceU :
        F(FaceF)
    elif Face==FaceD :
        B(FaceF)
    elif Face==FaceB :
        U(FaceF)
    elif Face==FaceL :
        D(FaceF)
    elif Face==FaceR :
        D(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceF["sept"]
        changement["deux"]=FaceF["huit"]
        changement["trois"]=FaceF["neuf"]
        changement["quatre"]=FaceD["un"]
        changement["cinq"]=FaceD["deux"]
        FaceF["sept"]=FaceL["sept"]
        FaceF["huit"]=FaceL["huit"]
        FaceF["neuf"]=FaceL["neuf"]
        FaceL["sept"]=FaceB["trois"]
        FaceL["huit"]=FaceB["deux"]
        FaceL["neuf"]=FaceB["un"]
        FaceB["trois"]=FaceR["sept"]
        FaceB["deux"]=FaceR["huit"]
        FaceB["un"]=FaceR["neuf"]
        FaceR["sept"]=changement["un"]
        FaceR["huit"]=changement["deux"]
        FaceR["neuf"]=changement["trois"]
        FaceD["un"]=FaceD["sept"]
        FaceD["sept"]=FaceD["neuf"]
        FaceD["neuf"]=FaceD["trois"]
        FaceD["trois"]=changement["quatre"]
        FaceD["deux"]=FaceD["quatre"]
        FaceD["quatre"]=FaceD["huit"]
        FaceD["huit"]=FaceD["six"]
        FaceD["six"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def DD(Face) :
    if Face==FaceU :
        FF(FaceF)
    elif Face==FaceD :
        BB(FaceF)
    elif Face==FaceB :
        UU(FaceF)
    elif Face==FaceL :
        DD(FaceF)
    elif Face==FaceR :
        DD(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceF["sept"]
        changement["deux"]=FaceF["huit"]
        changement["trois"]=FaceF["neuf"]
        changement["quatre"]=FaceD["un"]
        changement["cinq"]=FaceD["deux"]
        FaceF["sept"]=FaceR["sept"]
        FaceF["huit"]=FaceR["huit"]
        FaceF["neuf"]=FaceR["neuf"]
        FaceR["sept"]=FaceB["trois"]
        FaceR["huit"]=FaceB["deux"]
        FaceR["neuf"]=FaceB["un"]
        FaceB["trois"]=FaceL["sept"]
        FaceB["deux"]=FaceL["huit"]
        FaceB["un"]=FaceL["neuf"]
        FaceL["sept"]=changement["un"]
        FaceL["huit"]=changement["deux"]
        FaceL["neuf"]=changement["trois"]
        FaceD["un"]=FaceD["trois"]
        FaceD["trois"]=FaceD["neuf"]
        FaceD["neuf"]=FaceD["sept"]
        FaceD["sept"]=changement["quatre"]
        FaceD["deux"]=FaceD["six"]
        FaceD["six"]=FaceD["huit"]
        FaceD["huit"]=FaceD["quatre"]
        FaceD["quatre"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def F(Face) :
    if Face==FaceU :
        U(FaceF)
    elif Face==FaceD :
        D(FaceF)
    elif Face==FaceB :
        B(FaceF)
    elif Face==FaceL :
        L(FaceF)
    elif Face==FaceR :
        R(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceU["sept"]
        changement["deux"]=FaceU["huit"]
        changement["trois"]=FaceU["neuf"]
        changement["quatre"]=FaceF["un"]
        changement["cinq"]=FaceF["deux"]
        FaceU["sept"]=FaceL["neuf"]
        FaceU["huit"]=FaceL["six"]
        FaceU["neuf"]=FaceL["trois"]
        FaceL["neuf"]=FaceD["trois"]
        FaceL["six"]=FaceD["deux"]
        FaceL["trois"]=FaceD["un"]
        FaceD["trois"]=FaceR["un"]
        FaceD["deux"]=FaceR["quatre"]
        FaceD["un"]=FaceR["sept"]
        FaceR["un"]=changement["un"]
        FaceR["quatre"]=changement["deux"]
        FaceR["sept"]=changement["trois"]
        FaceF["un"]=FaceF["sept"]
        FaceF["sept"]=FaceF["neuf"]
        FaceF["neuf"]=FaceF["trois"]
        FaceF["trois"]=changement["quatre"]
        FaceF["deux"]=FaceF["quatre"]
        FaceF["quatre"]=FaceF["huit"]
        FaceF["huit"]=FaceF["six"]
        FaceF["six"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)



def FF(Face) :
    if Face==FaceU :
        UU(FaceF)
    elif Face==FaceD :
        DD(FaceF)
    elif Face==FaceB :
        BB(FaceF)
    elif Face==FaceL :
        LL(FaceF)
    elif Face==FaceR :
        RR(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceU["sept"]
        changement["deux"]=FaceU["huit"]
        changement["trois"]=FaceU["neuf"]
        changement["quatre"]=FaceF["un"]
        changement["cinq"]=FaceF["deux"]
        FaceU["sept"]=FaceR["un"]
        FaceU["huit"]=FaceR["quatre"]
        FaceU["neuf"]=FaceR["sept"]
        FaceR["un"]=FaceD["trois"]
        FaceR["quatre"]=FaceD["deux"]
        FaceR["sept"]=FaceD["un"]
        FaceD["trois"]=FaceL["neuf"]
        FaceD["deux"]=FaceL["six"]
        FaceD["un"]=FaceL["trois"]
        FaceL["neuf"]=changement["un"]
        FaceL["six"]=changement["deux"]
        FaceL["trois"]=changement["trois"]
        FaceF["un"]=FaceF["trois"]
        FaceF["trois"]=FaceF["neuf"]
        FaceF["neuf"]=FaceF["sept"]
        FaceF["sept"]=changement["quatre"]
        FaceF["deux"]=FaceF["six"]
        FaceF["six"]=FaceF["huit"]
        FaceF["huit"]=FaceF["quatre"]
        FaceF["quatre"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)




def B(Face) :
    if Face==FaceU :
        D(FaceF)
    elif Face==FaceD :
        U(FaceF)
    elif Face==FaceB :
        F(FaceF)
    elif Face==FaceL :
        R(FaceF)
    elif Face==FaceR :
        L(FaceF)
    elif Face==FaceF :
        changement["un"]=FaceU["un"]
        changement["deux"]=FaceU["deux"]
        changement["trois"]=FaceU["trois"]
        changement["quatre"]=FaceB["un"]
        changement["cinq"]=FaceB["deux"]
        FaceU["un"]=FaceR["trois"]
        FaceU["deux"]=FaceR["six"]
        FaceU["trois"]=FaceR["neuf"]
        FaceR["trois"]=FaceD["neuf"]
        FaceR["six"]=FaceD["huit"]
        FaceR["neuf"]=FaceD["sept"]
        FaceD["neuf"]=FaceL["sept"]
        FaceD["huit"]=FaceL["quatre"]
        FaceD["sept"]=FaceL["un"]
        FaceL["sept"]=changement["un"]
        FaceL["quatre"]=changement["deux"]
        FaceL["un"]=changement["trois"]
        FaceB["un"]=FaceB["sept"]
        FaceB["sept"]=FaceB["neuf"]
        FaceB["neuf"]=FaceB["trois"]
        FaceB["trois"]=changement["quatre"]
        FaceB["deux"]=FaceB["quatre"]
        FaceB["quatre"]=FaceB["huit"]
        FaceB["huit"]=FaceB["six"]
        FaceB["six"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)



def BB(Face) :
    if Face==FaceU :
        DD(FaceF)
    elif Face==FaceD :
        UU(FaceF)
    elif Face==FaceB :
        FF(FaceF)
    elif Face==FaceL :
        RR(FaceF)
    elif Face==FaceR :
        LL(FaceF)
    elif Face==FaceF:
        changement["un"]=FaceU["un"]
        changement["deux"]=FaceU["deux"]
        changement["trois"]=FaceU["trois"]
        changement["quatre"]=FaceB["un"]
        changement["cinq"]=FaceB["deux"]
        FaceU["un"]=FaceL["sept"]
        FaceU["deux"]=FaceL["quatre"]
        FaceU["trois"]=FaceL["un"]
        FaceL["sept"]=FaceD["neuf"]
        FaceL["quatre"]=FaceD["huit"]
        FaceL["un"]=FaceD["sept"]
        FaceD["neuf"]=FaceR["trois"]
        FaceD["huit"]=FaceR["six"]
        FaceD["sept"]=FaceR["neuf"]
        FaceR["trois"]=changement["un"]
        FaceR["six"]=changement["deux"]
        FaceR["neuf"]=changement["trois"]
        FaceB["un"]=FaceB["trois"]
        FaceB["trois"]=FaceB["neuf"]
        FaceB["neuf"]=FaceB["sept"]
        FaceB["sept"]=changement["quatre"]
        FaceB["deux"]=FaceB["six"]
        FaceB["six"]=FaceB["huit"]
        FaceB["huit"]=FaceB["quatre"]
        FaceB["quatre"]=changement["cinq"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def M(Face) :
    if Face==FaceU :
        M(FaceF)
    elif Face==FaceD :
        M(FaceF)
    elif Face==FaceB :
        M(FaceF)
    elif Face==FaceL :
        EE(FaceU)
    elif Face==FaceR :
        E(FaceU)
    elif Face==FaceF:
        changement["un"]=FaceF["deux"]
        changement["deux"]=FaceF["cinq"]
        changement["trois"]=FaceF["huit"]
        FaceF["deux"]=FaceD["deux"]
        FaceF["cinq"]=FaceD["cinq"]
        FaceF["huit"]=FaceD["huit"]
        FaceD["deux"]=FaceB["deux"]
        FaceD["cinq"]=FaceB["cinq"]
        FaceD["huit"]=FaceB["huit"]
        FaceB["deux"]=FaceU["deux"]
        FaceB["cinq"]=FaceU["cinq"]
        FaceB["huit"]=FaceU["huit"]
        FaceU["deux"]=changement["un"]
        FaceU["cinq"]=changement["deux"]
        FaceU["huit"]=changement["trois"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def MM(Face) :
    if Face==FaceU :
        MM(FaceF)
    elif Face==FaceD :
        MM(FaceF)
    elif Face==FaceB :
        MM(FaceF)
    elif Face==FaceL :
        E(FaceU)
    elif Face==FaceR :
        EE(FaceU)
    elif Face==FaceF:
        changement["un"]=FaceF["deux"]
        changement["deux"]=FaceF["cinq"]
        changement["trois"]=FaceF["huit"]
        FaceF["deux"]=FaceU["deux"]
        FaceF["cinq"]=FaceU["cinq"]
        FaceF["huit"]=FaceU["huit"]
        FaceU["deux"]=FaceB["deux"]
        FaceU["cinq"]=FaceB["cinq"]
        FaceU["huit"]=FaceB["huit"]
        FaceB["deux"]=FaceD["deux"]
        FaceB["cinq"]=FaceD["cinq"]
        FaceB["huit"]=FaceD["huit"]
        FaceD["deux"]=changement["un"]
        FaceD["cinq"]=changement["deux"]
        FaceD["huit"]=changement["trois"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def E(Face) :
    if Face==FaceU :
        changement["un"]=FaceU["quatre"]
        changement["deux"]=FaceU["cinq"]
        changement["trois"]=FaceU["six"]
        FaceU["quatre"]=FaceR["deux"]
        FaceU["cinq"]=FaceR["cinq"]
        FaceU["six"]=FaceR["huit"]
        FaceR["deux"]=FaceD["quatre"]
        FaceR["cinq"]=FaceD["cinq"]
        FaceR["huit"]=FaceD["six"]
        FaceD["quatre"]=FaceL["deux"]
        FaceD["cinq"]=FaceL["cinq"]
        FaceD["six"]=FaceL["huit"]
        FaceL["deux"]=changement["un"]
        FaceL["cinq"]=changement["deux"]
        FaceL["huit"]=changement["trois"]
    elif Face==FaceD :
        EE(FaceU)
    elif Face==FaceB :
        EE(FaceF)
    elif Face==FaceL :
        E(FaceF)
    elif Face==FaceR :
        E(FaceF)
    elif Face==FaceF:
        changement["un"]=FaceF["quatre"]
        changement["deux"]=FaceF["cinq"]
        changement["trois"]=FaceF["six"]
        FaceF["quatre"]=FaceR["quatre"]
        FaceF["cinq"]=FaceR["cinq"]
        FaceF["six"]=FaceR["six"]
        FaceR["quatre"]=FaceB["six"]
        FaceR["cinq"]=FaceB["cinq"]
        FaceR["six"]=FaceB["quatre"]
        FaceB["six"]=FaceL["quatre"]
        FaceB["cinq"]=FaceL["cinq"]
        FaceB["quatre"]=FaceL["six"]
        FaceL["quatre"]=changement["un"]
        FaceL["cinq"]=changement["deux"]
        FaceL["six"]=changement["trois"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)


def EE(Face) :
    if Face==FaceU :
        changement["un"]=FaceU["quatre"]
        changement["deux"]=FaceU["cinq"]
        changement["trois"]=FaceU["six"]
        FaceU["quatre"]=FaceL["deux"]
        FaceU["cinq"]=FaceL["cinq"]
        FaceU["six"]=FaceL["huit"]
        FaceL["deux"]=FaceD["quatre"]
        FaceL["cinq"]=FaceD["cinq"]
        FaceL["huit"]=FaceD["six"]
        FaceD["quatre"]=FaceR["deux"]
        FaceD["cinq"]=FaceR["cinq"]
        FaceD["six"]=FaceR["huit"]
        FaceR["deux"]=changement["un"]
        FaceR["cinq"]=changement["deux"]
        FaceR["huit"]=changement["trois"]
    elif Face==FaceD :
        E(FaceU)
    elif Face==FaceB :
        E(FaceF)
    elif Face==FaceL :
        EE(FaceF)
    elif Face==FaceR :
        EE(FaceF)
    elif Face==FaceF:
        changement["un"]=FaceF["quatre"]
        changement["deux"]=FaceF["cinq"]
        changement["trois"]=FaceF["six"]
        FaceF["quatre"]=FaceL["quatre"]
        FaceF["cinq"]=FaceL["cinq"]
        FaceF["six"]=FaceL["six"]
        FaceL["quatre"]=FaceB["six"]
        FaceL["cinq"]=FaceB["cinq"]
        FaceL["six"]=FaceB["quatre"]
        FaceB["six"]=FaceR["quatre"]
        FaceB["cinq"]=FaceR["cinq"]
        FaceB["quatre"]=FaceR["six"]
        FaceR["quatre"]=changement["un"]
        FaceR["cinq"]=changement["deux"]
        FaceR["six"]=changement["trois"]
        if cerclePosition==1 :
            couleurFace(long,haut,FaceU,f)
        elif cerclePosition==2 :
            couleurFace(long,haut,FaceF,f)
        elif cerclePosition==3 :
            couleurFace(long,haut,FaceD,f)
        elif cerclePosition==4:
            couleurFace(long,haut,FaceB,f)
        elif cerclePosition==5:
            couleurFace(long,haut,FaceL,f)
        elif cerclePosition==6:
            couleurFace(long,haut,FaceR,f)



#Création de l'interaction entre l'utilisateur et la fenêtre graphique :
#afficher le cercle rouge:
cerclePosition = 2
def dessinerCercle(cerclePosition) :
    cercleReset(long,haut,f)
    if cerclePosition==1 :
        draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long,(0.23611*haut-0.1111*haut)/2+0.1111*haut),(0.23611*haut-0.1111*haut)/1.4,rouge,f)
    elif cerclePosition==2:
        draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long,(0.416667*haut-0.29167*haut)/2+0.29167*haut),(0.416667*haut-0.29167*haut)/1.4,rouge,f)
    elif cerclePosition==3:
        draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long,(0.59722*haut-0.4722*haut)/2+0.4722*haut),(0.59722*haut-0.4722*haut)/1.4,rouge,f)
    elif cerclePosition==4:
        draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long,(0.777778*haut-0.652778*haut)/2+0.652778*haut),(0.777778*haut-0.652778*haut)/1.4,rouge,f)
    elif cerclePosition==5:
        draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long-0.1015625*long,(0.416667*haut-0.29167*haut)/2+0.29167*haut),(0.416667*haut-0.29167*haut)/1.4,rouge,f)
    elif cerclePosition==6:
        draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long+0.1015625*long,(0.416667*haut-0.29167*haut)/2+0.29167*haut),(0.416667*haut-0.29167*haut)/1.4,rouge,f)
dessinerCercle(cerclePosition)


#Création du mélangeur de cube
scramble = []
scrambleMoovs=[]
def scrambleCube(long,haut,f):
    moves = ["U","U'","U²","R","R'","R²","L","L'","L²","D","D'","D²","F","F'","F²","B","B'","B²","M","M'","M²","E","E'","E²"]
    scrambleMoovs=moves.copy()
    scramble = []
    reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
    for i in range (20):
        scramble.append(scrambleMoovs[alea_int(0,(len(scrambleMoovs))-1)])
        scrambleMoovs=moves.copy()
        if scramble[i]=="U":
            scrambleMoovs.remove("U")
            scrambleMoovs.remove("U'")
            scrambleMoovs.remove("U²")
            scrambleMoovs.remove("D'")
            scrambleMoovs.remove("E")
        elif scramble[i]=="U'":
            scrambleMoovs.remove("U")
            scrambleMoovs.remove("U'")
            scrambleMoovs.remove("U²")
            scrambleMoovs.remove("D")
            scrambleMoovs.remove("E'")
        elif scramble[i]=="U²":
            scrambleMoovs.remove("U")
            scrambleMoovs.remove("U'")
            scrambleMoovs.remove("U²")
            scrambleMoovs.remove("D²")
            scrambleMoovs.remove("E²")
        elif scramble[i]=="R":
            scrambleMoovs.remove("R")
            scrambleMoovs.remove("R'")
            scrambleMoovs.remove("R²")
            scrambleMoovs.remove("M")
            scrambleMoovs.remove("L'")
        elif scramble[i]=="R'":
            scrambleMoovs.remove("R")
            scrambleMoovs.remove("R'")
            scrambleMoovs.remove("R²")
            scrambleMoovs.remove("M'")
            scrambleMoovs.remove("L")
        elif scramble[i]=="R²":
            scrambleMoovs.remove("R")
            scrambleMoovs.remove("R'")
            scrambleMoovs.remove("R²")
            scrambleMoovs.remove("M²")
            scrambleMoovs.remove("L²")
        elif scramble[i]=="L":
            scrambleMoovs.remove("L")
            scrambleMoovs.remove("L'")
            scrambleMoovs.remove("L²")
            scrambleMoovs.remove("M'")
            scrambleMoovs.remove("R'")
        elif scramble[i]=="L'":
            scrambleMoovs.remove("L")
            scrambleMoovs.remove("L'")
            scrambleMoovs.remove("L²")
            scrambleMoovs.remove("M")
            scrambleMoovs.remove("R")
        elif scramble[i]=="L²":
            scrambleMoovs.remove("L")
            scrambleMoovs.remove("L'")
            scrambleMoovs.remove("L²")
            scrambleMoovs.remove("M²")
            scrambleMoovs.remove("R²")
        elif scramble[i]=="D":
            scrambleMoovs.remove("D")
            scrambleMoovs.remove("D'")
            scrambleMoovs.remove("D²")
            scrambleMoovs.remove("U'")
            scrambleMoovs.remove("E'")
        elif scramble[i]=="D'":
            scrambleMoovs.remove("D")
            scrambleMoovs.remove("D'")
            scrambleMoovs.remove("D²")
            scrambleMoovs.remove("U")
            scrambleMoovs.remove("E")
        elif scramble[i]=="D²":
            scrambleMoovs.remove("D")
            scrambleMoovs.remove("D'")
            scrambleMoovs.remove("D²")
            scrambleMoovs.remove("U'")
            scrambleMoovs.remove("U²")
        elif scramble[i]=="F":
            scrambleMoovs.remove("F")
            scrambleMoovs.remove("F'")
            scrambleMoovs.remove("F²")
        elif scramble[i]=="F'":
            scrambleMoovs.remove("F")
            scrambleMoovs.remove("F'")
            scrambleMoovs.remove("F²")
        elif scramble[i]=="F²":
            scrambleMoovs.remove("F")
            scrambleMoovs.remove("F'")
            scrambleMoovs.remove("F²")
        elif scramble[i]=="B":
            scrambleMoovs.remove("B")
            scrambleMoovs.remove("B'")
            scrambleMoovs.remove("B²")
        elif scramble[i]=="B'":
            scrambleMoovs.remove("B")
            scrambleMoovs.remove("B'")
            scrambleMoovs.remove("B²")
        elif scramble[i]=="B²":
            scrambleMoovs.remove("B")
            scrambleMoovs.remove("B'")
            scrambleMoovs.remove("B²")
        elif scramble[i]=="M":
            scrambleMoovs.remove("M")
            scrambleMoovs.remove("M'")
            scrambleMoovs.remove("M²")
            scrambleMoovs.remove("R")
            scrambleMoovs.remove("L'")
        elif scramble[i]=="M'":
            scrambleMoovs.remove("M")
            scrambleMoovs.remove("M'")
            scrambleMoovs.remove("M²")
            scrambleMoovs.remove("R'")
            scrambleMoovs.remove("L")
        elif scramble[i]=="M²":
            scrambleMoovs.remove("M")
            scrambleMoovs.remove("M'")
            scrambleMoovs.remove("M²")
            scrambleMoovs.remove("R²")
            scrambleMoovs.remove("L²")
        elif scramble[i]=="E":
            scrambleMoovs.remove("E")
            scrambleMoovs.remove("E'")
            scrambleMoovs.remove("E²")
            scrambleMoovs.remove("U")
            scrambleMoovs.remove("D'")
        elif scramble[i]=="E'":
            scrambleMoovs.remove("E")
            scrambleMoovs.remove("E'")
            scrambleMoovs.remove("E²")
            scrambleMoovs.remove("U'")
            scrambleMoovs.remove("D")
        elif scramble[i]=="E²":
            scrambleMoovs.remove("E")
            scrambleMoovs.remove("E'")
            scrambleMoovs.remove("E²")
            scrambleMoovs.remove("U²")
            scrambleMoovs.remove("D²")

        if scramble[i]=="U":
            U(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="U'":
            UU(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="U²":
            U(FaceF)
            U(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="R":
            R(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="R'":
            RR(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="R²":
            R(FaceF)
            R(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="L":
            L(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="L'":
            LL(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="L²":
            L(FaceF)
            L(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="D":
            D(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="D'":
            DD(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="D²":
            D(FaceF)
            D(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="F":
            F(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="F'":
            FF(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="F²":
            F(FaceF)
            F(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="B":
            B(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="B'":
            BB(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="B²":
            B(FaceF)
            B(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="M":
            M(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="M'":
            MM(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="M²":
            M(FaceF)
            M(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="E":
            E(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="E'":
            EE(FaceF)
            afficherMélange(long,haut,scramble,f)
        elif scramble[i]=="E²":
            E(FaceF)
            E(FaceF)
            afficherMélange(long,haut,scramble,f)
    return scramble


def RANDOM(long,haut,longueurScramble,f,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL):
    fichier="algorithmes_%s.txt" %longueurScramble
    with open(fichier, "w") as o:
        o.write("")
    vérification=True
    essaies=0
    while essaies<10:
        croix_droite_nombre=0
        croix_nombre=0
        essaies=essaies+1
        croix_faites=False
        croix_droite_faites=False
        draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
        couleurFace(long,haut,FaceF,f)
        reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
        compte=0
        scrambleMoovs = ["U","U'","U²","R","R'","R²","L","L'","L²","D","D'","D²","F","F'","F²","B","B'","B²","M","M'","M²","E","E'","E²"]
        longueur=0
        scramble=[]
        for i in range (longueurScramble):
            scramble.append(scrambleMoovs[alea_int(0,(len(scrambleMoovs))-1)])
            scrambleMoovs = ["U","U'","U²","R","R'","R²","L","L'","L²","D","D'","D²","F","F'","F²","B","B'","B²","M","M'","M²","E","E'","E²"]
            if scramble[i]=="U":
                scrambleMoovs.remove("U")
                scrambleMoovs.remove("U'")
                scrambleMoovs.remove("U²")
                scrambleMoovs.remove("E")
                scrambleMoovs.remove("D'")
                longueur=longueur+1
            elif scramble[i]=="U'":
                scrambleMoovs.remove("U")
                scrambleMoovs.remove("U'")
                scrambleMoovs.remove("U²")
                scrambleMoovs.remove("E'")
                scrambleMoovs.remove("D")
                longueur=longueur+1
            elif scramble[i]=="U²":
                scrambleMoovs.remove("U")
                scrambleMoovs.remove("U'")
                scrambleMoovs.remove("U²")
                scrambleMoovs.remove("E²")
                scrambleMoovs.remove("D²")
                longueur=longueur+2
            elif scramble[i]=="R":
                scrambleMoovs.remove("R")
                scrambleMoovs.remove("R'")
                scrambleMoovs.remove("R²")
                scrambleMoovs.remove("E²")
                scrambleMoovs.remove("D²")
                longueur=longueur+1
            elif scramble[i]=="R'":
                scrambleMoovs.remove("R")
                scrambleMoovs.remove("R'")
                scrambleMoovs.remove("R²")
                longueur=longueur+1

            elif scramble[i]=="R²":
                scrambleMoovs.remove("R")
                scrambleMoovs.remove("R'")
                scrambleMoovs.remove("R²")
                longueur=longueur+2

            elif scramble[i]=="L":
                scrambleMoovs.remove("L")
                scrambleMoovs.remove("L'")
                scrambleMoovs.remove("L²")
                longueur=longueur+1

            elif scramble[i]=="L'":
                scrambleMoovs.remove("L")
                scrambleMoovs.remove("L'")
                scrambleMoovs.remove("L²")
                longueur=longueur+1

            elif scramble[i]=="L²":
                scrambleMoovs.remove("L")
                scrambleMoovs.remove("L'")
                scrambleMoovs.remove("L²")
                longueur=longueur+2

            elif scramble[i]=="D":
                scrambleMoovs.remove("D")
                scrambleMoovs.remove("D'")
                scrambleMoovs.remove("D²")
                longueur=longueur+1

            elif scramble[i]=="D'":
                scrambleMoovs.remove("D")
                scrambleMoovs.remove("D'")
                scrambleMoovs.remove("D²")
                longueur=longueur+1

            elif scramble[i]=="D²":
                scrambleMoovs.remove("D")
                scrambleMoovs.remove("D'")
                scrambleMoovs.remove("D²")
                longueur=longueur+2

            elif scramble[i]=="F":
                scrambleMoovs.remove("F")
                scrambleMoovs.remove("F'")
                scrambleMoovs.remove("F²")
                longueur=longueur+1

            elif scramble[i]=="F'":
                scrambleMoovs.remove("F")
                scrambleMoovs.remove("F'")
                scrambleMoovs.remove("F²")
                longueur=longueur+1

            elif scramble[i]=="F²":
                scrambleMoovs.remove("F")
                scrambleMoovs.remove("F'")
                scrambleMoovs.remove("F²")
                longueur=longueur+2

            elif scramble[i]=="B":
                scrambleMoovs.remove("B")
                scrambleMoovs.remove("B'")
                scrambleMoovs.remove("B²")
                longueur=longueur+1

            elif scramble[i]=="B'":
                scrambleMoovs.remove("B")
                scrambleMoovs.remove("B'")
                scrambleMoovs.remove("B²")
                longueur=longueur+1

            elif scramble[i]=="B²":
                scrambleMoovs.remove("B")
                scrambleMoovs.remove("B'")
                scrambleMoovs.remove("B²")
                longueur=longueur+2

            elif scramble[i]=="M":
                scrambleMoovs.remove("M")
                scrambleMoovs.remove("M'")
                scrambleMoovs.remove("M²")
                longueur=longueur+1
            elif scramble[i]=="M'":
                scrambleMoovs.remove("M")
                scrambleMoovs.remove("M'")
                scrambleMoovs.remove("M²")
                longueur=longueur+1
            elif scramble[i]=="M²":
                scrambleMoovs.remove("M")
                scrambleMoovs.remove("M'")
                scrambleMoovs.remove("M²")
                longueur=longueur+2
            elif scramble[i]=="E":
                scrambleMoovs.remove("E")
                scrambleMoovs.remove("E'")
                scrambleMoovs.remove("E²")
                longueur=longueur+1
            elif scramble[i]=="E'":
                scrambleMoovs.remove("E")
                scrambleMoovs.remove("E'")
                scrambleMoovs.remove("E²")
                longueur=longueur+1
            elif scramble[i]=="E²":
                scrambleMoovs.remove("E")
                scrambleMoovs.remove("E'")
                scrambleMoovs.remove("E²")
                longueur=longueur+2
        nombreDeCoup=0
        while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<longueur:
            draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
            if scramble[compte%longueurScramble]=="U":
                U(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="U'":
                UU(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="U²":
                U(FaceF)
                nombreDeCoup=nombreDeCoup+1
                U(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="R":
                R(FaceF)
                compte=compte+1
            elif scramble[compte%longueurScramble]=="R'":
                RR(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="R²":
                R(FaceF)
                nombreDeCoup=nombreDeCoup+1
                R(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="L":
                L(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="L'":
                LL(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="L²":
                L(FaceF)
                nombreDeCoup=nombreDeCoup+1
                L(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="D":
                D(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="D'":
                DD(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="D²":
                D(FaceF)
                nombreDeCoup=nombreDeCoup+1
                D(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="F":
                F(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="F'":
                FF(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="F²":
                F(FaceF)
                nombreDeCoup=nombreDeCoup+1
                F(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="B":
                B(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="B'":
                BB(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="B²":
                B(FaceF)
                nombreDeCoup=nombreDeCoup+1
                B(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="M":
                M(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="M'":
                MM(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="M²":
                M(FaceF)
                nombreDeCoup=nombreDeCoup+1
                M(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="E":
                E(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="E'":
                EE(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            elif scramble[compte%longueurScramble]=="E²":
                E(FaceF)
                nombreDeCoup=nombreDeCoup+1
                E(FaceF)
                compte=compte+1
                nombreDeCoup=nombreDeCoup+1
            if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False and nombreDeCoup%longueur==0:
                print("La croix droite a été réalisée en :",nombreDeCoup,"coups.")
                croix_droite_nombre=nombreDeCoup
                croix_droite_faites=True
            if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False and nombreDeCoup%longueur==0:
                print("La croix a été réalisée en :",nombreDeCoup,"coups.")
                croix_nombre=nombreDeCoup
                croix_faites=True
        if (not croix_droite_faites) and croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL):
            croix_droite_nombre=nombreDeCoup
            croix_droite_faites=True
        if (not croix_faites) and croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL):
            croix_nombre=nombreDeCoup
            croix_faites=True
        cerclePosition=2
        théorème=croix_droite_nombre*croix_nombre//pgcd(croix_droite_nombre,croix_nombre)
        print("Le théorème dit :",croix_droite_nombre,"x",croix_nombre,"/PGCD(",croix_droite_nombre,",",croix_nombre,")=",théorème,".")
        print("Le cube a été réalisé en :",nombreDeCoup,"coups, avec la combinaison :",scramble,".")
        print("Essaie numéro :",essaies)
        if théorème==nombreDeCoup:
            vérification=True
            print("Votre théorème marche.")
        else :
            vérification=False
            print("Votre théorème ne marche pas.")
        with open(fichier, "a") as o:
            o.write("Essai numéro : %s" %essaies + "\n")
            o.write("Algorithme :" + str(scramble) + "\n")
            o.write("La croix droite a été réalisée en : "+str(croix_droite_nombre)+" coups."+"\n")
            o.write("La croix a été réalisée en : "+str(croix_nombre)+" coups."+"\n")
            o.write("Le théorème dit : "+str(croix_droite_nombre)+" x "+str(croix_nombre)+" / PGCD("+str(croix_droite_nombre)+", "+str(croix_nombre)+") = "+str(théorème)+"."+"\n")
            o.write("Le cube a été réalisé en %s coups." %nombreDeCoup +"\n")
            if théorème==nombreDeCoup:
                o.write("Le théorème fonctionne !"+"\n"+"\n")
            else :
                o.write("Le théorème ne fonctionne pas. <-----------------------------------------------------------------------------------------------------------"+"\n"+"\n")


affichage(long,haut,f)
dessinerCercle(cerclePosition)
couleurPatron(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
couleurFace(long,haut,FaceF,f)
afficherMélange(long,haut,scramble,f)
continueLoop = True
while (continueLoop):
#Intéraction avec le patron :
    affiche_all()
    e = None
    e = wait_click_or_key([pygame.K_u, pygame.K_r, pygame.K_l, pygame.K_d, pygame.K_f, pygame.K_b, pygame.K_m, pygame.K_e, pygame.K_SPACE])

    if type(e) == tuple:
        x, y = e
        if x>0.21875*long and x<0.2890625*long and y>0.1111*haut and y<0.23611*haut and cerclePosition!=1 :
            cerclePosition=1
        elif x>0.21875*long and x<0.2890625*long and y>0.29167*haut and y<0.416667*haut and cerclePosition!=2 :
            cerclePosition=2
        elif x>0.21875*long and x<0.2890625*long and y>0.4722*haut and y<0.59722*haut and cerclePosition!=3 :
            cerclePosition=3
        elif x>0.21875*long and x<0.2890625*long and y>0.652778*haut and y<0.777778*haut and cerclePosition!=4 :
            cerclePosition=4
        elif x>0.21875*long-0.1015625*long and x<0.2890625*long-0.1015625*long and y>0.29167*haut and y<0.416667*haut and cerclePosition!=5 :
            cerclePosition=5
        elif x>0.21875*long+0.1015625*long and x<0.2890625*long+0.1015625*long and y>0.29167*haut and y<0.416667*haut and cerclePosition!=6 :
            cerclePosition=6
    #Interactionn avec les commandes :
        if y>haut-0.1111*haut :
            if x<0.0625*long :
                ecrire("U",(0.009375*long,0.89444*haut),0.05625*long,gris,f)
                attendre(200)
                ecrire("U",(0.009375*long,0.89444*haut),0.05625*long,blanc,f)
                if cerclePosition==1 :
                    U(FaceU)
                elif cerclePosition==2 :
                    U(FaceF)
                elif cerclePosition==3 :
                    U(FaceD)
                elif cerclePosition==4 :
                    U(FaceB)
                elif cerclePosition==5 :
                    U(FaceL)
                elif cerclePosition==6 :
                    U(FaceR)
            elif x<0.0625*long*2 and x>0.0625*long*1:
                ecrire("U'",(0.009375*long+(0.0625*long*1),0.89444*haut),0.05625*long,gris,f)
                attendre(200)
                ecrire("U'",(0.009375*long+(0.0625*long*1),0.89444*haut),0.05625*long,blanc,f)
                if cerclePosition==1 :
                    UU(FaceU)
                elif cerclePosition==2 :
                    UU(FaceF)
                elif cerclePosition==3 :
                    UU(FaceD)
                elif cerclePosition==4 :
                    UU(FaceB)
                elif cerclePosition==5 :
                    UU(FaceL)
                elif cerclePosition==6 :
                    UU(FaceR)
            elif x<0.0625*long*3 and x>0.0625*long*2:
                ecrire("R",(0.009375*long+(0.0625*long*2),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("R",(0.009375*long+(0.0625*long*2),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    R(FaceU)
                elif cerclePosition==2 :
                    R(FaceF)
                elif cerclePosition==3 :
                    R(FaceD)
                elif cerclePosition==4 :
                    R(FaceB)
                elif cerclePosition==5 :
                    R(FaceL)
                elif cerclePosition==6 :
                    R(FaceR)
            elif x<0.0625*long*4 and x>0.0625*long*3:
                ecrire("R'",(0.009375*long+(0.0625*long*3),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("R'",(0.009375*long+(0.0625*long*3),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    RR(FaceU)
                elif cerclePosition==2 :
                    RR(FaceF)
                elif cerclePosition==3 :
                    RR(FaceD)
                elif cerclePosition==4 :
                    RR(FaceB)
                elif cerclePosition==5 :
                    RR(FaceL)
                elif cerclePosition==6 :
                    RR(FaceR)
            elif x<0.0625*long*5 and x>0.0625*long*4:
                ecrire("L",(0.009375*long+(0.0625*long*4),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("L",(0.009375*long+(0.0625*long*4),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    L(FaceU)
                elif cerclePosition==2 :
                    L(FaceF)
                elif cerclePosition==3 :
                    L(FaceD)
                elif cerclePosition==4 :
                    L(FaceB)
                elif cerclePosition==5 :
                    L(FaceL)
                elif cerclePosition==6 :
                    L(FaceR)
            elif x<0.0625*long*6 and x>0.0625*long*5:
                ecrire("L'",(0.009375*long+(0.0625*long*5),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("L'",(0.009375*long+(0.0625*long*5),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    LL(FaceU)
                elif cerclePosition==2 :
                    LL(FaceF)
                elif cerclePosition==3 :
                    LL(FaceD)
                elif cerclePosition==4 :
                    LL(FaceB)
                elif cerclePosition==5 :
                    LL(FaceL)
                elif cerclePosition==6 :
                    LL(FaceR)
            elif x<0.0625*long*7 and x>0.0625*long*6:
                ecrire("D",(0.009375*long+(0.0625*long*6),0.9*haut),0.05625*long,gris,f)
                attendre(200)
                ecrire("D",(0.009375*long+(0.0625*long*6),0.9*haut),0.05625*long,blanc,f)
                if cerclePosition==1 :
                    D(FaceU)
                elif cerclePosition==2 :
                    D(FaceF)
                elif cerclePosition==3 :
                    D(FaceD)
                elif cerclePosition==4 :
                    D(FaceB)
                elif cerclePosition==5 :
                    D(FaceL)
                elif cerclePosition==6 :
                    D(FaceR)
            elif x<0.0625*long*8 and x>0.0625*long*7:
                ecrire("D'",(0.009375*long+(0.0625*long*7),0.9*haut),0.05625*long,gris,f)
                attendre(200)
                ecrire("D'",(0.009375*long+(0.0625*long*7),0.9*haut),0.05625*long,blanc,f)
                if cerclePosition==1 :
                    DD(FaceU)
                elif cerclePosition==2 :
                    DD(FaceF)
                elif cerclePosition==3 :
                    DD(FaceD)
                elif cerclePosition==4 :
                    DD(FaceB)
                elif cerclePosition==5 :
                    DD(FaceL)
                elif cerclePosition==6 :
                    DD(FaceR)
            elif x<0.0625*long*9 and x>0.0625*long*8:
                ecrire("F",(0.009375*long+(0.0625*long*8),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("F",(0.009375*long+(0.0625*long*8),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    F(FaceU)
                elif cerclePosition==2 :
                    F(FaceF)
                elif cerclePosition==3 :
                    F(FaceD)
                elif cerclePosition==4 :
                    F(FaceB)
                elif cerclePosition==5 :
                    F(FaceL)
                elif cerclePosition==6 :
                    F(FaceR)
            elif x<0.0625*long*10 and x>0.0625*long*9:
                ecrire("F'",(0.009375*long+(0.0625*long*9),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("F'",(0.009375*long+(0.0625*long*9),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    FF(FaceU)
                elif cerclePosition==2 :
                    FF(FaceF)
                elif cerclePosition==3 :
                    FF(FaceD)
                elif cerclePosition==4 :
                    FF(FaceB)
                elif cerclePosition==5 :
                    FF(FaceL)
                elif cerclePosition==6 :
                    FF(FaceR)
            elif x<0.0625*long*11 and x>0.0625*long*10:
                ecrire("B",(0.009375*long+(0.0625*long*10),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("B",(0.009375*long+(0.0625*long*10),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    B(FaceU)
                elif cerclePosition==2 :
                    B(FaceF)
                elif cerclePosition==3 :
                    B(FaceD)
                elif cerclePosition==4 :
                    B(FaceB)
                elif cerclePosition==5 :
                    B(FaceL)
                elif cerclePosition==6 :
                    B(FaceR)
            elif x<0.0625*long*12 and x>0.0625*long*11:
                ecrire("B'",(0.009375*long+(0.0625*long*11),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("B'",(0.009375*long+(0.0625*long*11),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    BB(FaceU)
                elif cerclePosition==2 :
                    BB(FaceF)
                elif cerclePosition==3 :
                    BB(FaceD)
                elif cerclePosition==4 :
                    BB(FaceB)
                elif cerclePosition==5 :
                    BB(FaceL)
                elif cerclePosition==6 :
                    BB(FaceR)
            elif x<0.0625*long*13 and x>0.0625*long*12:
                ecrire("M",(0.007595*long+(0.0625*long*12),0.90555*haut),0.05125*long,gris,f)
                attendre(200)
                ecrire("M",(0.007595*long+(0.0625*long*12),0.90555*haut),0.05125*long,blanc,f)
                if cerclePosition==1 :
                    M(FaceU)
                elif cerclePosition==2 :
                    M(FaceF)
                elif cerclePosition==3 :
                    M(FaceD)
                elif cerclePosition==4 :
                    M(FaceB)
                elif cerclePosition==5 :
                    M(FaceL)
                elif cerclePosition==6 :
                    M(FaceR)
            elif x<0.0625*long*14 and x>0.0625*long*13:
                ecrire("M'",(0.007595*long+(0.0625*long*13),0.90555*haut),0.05125*long,gris,f)
                attendre(200)
                ecrire("M'",(0.007595*long+(0.0625*long*13),0.90555*haut),0.05125*long,blanc,f)
                if cerclePosition==1 :
                    MM(FaceU)
                elif cerclePosition==2 :
                    MM(FaceF)
                elif cerclePosition==3 :
                    MM(FaceD)
                elif cerclePosition==4 :
                    MM(FaceB)
                elif cerclePosition==5 :
                    MM(FaceL)
                elif cerclePosition==6 :
                    MM(FaceR)
            elif x<0.0625*long*15 and x>0.0625*long*14:
                ecrire("E",(0.009375*long+(0.0625*long*14),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("E",(0.009375*long+(0.0625*long*14),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    E(FaceU)
                elif cerclePosition==2 :
                    E(FaceF)
                elif cerclePosition==3 :
                    E(FaceD)
                elif cerclePosition==4 :
                    E(FaceB)
                elif cerclePosition==5 :
                    E(FaceL)
                elif cerclePosition==6 :
                    E(FaceR)
            elif x<0.0625*long*16 and x>0.0625*long*15:
                ecrire("E'",(0.009375*long+(0.0625*long*15),0.88888*haut),0.0625*long,gris,f)
                attendre(200)
                ecrire("E'",(0.009375*long+(0.0625*long*15),0.88888*haut),0.0625*long,blanc,f)
                if cerclePosition==1 :
                    EE(FaceU)
                elif cerclePosition==2 :
                    EE(FaceF)
                elif cerclePosition==3 :
                    EE(FaceD)
                elif cerclePosition==4 :
                    EE(FaceB)
                elif cerclePosition==5 :
                    EE(FaceL)
                elif cerclePosition==6 :
                    EE(FaceR)
        #Echapper la fenetre
        elif x>long-0.0625*long and y<0.111111*haut :
            continueLoop = False
        #Reset le cube
        elif x>long/2 and x<long/2+0.0625*long and y<0.11111*haut :
            reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
            scramble=[]
        #Scramble le cube
        elif x>long/2-0.0625*long and x<long/2 and y<0.111111*haut:
            cerclePosition=2
            scramble=scrambleCube(long,haut,f)
            afficherMélange(long,haut,scramble,f)
        #Listes d'algorithmes
        elif x<0.0625*long and y>0.77777*haut and y<0.8888*haut:
            draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
            listes(long,haut,f)
            x,y=wait_clic()
            if x<0.1*long and y<0.055555*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                scramble=[]
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    R(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,96,f)
                    U(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,96,f)
                    R(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,96,f)
                    E(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,96,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.0625*long and y>0.05555*haut and y<0.11111*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    UU(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,126,f)
                    R(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,126,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.09*long and y>0.11111*haut and y<0.16666*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<4:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    U(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,1260,f)
                    L(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,1260,f)
                    D(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,1260,f)
                    R(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,1260,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.1*long and y>0.15555*haut and y<0.222222*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                couleurFace(long,haut,FaceR,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<4:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    U(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,24,f)
                    R(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,24,f)
                    UU(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,24,f)
                    RR(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,24,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                cerclePosition=2
                print("Le cube a été réalisé en :",compte,"coups.")
            elif x<0.060*long and y>0.2222222*haut and y<0.277777*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    U(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,252,f)
                    E(FaceF)
                    barre_progression(long,haut,compte+1,252,f)
                    L(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,252,f)
                    MM(FaceF)
                    barre_progression(long,haut,compte+1,252,f)
                    D(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,252,f)
                    EE(FaceF)
                    barre_progression(long,haut,compte+1,252,f)
                    R(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,252,f)
                    M(FaceF)
                    barre_progression(long,haut,compte+1,252,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.066*long and y>0.27777*haut and y<0.333333*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    U(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,24,f)
                    U(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,24,f)
                    R(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,24,f)
                    R(FaceF)
                    compte=compte+1
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.1*long and y>0.333333*haut and y<0.3888888*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    L(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,126,f)
                    L(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,126,f)
                    B(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,126,f)
                    L(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,126,f)
                    L(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,126,f)
                    F(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,126,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.15*long and y>0.388888*haut and y<0.4444444*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    for i in range(3):
                        U(FaceF)
                        compte=compte+1
                        barre_progression(long,haut,compte+1,468,f)
                        R(FaceF)
                        compte=compte+1
                        barre_progression(long,haut,compte+1,468,f)
                        UU(FaceF)
                        compte=compte+1
                        barre_progression(long,haut,compte+1,468,f)
                        RR(FaceF)
                        compte=compte+1
                        barre_progression(long,haut,compte+1,468,f)
                    F(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,468,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.061*long and y>0.44444*haut and y<0.49999*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    M(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,16,f)
                    U(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,16,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.05*long and y>0.49999*haut and y<0.55555*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    M(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,72,f)
                    U(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,72,f)
                    E(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,72,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.04*long and y>0.555555*haut and y<0.611111*haut:
                croix_faites=False
                croix_droite_faites=False
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)
                compte=0
                draw_fill_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),noir,f)
                while fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==False or compte<2:
                    draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
                    UU(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,1008,f)
                    EE(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,1008,f)
                    R(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,1008,f)
                    M(FaceF)
                    compte=compte+1
                    barre_progression(long,haut,compte+1,1008,f)
                    if croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_droite_faites==False:
                        print("La croix droite a été réalisée en :",compte,"coups.")
                        croix_droite_faites=True
                    if croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)==True and croix_faites==False:
                        print("La croix a été réalisée en :",compte,"coups.")
                        croix_faites=True
                print("Le cube a été réalisé en :",compte,"coups.")
                cerclePosition=2
            elif x<0.12*long and y>0.61111*haut and y<0.666666*haut:
                RANDOM(long,haut,2,f,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)
            elif x<0.12*long and y>0.66666*haut and y<0.722222*haut:
                RANDOM(long,haut,3,f,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)
            elif x<0.12*long and y>0.722222*haut and y<0.777777*haut:
                RANDOM(long,haut,4,f,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)
            elif x<0.12*long and y>0.77777*haut and y<0.833333*haut:
                RANDOM(long,haut,5,f,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)
            elif x<0.12*long and y>0.833333*haut and y<0.888888*haut:
                RANDOM(long,haut,10,f,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL)

            else:
                cerclePosition=2
                draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
    elif type(e)==str:
        if e ==" ":
            attendre(500)
            draw_fill_rectangle((0,0),(long,0.8888*haut),noir,f)
            draw_rectangle((long-0.0625*long,0.111111*haut),(long,0),blanc,f)
            ecrire("ESC",(long-0.0625*long,0),0.03125*long,blanc,f)
            mn = 0
            nd = 0
            ecrire("0:00",(long//3,haut//3),(long+haut)//8,blanc,f)
            e = wait_key()
            e = None
            while e != " " and mn < 60:
                temps = str(mn)+":"+str(round(nd,4))
                draw_fill_rectangle((0,0.0625*haut),(long,0.8888*haut),noir,f)
                draw_rectangle((long-0.0625*long,0.111111*haut),(long,0),blanc,f)
                ecrire("ESC",(long-0.0625*long,0),0.03125*long,blanc,f)
                ecrire('Appuyez sur "Espace" pour arrêter du chronomètre',(0.03125*long,0),0.015625*long,blanc,f )
                ecrire('Appuyez sur "Echap" pour sortir du chronomètre',(0.03125*long,0.03125*haut),0.015625*long,blanc,f )
                ecrire(temps,(long//3,haut//3),(long+haut)//8,blanc,f)
                nd = round(nd + 0.1,4)
                e = wait_key()
                if e=="\x1B":
                    break
                attendre(100)
                e = wait_key()
                if e=="\x1B":
                    break
                if nd == 60:
                    mn = round(mn+1,4)
                    nd = 0.00
            x,y=0,haut
            while e != "\x1B" and (x<long-0.0625*long or y>0.111111*haut):
                e=wait_click_or_key([pygame.K_SPACE])
                if type(e)==tuple:
                    x,y=e
                    e=""
                else :
                    x,y=0,haut
            draw_fill_rectangle((0,0),(long,haut-haut/9),noir,f)



        elif e == "u":
            if cerclePosition==1 :
                U(FaceU)
            elif cerclePosition==2 :
                U(FaceF)
            elif cerclePosition==3 :
                U(FaceD)
            elif cerclePosition==4 :
                U(FaceB)
            elif cerclePosition==5 :
                U(FaceL)
            elif cerclePosition==6 :
                U(FaceR)
        elif e == "U":
            if cerclePosition==1 :
                UU(FaceU)
            elif cerclePosition==2 :
                UU(FaceF)
            elif cerclePosition==3 :
                UU(FaceD)
            elif cerclePosition==4 :
                UU(FaceB)
            elif cerclePosition==5 :
                UU(FaceL)
            elif cerclePosition==6 :
                UU(FaceR)
        elif e == "r":
            if cerclePosition==1 :
                R(FaceU)
            elif cerclePosition==2 :
                R(FaceF)
            elif cerclePosition==3 :
                R(FaceD)
            elif cerclePosition==4 :
                R(FaceB)
            elif cerclePosition==5 :
                R(FaceL)
            elif cerclePosition==6 :
                R(FaceR)
        elif e == "R":
            if cerclePosition==1 :
                RR(FaceU)
            elif cerclePosition==2 :
                RR(FaceF)
            elif cerclePosition==3 :
                RR(FaceD)
            elif cerclePosition==4 :
                RR(FaceB)
            elif cerclePosition==5 :
                RR(FaceL)
            elif cerclePosition==6 :
                RR(FaceR)
        elif e == "l":
            if cerclePosition==1 :
                L(FaceU)
            elif cerclePosition==2 :
                L(FaceF)
            elif cerclePosition==3 :
                L(FaceD)
            elif cerclePosition==4 :
                L(FaceB)
            elif cerclePosition==5 :
                L(FaceL)
            elif cerclePosition==6 :
                L(FaceR)
        elif e == "L":
            if cerclePosition==1 :
                LL(FaceU)
            elif cerclePosition==2 :
                LL(FaceF)
            elif cerclePosition==3 :
                LL(FaceD)
            elif cerclePosition==4 :
                LL(FaceB)
            elif cerclePosition==5 :
                LL(FaceL)
            elif cerclePosition==6 :
                LL(FaceR)
        elif e == "d":
            if cerclePosition==1 :
                D(FaceU)
            elif cerclePosition==2 :
                D(FaceF)
            elif cerclePosition==3 :
                D(FaceD)
            elif cerclePosition==4 :
                D(FaceB)
            elif cerclePosition==5 :
                D(FaceL)
            elif cerclePosition==6 :
                D(FaceR)
        elif e == "D":
            if cerclePosition==1 :
                DD(FaceU)
            elif cerclePosition==2 :
                DD(FaceF)
            elif cerclePosition==3 :
                DD(FaceD)
            elif cerclePosition==4 :
                DD(FaceB)
            elif cerclePosition==5 :
                DD(FaceL)
            elif cerclePosition==6 :
                DD(FaceR)
        elif e == "f":
            if cerclePosition==1 :
                F(FaceU)
            elif cerclePosition==2 :
                F(FaceF)
            elif cerclePosition==3 :
                F(FaceD)
            elif cerclePosition==4 :
                F(FaceB)
            elif cerclePosition==5 :
                F(FaceL)
            elif cerclePosition==6 :
                F(FaceR)
        elif e == "F":
            if cerclePosition==1 :
                FF(FaceU)
            elif cerclePosition==2 :
                FF(FaceF)
            elif cerclePosition==3 :
                FF(FaceD)
            elif cerclePosition==4 :
                FF(FaceB)
            elif cerclePosition==5 :
                FF(FaceL)
            elif cerclePosition==6 :
                FF(FaceR)
        elif e == "b":
            if cerclePosition==1 :
                B(FaceU)
            elif cerclePosition==2 :
                B(FaceF)
            elif cerclePosition==3 :
                B(FaceD)
            elif cerclePosition==4 :
                B(FaceB)
            elif cerclePosition==5 :
                B(FaceL)
            elif cerclePosition==6 :
                B(FaceR)
        elif e == "B":
            if cerclePosition==1 :
                BB(FaceU)
            elif cerclePosition==2 :
                BB(FaceF)
            elif cerclePosition==3 :
                BB(FaceD)
            elif cerclePosition==4 :
                BB(FaceB)
            elif cerclePosition==5 :
                BB(FaceL)
            elif cerclePosition==6 :
                BB(FaceR)
        elif e == "m":
            if cerclePosition==1 :
                M(FaceU)
            elif cerclePosition==2 :
                M(FaceF)
            elif cerclePosition==3 :
                M(FaceD)
            elif cerclePosition==4 :
                M(FaceB)
            elif cerclePosition==5 :
                M(FaceL)
            elif cerclePosition==6 :
                M(FaceR)
        elif e == "M":
            if cerclePosition==1 :
                MM(FaceU)
            elif cerclePosition==2 :
                MM(FaceF)
            elif cerclePosition==3 :
                MM(FaceD)
            elif cerclePosition==4 :
                MM(FaceB)
            elif cerclePosition==5 :
                MM(FaceL)
            elif cerclePosition==6 :
                MM(FaceR)
        elif e == "e":
            if cerclePosition==1 :
                E(FaceU)
            elif cerclePosition==2 :
                E(FaceF)
            elif cerclePosition==3 :
                E(FaceD)
            elif cerclePosition==4 :
                E(FaceB)
            elif cerclePosition==5 :
                E(FaceL)
            elif cerclePosition==6 :
                E(FaceR)
        elif e == "E":
            if cerclePosition==1 :
                EE(FaceU)
            elif cerclePosition==2 :
                EE(FaceF)
            elif cerclePosition==3 :
                EE(FaceD)
            elif cerclePosition==4 :
                EE(FaceB)
            elif cerclePosition==5 :
                EE(FaceL)
            elif cerclePosition==6 :
                EE(FaceR)
        elif e == "\x1B":
            continueLoop = False
    else :
        continue

    affichage(long,haut,f)
    afficherMélange(long,haut,scramble,f)
    dessinerCercle(cerclePosition)
    if cerclePosition==1 :
        couleurFace(long,haut,FaceU,f)
    elif cerclePosition==2 :
        couleurFace(long,haut,FaceF,f)
    elif cerclePosition==3 :
        couleurFace(long,haut,FaceD,f)
    elif cerclePosition==4 :
        couleurFace(long,haut,FaceB,f)
    elif cerclePosition==5 :
        couleurFace(long,haut,FaceL,f)
    elif cerclePosition==6 :
        couleurFace(long,haut,FaceR,f)
    couleurPatron(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f)


quit_graphics()
