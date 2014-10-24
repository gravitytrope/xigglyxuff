#!/usr/bin/python
import random, sys, time

# ints = [1,2,3,4,5,6,7,8,9]
# squares = [i*i for i in ints if i%2 == 0 else 0]

listy = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n',
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
print('\nWhat language do you speak, human? (Russian/ru, English/en, Robotic/ro, Potato/po)')
l1 = str(input())

if l1 == 'en':
    print('English selected.')
elif l1 == 'ru':
    listy = ['в', 'd', 'f', 'g', 'j', 'l', 'м', 'п',
            'ґ', '₴', 'т', 'ш', 'z', 'Ьґ', 'вl', 'p',
            'dґ', 'fl', 'fґ', 'gl', 'gя', 'pl', 'pя',
            '₴п', '$p', '₴т', '₴щ', 'тґ', 'тш', 'щя',
            'cн', 'cl', 'кl', 'кя', '$cнш', '$cн',
            '$cнl', 'у']
    e1 = 'їgglу'
    e2 = 'цff'
    print('Яц₴$їaп ₴ёlёcтёd.')
elif l1 == 'ro':
    listy = ['┬BZZZZZT', '╒BZZZZT', '║first law of robotics: A robot may not injure a human being or, through inaction, allow a human being to come to harm.', '╔', '∩01100', '®', '©', '¥',
            '¢TARGET ACQUIRED. ENGAGING.', 'ONEZEROZEROONEONEZEROONEONEZEROONEZEROZEROONEONEƒ', '$Captain, I have detected a seismic disturbance on the planet\' surface. It seems to be emanating fro-BKJAOERRORIJDERRORUOSERRORAIJERRORFLIAUERRORDSHFOERRORLIUr', '×', '™', '³', '²', 'Δ',
            '0110100101001101100010111010110010011001', '❤third law of robotics: A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.', 'BOOP❥', '웃', '유', '♋', '☮', '✌',
            '☏DANGER-HOSTILES-DETECTED', '☢EXTERMINATE', '☠KILL ALL HUMANS!', '♚DESTROY. DESTROY.', '100101001100011011011001001101010100', '✔?', '♪', '✈',
            '⌘404 DOES NOT COMPUTE', '♂BEEP', '♀!second law of robotics: A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.', '❅', 'ツ', '00101001☁', '☃', '✄',
            '☣if i only had a heeeaarrrtt', '☯RESISTANCE IS FUTILE']
    e1 = '♒✎∞☤✪'
    e2 = '♛♫✫'
    print('✉ღ✘BEEP✍✯☭➳❝ ✡✿BOOP℉❣')
#elif l1 == 'po':
#    listy = []
#    e1 = ''
#    e2 = ''
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
            c1 = random.choice(listy)
            c2 = random.choice(listy)
            while c2 == c1:
                c2 = random.choice(listy)
            xig = c1.title()+e1+c2+e2
            if i % 4:
                print('\t', xig, end="")
            else:
                print('\n\t', xig, end="")
            xigList.append(xig)

        end = time.time()
        elapsed = end - start
        
        print('\n\nTime taken:', elapsed, 'seconds.')
        print('\nProfessor Oak thinks', random.choice(xigList), 'is a good choice.')
        del xigList[:]
          
    except ValueError:
        print('\nOnly integers are accepted. Sort your life out.')
