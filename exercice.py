#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
  nouveau_mot=''
for c in mot:
    # TODO completer la fonction ici
    
    
    nouveau_mot= chr(ord(c))
    return nouveau_mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
