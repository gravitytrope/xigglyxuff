#!/usr/bin/python
import random, sys, time

list = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 
        'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',
        'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
        'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',
        ]



print ('Hello, pokédude.')

while True:
    try:
        print ('\nHow many usernames do you want me to generate? (q to quit)\n')
        u1 = input()
        
        if u1 == 'q':
            sys.exit()
            
        start = time.time()
        u1 = int(u1)
        xigList = []
        
        for i in range(u1):
            xig = ''
            c1 = random.choice(list)
            c2 = random.choice(list)
            while c2 == c1:
                c2 = random.choice(list)
            xig = c1.title()+'iggly'+c2+'uff'
            print ('\t\t',xig)
            xigList.append(xig)

        end = time.time()
        elapsed = end - start
        
        print('\nTime taken:', elapsed, 'seconds.')
        print('\nProfessor Oak thinks', random.choice(xigList) ,'is a good choice.')
        del xigList[:]
        
    except ValueError:
        print('\nOnly integers are accepted. Sort your life out.')
