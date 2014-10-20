#!/usr/bin/python
import random
import sys

list = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 
        'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',
        'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
        'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',
        ]

print ('Hello, pokédude.')

while True:
    print ('\nHow many usernames do you want me to generate? (q to quit)\n')
    u1 = input()

    if u1 == 'q':
        sys.exit()

    u1 = int(u1)
    for i in range(u1):
        c1 = random.choice(list)
        c2 = random.choice(list)
        while c2 == c1:
            c2 = random.choice(list)
        print ('\t\t',c1.title()+'iggly'+c2+'uff')

