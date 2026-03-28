# Créé par Riwan, le 17/01/2026 en Python 3.7
from graphics import *

def affichage(long,haut,f):
    """
    redessine les contours blancs de tous les trucs

    long: longueur de la fenêtre graphique
    haut: hauteur de la fenêtre
    f: nom de la fenêtre
    """
    #Séparation de l'écran en deux parties égales
    draw_line((long/2,0),(long/2,haut/1.125),blanc,f)

    #Création du cadre de la face visible du cube sur le droit gauche de l'écran
    draw_rectangle((long//2+long//16,haut//1.125//8),(long-long//16,haut//1.125-haut//1.125//8),blanc,f)
    draw_line((0.6875*long,haut//1.125//8),(0.6875*long,haut//1.125-haut//1.125//8),blanc,f)
    draw_line((0.8125*long,haut//1.125//8),(0.8125*long,haut//1.125-haut//1.125//8),blanc,f)
    draw_line((long//2+long//16,0.3333*haut),(long-long//16,0.3333*haut),blanc,f)
    draw_line((long//2+long//16,0.5555*haut),(long-long//16,0.5555*haut),blanc,f)


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



def affichercube(long,haut,f) :
    draw_rectangle((long//2+long//16,haut//1.125//8),(long-long//16,haut//1.125-haut//1.125//8),blanc,f)
    draw_line((0.6875*long,haut//1.125//8),(0.6875*long,haut//1.125-haut//1.125//8),blanc,f)
    draw_line((0.8125*long,haut//1.125//8),(0.8125*long,haut//1.125-haut//1.125//8),blanc,f)
    draw_line((long//2+long//16,0.3333*haut),(long-long//16,0.3333*haut),blanc,f)
    draw_line((long//2+long//16,0.5555*haut),(long-long//16,0.5555*haut),blanc,f)


def afficherpatron(long,haut,f):
    draw_rectangle((0.21875*long,0.1111*haut),(0.2890625*long,0.23611*haut),blanc,f)
    draw_line((0.2421875*long,0.1111*haut),(0.2421875*long,0.23333*haut),blanc,f)
    draw_line((0.2421875*long+0.0234375*long,0.1111*haut),(0.2421875*long+0.0234375*long,0.23333*haut),blanc,f)
    draw_line((0.21875*long,0.1111*haut+0.041666*haut),(0.2880625*long,0.1111*haut+0.041666*haut),blanc,f)
    draw_line((0.21875*long,0.1111*haut+(2*0.041666*haut)),(0.2880625*long,0.1111*haut+(0.041666*haut*2)),blanc,f)


    draw_rectangle((0.21875*long,0.29167*haut),(0.2890625*long,0.41666*haut),blanc,f)
    draw_line((0.2421875*long,0.29167*haut),(0.2421875*long,0.413*haut),blanc,f)
    draw_line((0.2421875*long+0.0234375*long,0.29167*haut),(0.2421875*long+0.0234375*long,0.413*haut),blanc,f)
    draw_line((0.21875*long,0.29167*haut+0.041666*haut),(0.2880625*long,0.29167*haut+0.041666*haut),blanc,f)
    draw_line((0.21875*long,0.29167*haut+(2*0.041666*haut)),(0.2880625*long,0.29167*haut+(0.041666*haut*2)),blanc,f)

    draw_rectangle((0.21875*long,0.4722*haut),(0.2890625*long,0.59722*haut),blanc,f)
    draw_line((0.2421875*long,0.4722*haut),(0.2421875*long,0.59422*haut),blanc,f)
    draw_line((0.2421875*long+0.0234375*long,0.4722*haut),(0.2421875*long+0.0234375*long,0.59422*haut),blanc,f)
    draw_line((0.21875*long,0.4722*haut+0.041666*haut),(0.2880625*long,0.4722*haut+0.041666*haut),blanc,f)
    draw_line((0.21875*long,0.4722*haut+(2*0.041666*haut)),(0.2880625*long,0.4722*haut+(0.041666*haut*2)),blanc,f)

    draw_rectangle((0.21875*long,0.652778*haut),(0.2890625*long,0.777778*haut),blanc,f)
    draw_line((0.2421875*long,0.652778*haut),(0.2421875*long,0.774445*haut),blanc,f)
    draw_line((0.2421875*long+0.0234375*long,0.652778*haut),(0.2421875*long+0.0234375*long,0.774445*haut),blanc,f)
    draw_line((0.21875*long,0.652778*haut+0.041666*haut),(0.2880625*long,0.652778*haut+0.041666*haut),blanc,f)
    draw_line((0.21875*long,0.652778*haut+(2*0.041666*haut)),(0.2880625*long,0.652778*haut+(0.041666*haut*2)),blanc,f)

    draw_rectangle((0.1171875*long,0.291667*haut),(0.1875*long,0.416667*haut),blanc,f)
    draw_line((0.1171875*long+0.0234375*long,0.29167*haut),(0.1171875*long+0.0234375*long,0.415333*haut),blanc,f)
    draw_line((0.1171875*long+(2*0.0234375*long),0.29167*haut),(0.1171875*long+(0.0234375*long*2),0.415333*haut),blanc,f)
    draw_line((0.1171875*long,0.29167*haut+0.041666*haut),(0.1865*long,0.29167*haut+0.041666*haut),blanc,f)
    draw_line((0.1171875*long,0.29167*haut+(2*0.041666*haut)),(0.1865*long,0.29167*haut+(0.041666*haut*2)),blanc,f)


    draw_rectangle((0.3203125*long,0.291667*haut),(0.390625*long,0.416667*haut),blanc,f)
    draw_line((0.3203125*long+0.0234375*long,0.29167*haut),(0.3203125*long+0.0234375*long,0.415333*haut),blanc,f)
    draw_line((0.3203125*long+(2*0.0234375*long),0.29167*haut),(0.3203125*long+(2*0.0234375*long),0.415333*haut),blanc,f)
    draw_line((0.3203125*long,0.29167*haut+0.041666*haut),(0.389*long,0.29167*haut+0.041666*haut),blanc,f)
    draw_line((0.3203125*long,0.29167*haut+(2*0.041666*haut)),(0.389*long,0.29167*haut+(0.041666*haut*2)),blanc,f)


def couleurFace(long,haut,Face,f):
    draw_fill_rectangle((long//2+long//16,haut//1.125//8),(0.6875*long+1,0.3333*haut+1),Face["un"],f)
    draw_fill_rectangle((0.6875*long,0.3333*haut),(0.8125*long+1,haut//1.125//8),Face["deux"],f)
    draw_fill_rectangle((0.8125*long,haut//1.125//8),(long-long//16,0.3333*haut+1),Face["trois"],f)
    draw_fill_rectangle((0.5625*long,0.3333*haut),(0.6875*long+1,0.5556*haut+1),Face["quatre"],f)
    draw_fill_rectangle((0.6875*long,0.3333*haut),(0.8125*long+1,0.5556*haut+1),Face["cinq"],f)
    draw_fill_rectangle((0.8125*long,0.3333*haut),(0.9375*long+1,0.5556*haut+1),Face["six"],f)
    draw_fill_rectangle((0.5625*long,0.5556*haut),(0.6875*long+1,0.7778*haut+1),Face["sept"],f)
    draw_fill_rectangle((0.6875*long,0.5556*haut),(0.8125*long+1,0.7778*haut+1),Face["huit"],f)
    draw_fill_rectangle((0.8125*long,0.5556*haut),(0.9375*long+1,0.7778*haut+1),Face["neuf"],f)
    affichercube(long,haut,f)


def couleurPatron(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f):
    draw_fill_rectangle((0.21875*long,0.29167*haut),(0.2421875*long+1,0.3344*haut),FaceF["un"],f)
    draw_fill_rectangle((0.2421875*long,0.29167*haut),(0.265625*long+1,0.3344*haut),FaceF["deux"],f)
    draw_fill_rectangle((0.265625*long,0.29167*haut),(0.2890625*long,0.3344*haut),FaceF["trois"],f)
    draw_fill_rectangle((0.21875*long,0.3344*haut),(0.2421875*long+1,0.376*haut),FaceF["quatre"],f)
    draw_fill_rectangle((0.2421875*long,0.3344*haut),(0.265625*long+1,0.376*haut),FaceF["cinq"],f)
    draw_fill_rectangle((0.265625*long,0.3344*haut),(0.2890625*long,0.376*haut),FaceF["six"],f)
    draw_fill_rectangle((0.21875*long,0.376*haut),(0.2421875*long+1,0.416*haut),FaceF["sept"],f)
    draw_fill_rectangle((0.2421875*long,0.376*haut),(0.265625*long+1,0.416*haut),FaceF["huit"],f)
    draw_fill_rectangle((0.265625*long,0.376*haut),(0.2890625*long,0.416*haut),FaceF["neuf"],f)

    draw_fill_rectangle((0.21875*long,0.4723*haut),(0.2421875*long+1,0.5139*haut),FaceD["un"],f)
    draw_fill_rectangle((0.2421875*long,0.4723*haut),(0.265625*long+1,0.5139*haut),FaceD["deux"],f)
    draw_fill_rectangle((0.265625*long,0.4723*haut),(0.2890625*long,0.5139*haut),FaceD["trois"],f)
    draw_fill_rectangle((0.21875*long,0.5139*haut),(0.2421875*long+1,0.5556*haut),FaceD["quatre"],f)
    draw_fill_rectangle((0.2421875*long,0.5139*haut),(0.265625*long+1,0.5556*haut),FaceD["cinq"],f)
    draw_fill_rectangle((0.265625*long,0.5139*haut),(0.2890625*long,0.5556*haut),FaceD["six"],f)
    draw_fill_rectangle((0.21875*long,0.5556*haut),(0.2421875*long+1,0.597*haut),FaceD["sept"],f)
    draw_fill_rectangle((0.2421875*long,0.5556*haut),(0.265625*long+1,0.597*haut),FaceD["huit"],f)
    draw_fill_rectangle((0.265625*long,0.5556*haut),(0.2890625*long,0.597*haut),FaceD["neuf"],f)

    draw_fill_rectangle((0.3203125*long,0.29167*haut),(0.34375*long+1,0.34*haut),FaceR["un"],f)
    draw_fill_rectangle((0.34375*long,0.29167*haut),(0.3671875*long+1,0.34*haut),FaceR["deux"],f)
    draw_fill_rectangle((0.3671875*long,0.29167*haut),(0.390625*long,0.34*haut),FaceR["trois"],f)
    draw_fill_rectangle((0.3203125*long,0.3344*haut),(0.34375*long+1,0.38*haut),FaceR["quatre"],f)
    draw_fill_rectangle((0.34375*long,0.3344*haut),(0.3671875*long+1,0.38*haut),FaceR["cinq"],f)
    draw_fill_rectangle((0.3671875*long,0.3344*haut),(0.390625*long,0.38*haut),FaceR["six"],f)
    draw_fill_rectangle((0.3203125*long,0.376*haut),(0.34375*long+1,0.4167*haut),FaceR["sept"],f)
    draw_fill_rectangle((0.34375*long,0.376*haut),(0.3671875*long+1,0.4167*haut),FaceR["huit"],f)
    draw_fill_rectangle((0.3671875*long,0.376*haut),(0.390625*long,0.4167*haut),FaceR["neuf"],f)

    draw_fill_rectangle((0.21875*long,0.6528*haut),(0.2421875*long+1,0.7*haut),FaceB["un"],f)
    draw_fill_rectangle((0.2421875*long,0.6528*haut),(0.265625*long+1,0.7*haut),FaceB["deux"],f)
    draw_fill_rectangle((0.265625*long,0.6528*haut),(0.2890625*long,0.7*haut),FaceB["trois"],f)
    draw_fill_rectangle((0.21875*long,0.6945*haut),(0.2421875*long+1,0.74*haut),FaceB["quatre"],f)
    draw_fill_rectangle((0.2421875*long,0.6945*haut),(0.265625*long+1,0.74*haut),FaceB["cinq"],f)
    draw_fill_rectangle((0.265625*long,0.6945*haut),(0.2890625*long,0.74*haut),FaceB["six"],f)
    draw_fill_rectangle((0.21875*long,0.7362*haut),(0.2421875*long+1,0.7778*haut),FaceB["sept"],f)
    draw_fill_rectangle((0.2421875*long,0.7362*haut),(0.265625*long+1,0.7778*haut),FaceB["huit"],f)
    draw_fill_rectangle((0.265625*long,0.7362*haut),(0.2890625*long,0.7778*haut),FaceB["neuf"],f)

    draw_fill_rectangle((0.21875*long,0.1112*haut),(0.2421875*long+1,0.154*haut),FaceU["un"],f)
    draw_fill_rectangle((0.2421875*long,0.1112*haut),(0.265625*long+1,0.154*haut),FaceU["deux"],f)
    draw_fill_rectangle((0.265625*long,0.1112*haut),(0.2890625*long,0.154*haut),FaceU["trois"],f)
    draw_fill_rectangle((0.21875*long,0.1528*haut),(0.2421875*long+1,0.196*haut),FaceU["quatre"],f)
    draw_fill_rectangle((0.2421875*long,0.1528*haut),(0.265625*long+1,0.196*haut),FaceU["cinq"],f)
    draw_fill_rectangle((0.265625*long,0.1528*haut),(0.2890625*long,0.196*haut),FaceU["six"],f)
    draw_fill_rectangle((0.21875*long,0.1945*haut),(0.2421875*long+1,0.2361*haut),FaceU["sept"],f)
    draw_fill_rectangle((0.2421875*long,0.1945*haut),(0.265625*long+1,0.2361*haut),FaceU["huit"],f)
    draw_fill_rectangle((0.265625*long,0.1945*haut),(0.2890625*long,0.2361*haut),FaceU["neuf"],f)

    draw_fill_rectangle((0.1171875*long,0.29167*haut),(0.140625*long+1,0.3344*haut),FaceL["un"],f)
    draw_fill_rectangle((0.140625*long,0.29167*haut),(0.1640625*long+1,0.3344*haut),FaceL["deux"],f)
    draw_fill_rectangle((0.1640625*long,0.29167*haut),(0.1875*long,0.3344*haut),FaceL["trois"],f)
    draw_fill_rectangle((0.1171875*long,0.3344*haut),(0.140625*long+1,0.376*haut),FaceL["quatre"],f)
    draw_fill_rectangle((0.140625*long,0.3344*haut),(0.1640625*long+1,0.376*haut),FaceL["cinq"],f)
    draw_fill_rectangle((0.1640625*long,0.3344*haut),(0.1875*long,0.376*haut),FaceL["six"],f)
    draw_fill_rectangle((0.1171875*long,0.376*haut),(0.140625*long+1,0.4167*haut),FaceL["sept"],f)
    draw_fill_rectangle((0.140625*long,0.376*haut),(0.1640625*long+1,0.4167*haut),FaceL["huit"],f)
    draw_fill_rectangle((0.1640625*long,0.376*haut),(0.1875*long,0.4167*haut),FaceL["neuf"],f)
    afficherpatron(long,haut,f)

def reset(long,haut,FaceF,FaceD,FaceR,FaceB,FaceU,FaceL,f) :
    draw_fill_rectangle((0,0),(long/2-0.0625*long-1,0.111111*haut),noir,f)
    FaceF["un"]=rouge
    FaceF["deux"]=rouge
    FaceF["trois"]=rouge
    FaceF["quatre"]=rouge
    FaceF["cinq"]=rouge
    FaceF["six"]=rouge
    FaceF["sept"]=rouge
    FaceF["huit"]=rouge
    FaceF["neuf"]=rouge

    FaceU["un"]=vert
    FaceU["deux"]=vert
    FaceU["trois"]=vert
    FaceU["quatre"]=vert
    FaceU["cinq"]=vert
    FaceU["six"]=vert
    FaceU["sept"]=vert
    FaceU["huit"]=vert
    FaceU["neuf"]=vert

    FaceD["un"]=bleu
    FaceD["deux"]=bleu
    FaceD["trois"]=bleu
    FaceD["quatre"]=bleu
    FaceD["cinq"]=bleu
    FaceD["six"]=bleu
    FaceD["sept"]=bleu
    FaceD["huit"]=bleu
    FaceD["neuf"]=bleu

    FaceB["un"]=orange
    FaceB["deux"]=orange
    FaceB["trois"]=orange
    FaceB["quatre"]=orange
    FaceB["cinq"]=orange
    FaceB["six"]=orange
    FaceB["sept"]=orange
    FaceB["huit"]=orange
    FaceB["neuf"]=orange

    FaceL["un"]=jaune
    FaceL["deux"]=jaune
    FaceL["trois"]=jaune
    FaceL["quatre"]=jaune
    FaceL["cinq"]=jaune
    FaceL["six"]=jaune
    FaceL["sept"]=jaune
    FaceL["huit"]=jaune
    FaceL["neuf"]=jaune

    FaceR["un"]=blanc
    FaceR["deux"]=blanc
    FaceR["trois"]=blanc
    FaceR["quatre"]=blanc
    FaceR["cinq"]=blanc
    FaceR["six"]=blanc
    FaceR["sept"]=blanc
    FaceR["huit"]=blanc
    FaceR["neuf"]=blanc

def dessinerCercle(cerclePosition) :
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


def afficherMélange(long,haut,scramble,f):
    draw_fill_rectangle((0,0),(long/2-0.0625*long-1,0.111111*haut),noir,f)
    for i in range (len(scramble)):
        if i<10 :
            ecrire(scramble[i],(i*0.0399*long,0),0.03125*long,blanc,f)
        elif i>=10:
            ecrire(scramble[i],((i-10)*0.0399*long,0.05555*haut),0.03125*long,blanc,f)


def fin(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL):
    if FaceF["un"]==rouge and FaceF["deux"]==rouge and FaceF["trois"]==rouge and FaceF["quatre"]==rouge and FaceF["cinq"]==rouge and FaceF["six"]==rouge and FaceF["sept"]==rouge and FaceF["huit"]==rouge and FaceF["neuf"]==rouge and FaceU["un"]==vert and FaceU["deux"]==vert and FaceU["trois"]==vert and FaceU["quatre"]==vert and FaceU["cinq"]==vert and  FaceU["six"]==vert and FaceU["sept"]==vert and FaceU["huit"]==vert and FaceU["neuf"]==vert and FaceD["un"]==bleu and FaceD["deux"]==bleu and FaceD["trois"]==bleu and FaceD["quatre"]==bleu and FaceD["cinq"]==bleu and FaceD["six"]==bleu and FaceD["sept"]==bleu and FaceD["huit"]==bleu and FaceD["neuf"]==bleu and FaceB["un"]==orange and FaceB["deux"]==orange and FaceB["trois"]==orange and FaceB["quatre"]==orange and FaceB["cinq"]==orange and FaceB["six"]==orange and FaceB["sept"]==orange and FaceB["huit"]==orange and FaceB["neuf"]==orange and FaceL["un"]==jaune and FaceL["deux"]==jaune and FaceL["trois"]==jaune and FaceL["quatre"]==jaune and    FaceL["cinq"]==jaune and    FaceL["six"]==jaune and    FaceL["sept"]==jaune and    FaceL["huit"]==jaune and    FaceL["neuf"]==jaune and    FaceR["un"]==blanc and    FaceR["deux"]==blanc and    FaceR["trois"]==blanc and    FaceR["quatre"]==blanc and    FaceR["cinq"]==blanc and    FaceR["six"]==blanc and    FaceR["sept"]==blanc and    FaceR["huit"]==blanc and    FaceR["neuf"]==blanc:
        return True
    else:
        return False

#création des listes d'algorithmes
def listes(long,haut,f):
    draw_rectangle((0,0),(0.090*long,0.0555555*haut),blanc,f)
    ecrire("RURE",(0,0),0.03125*long,blanc,f)

    draw_rectangle((0,0.05555*haut),(0.0625*long,0.11111*haut),blanc,f)
    ecrire("U'R",(0,0.05555*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.11111*haut),(0.090*long,0.1666666*haut),blanc,f)
    ecrire("ULDR",(0,0.11111*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.166666*haut),(0.1*long,0.22222*haut),blanc,f)
    ecrire("URU'R'",(0,0.16666*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.2222222*haut),(0.060*long,0.277777*haut),blanc,f)
    ecrire("uldr",(0,0.2222222*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.277777*haut),(0.066*long,0.333333*haut),blanc,f)
    ecrire("U²R²",(0,0.277777*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.333333*haut),(0.1*long,0.3888888*haut),blanc,f)
    ecrire("L²BL²F",(0,0.333333*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.388888*haut),(0.15*long,0.444444*haut),blanc,f)
    ecrire("(RUR'U')³F",(0,0.38*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.44444*haut),(0.061*long,0.49999*haut),blanc,f)
    ecrire("MU",(0,0.44444*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.49999*haut),(0.05*long,0.55555*haut),blanc,f)
    ecrire("Mu",(0,0.49999*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.55555*haut),(0.04*long,0.61111*haut),blanc,f)
    ecrire("u'r",(0,0.55555*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.61111*haut),(0.12*long,0.66666*haut),blanc,f)
    ecrire("RAND 2",(0,0.61111*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.66666*haut),(0.12*long,0.72222*haut),blanc,f)
    ecrire("RAND 3",(0,0.66666*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.72222*haut),(0.12*long,0.7777*haut),blanc,f)
    ecrire("RAND 4",(0,0.72222*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.7777*haut),(0.12*long,0.833333*haut),blanc,f)
    ecrire("RAND 5",(0,0.7777*haut),0.03125*long,blanc,f)

    draw_rectangle((0,0.8333*haut),(0.135*long,0.88888*haut),blanc,f)
    ecrire("RAND 10",(0,0.8333*haut),0.03125*long,blanc,f)


def cercleReset(long,haut,f):
    draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long,(0.23611*haut-0.1111*haut)/2+0.1111*haut),(0.23611*haut-0.1111*haut)/1.4,noir,f)
    draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long,(0.416667*haut-0.29167*haut)/2+0.29167*haut),(0.416667*haut-0.29167*haut)/1.4,noir,f)
    draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long,(0.59722*haut-0.4722*haut)/2+0.4722*haut),(0.59722*haut-0.4722*haut)/1.4,noir,f)
    draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long,(0.777778*haut-0.652778*haut)/2+0.652778*haut),(0.777778*haut-0.652778*haut)/1.4,noir,f)
    draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long-0.1015625*long,(0.416667*haut-0.29167*haut)/2+0.29167*haut),(0.416667*haut-0.29167*haut)/1.4,noir,f)
    draw_circle(((0.2890625*long-0.21875*long)/2+0.21875*long+0.1015625*long,(0.416667*haut-0.29167*haut)/2+0.29167*haut),(0.416667*haut-0.29167*haut)/1.4,noir,f)



def croix_droite(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL) :
    if FaceF["deux"]==rouge and FaceF["quatre"]==rouge and FaceF["cinq"]==rouge and FaceF["six"]==rouge and FaceF["huit"]==rouge and FaceU["deux"]==vert and FaceU["quatre"]==vert and FaceU["cinq"]==vert and FaceU["six"]==vert and FaceU["huit"]==vert and FaceD["deux"]==bleu and FaceD["quatre"]==bleu and FaceD["cinq"]==bleu and FaceD["six"]==bleu and FaceD["huit"]==bleu and FaceB["deux"]==orange and FaceB["quatre"]==orange and FaceB["cinq"]==orange  and FaceB["six"]==orange and FaceB["huit"]==orange and FaceL["deux"]==jaune and FaceL["quatre"]==jaune and FaceL["cinq"]==jaune and FaceL["six"]==jaune and FaceL["huit"]==jaune and FaceR["deux"]==blanc and FaceR["quatre"]==blanc and FaceR["cinq"]==blanc and FaceR["six"]==blanc and FaceR["huit"]==blanc:
        return True
    else:
        return False

def croix(FaceF,FaceD,FaceR,FaceB,FaceU,FaceL) :
    if FaceF["un"]==rouge and FaceF["trois"]==rouge and FaceF["sept"]==rouge and FaceF["neuf"]==rouge and FaceU["un"]==vert and FaceU["trois"]==vert and FaceU["sept"]==vert and FaceU["neuf"]==vert and FaceD["un"]==bleu and FaceD["trois"]==bleu and FaceD["sept"]==bleu and FaceD["neuf"]==bleu and FaceB["un"]==orange and FaceB["trois"]==orange and FaceB["sept"]==orange and FaceB["neuf"]==orange and FaceL["un"]==jaune and FaceL["trois"]==jaune and FaceL["sept"]==jaune and    FaceL["neuf"]==jaune and    FaceR["un"]==blanc and    FaceR["trois"]==blanc and    FaceR["sept"]==blanc and    FaceR["neuf"]==blanc:
        return True
    else:
        return False


def barre_progression(long,haut,nombre,final,f):
    draw_rectangle((0.5625*long,0.80555*haut),(0.9375*long,0.861111*haut),blanc,f)
    draw_fill_rectangle((0.5625*long,0.80555*haut),(0.5625*long+(nombre*((0.375*long)/final)),0.861111*haut),rouge,f)

def pgcd(x,y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    for i in range(y//2, 0, -1):
        if x % i == 0 and y % i == 0:
            return i
