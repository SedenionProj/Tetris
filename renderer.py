import os

longueur, hauteur = os.get_terminal_size()

image = [[' ' for _ in range(longueur)] for _ in range(hauteur)]
hauteur -= 2

def placerPixel(x, y, char):
    # place un pixel sur l'écran
    x1 = round(x)
    y1 = round(y)
    if 0 <= x1 <= longueur - 1 and 0 <= y1 <= hauteur - 1:
        image[y1][x1] = char


def afficher(*info):
    # affiche l'image à l'écran
    info = "".join(info)
    info += ' ' * (longueur - len(info))
    strImage = ''
    for y in range(hauteur):
        for x in range(longueur):
            strImage += image[y][x]
    print(info + strImage, end='')


def supprimer():
    # réinitialise l'image
    for y in range(hauteur):
        for x in range(longueur):
            image[y][x] = ' '
