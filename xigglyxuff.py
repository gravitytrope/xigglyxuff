#!/usr/bin/python
import random

list = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 
        'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',
        'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
        'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',
        ]

print ('Hello, pokédude. Here are the usernames you requested.\n')

random.shuffle(list)

for i in range(10):
    print ('\t\t',list.pop().title()+'iggly'+list.pop()+'uff')
