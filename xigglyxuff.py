#!/usr/bin/python
import random

list = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 
        'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',
        'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
        'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',
        ]

print ('Hello, pokédude. Here are the usernames you requested.\n')

for i in range(15):
    c1 = random.choice(list)
    c2 = random.choice(list)
    while c2 == c1:
        c2 = random.choice(list)
    print ('\t\t',c1.title()+'iggly'+c2+'uff')