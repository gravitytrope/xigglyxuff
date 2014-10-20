#!/usr/bin/python
import random

list = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 
        'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',
        'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
        'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',
        ]

print ('Hello, pokédude. How many usernames do you want me to generate?\n')
u1 = int(input())

for i in range(u1):
    c1 = random.choice(list)
    c2 = random.choice(list)
    while c2 == c1:
        c2 = random.choice(list)
    print ('\t\t',c1.title()+'iggly'+c2+'uff')
