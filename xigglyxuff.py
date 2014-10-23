#!/usr/bin/python
import random, sys, time

# ints = [1,2,3,4,5,6,7,8,9]
# squares = [i*i for i in ints if i%2 == 0 else 0]

list = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n',
          'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',
          'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
          'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',
          'ch', 'cl', 'kl', 'kr', 'schw', 'sch',
          'schl', 'y']

e1 = 'iggly'
e2 = 'uff'

print('▀▄▒▄▀ ▀█▀ ▒█▀▀█ ▒█▀▀█ ▒█░░░ ▒█░░▒█ ▀▄▒▄▀ ▒█░▒█ ▒█▀▀▀ ▒█▀▀▀ █ ')
print('░▒█░░ ▒█░ ▒█░▄▄ ▒█░▄▄ ▒█░░░ ▒█▄▄▄█ ░▒█░░ ▒█░▒█ ▒█▀▀▀ ▒█▀▀▀ ▀ ')
print('▄▀▒▀▄ ▄█▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ░░▒█░░ ▄▀▒▀▄ ░▀▄▄▀ ▒█░░░ ▒█░░░ ▄ ')
print('\nHello, pokédude!')
print('\nWhat language do you speak, human? (Russian/ru, English/en, French/fr, German/de)')
l1 = str(input())

if l1 == 'en':
    print('English selected.')
elif l1 == 'ru':
    list = ['в', 'd', 'f', 'g', 'j', 'l', 'м', 'п',
              'ґ', '₴', 'т', 'ш', 'z', 'Ьґ', 'вl', 'p',
              'dґ', 'fl', 'fґ', 'gl', 'gя', 'pl', 'pя',
              '₴п', '$p', '₴т', '₴щ', 'тґ', 'тш', 'щя',
              'cн', 'cl', 'кl', 'кя', '$cнш', '$cн',
              '$cнl', 'у']
    e1 = 'їgglу'
    e2 = 'цff'
    print('Яц₴$їaп ₴ёlёcтёd.')
else:
    print('"'+l1+'" is an invalid option. Defaulting to English.')

while True:
    try:
        print('\nHow many usernames do you want me to generate? (q to quit)')
        u1 = input()
        
        if u1 == 'q':
            sys.exit(0)
            
        start = time.time()
        u1 = int(u1)
                    
        xigList = ['Wigglytuff', 'Jigglypuff', 'Igglybuff']

        if u1 < 1 or u1 > 500:
            print('\nWOAH! Are you crazy? That number is totally ridiculous.')
            continue
            
        for i in range(u1):
            xig = ''
            c1 = random.choice(list)
            c2 = random.choice(list)
            while c2 == c1:
                c2 = random.choice(list)
            xig = c1.title()+e1+c2+e2
            print('\t\t', xig)
            xigList.append(xig)

        end = time.time()
        elapsed = end - start
        
        print('\nTime taken:', elapsed, 'seconds.')
        print('\nProfessor Oak thinks', random.choice(xigList), 'is a good choice.')
        del xigList[:]
          
    except ValueError:
        print('\nOnly integers are accepted. Sort your life out.')
