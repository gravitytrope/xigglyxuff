#!/usr/bin/python
import random, sys, time

# ints = [1,2,3,4,5,6,7,8,9]
# squares = [i*i for i in ints if i%2 == 0 else 0]

def main():
    # Defining the default list in english
    listy = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n',
             'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',
             'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
             'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',
             'ch', 'cl', 'kl', 'kr', 'schw', 'sch',
             'schl', 'y', '']
    # Our default bits that aren't changed
    e1 = 'iggly'
    e2 = 'uff'
    print('▀▄▒▄▀ ▀█▀ ▒█▀▀█ ▒█▀▀█ ▒█░░░ ▒█░░▒█ ▀▄▒▄▀ ▒█░▒█ ▒█▀▀▀ ▒█▀▀▀ █ ')
    print('░▒█░░ ▒█░ ▒█░▄▄ ▒█░▄▄ ▒█░░░ ▒█▄▄▄█ ░▒█░░ ▒█░▒█ ▒█▀▀▀ ▒█▀▀▀ ▀ ')
    print('▄▀▒▀▄ ▄█▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ░░▒█░░ ▄▀▒▀▄ ░▀▄▄▀ ▒█░░░ ▒█░░░ ▄ ')
    print('\nHello, pokédude!')
    print('\nWhat language do you speak, human? (Russian/ru, English/en, Robotic/ro, Potato/po)')
    # Convert user input to a stringywingy
    l1 = str(input())
    # Stuff we do if he or she chooses English
    if l1 == 'en':
        print('English selected.')
    elif l1 == 'ru': # Change the list to Russian!
        listy = ['в', 'd', 'f', 'g', 'j', 'l', 'м', 'п',
                 'ґ', '₴', 'т', 'ш', 'z', 'Ьґ', 'вl', 'p',
                 'dґ', 'fl', 'fґ', 'gl', 'gя', 'pl', 'pя',
                 '₴п', '$p', '₴т', '₴щ', 'тґ', 'тш', 'щя',
                 'cн', 'cl', 'кl', 'кя', '$cнш', '$cн',
                 '$cнl', 'у']
        e1 = 'їgglу'
        e2 = 'цff'
        print('Яц₴$їaп ₴ёlёcтёd.')
    elif l1 == 'ro': # Beep boop, robot list. Things get weird.
        listy = ['┬BZZZZZT', '╒BZZZZT',
                 '║first law of robotics: A robot may not injure a human being or, through inaction, allow a human being to come to harm.',
                 '╔', '∩01100', '®', '©', '¥',
                 '¢TARGET ACQUIRED. ENGAGING.', 'ONEZEROZEROONEONEZEROONEONEZEROONEZEROZEROONEONEƒ',
                 '$Captain, I have detected a seismic disturbance on the planet\' surface. It seems to be emanating fro-BKJAOERRORIJDERRORUOSERRORAIJERRORFLIAUERRORDSHFOERRORLIUr',
                 '×', '™', '³', '²', 'Δ',
                 '0110100101001101100010111010110010011001',
                 '❤third law of robotics: A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.',
                 'BOOP❥', '웃', '유', '♋', '☮', '✌',
                 '☏DANGER-HOSTILES-DETECTED', '☢EXTERMINATE', '☠KILL ALL HUMANS!', '♚DESTROY. DESTROY.',
                 '100101001100011011011001001101010100', '✔?', '♪', '✈',
                 '⌘404 DOES NOT COMPUTE', '♂BEEP',
                 '♀!second law of robotics: A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.',
                 '❅', 'ツ', '00101001☁', '☃', '✄',
                 '☣if i only had a heeeaarrrtt', '☯RESISTANCE IS FUTILE']
        e1 = '♒✎∞☤✪'
        e2 = '♛♫✫'
        print('✉ღ✘BEEP✍✯☭➳❝ ✡✿BOOP℉❣')
    # Haven't implemented Potato language yet. WIP.
    # elif l1 == 'po':
    # listy = []
    # e1 = ''
    #    e2 = ''
    else:
        # Anything else than gets input is invalid
        # and the script defaults to English because
        # I can't be arsed to ask the user all over again
        print('"' + l1 + '" is an invalid option. Defaulting to English.')

    # Let's get to generating stuff!
    while True:
        try:
            print('\nHow many usernames do you want me to generate? (q to quit)')
            u1 = input()
            # If the user wants to quit, the system exits
            if u1 == 'q':
                sys.exit(0)
            # Start our timer!
            start = time.time()
            # Convert user input to an integer
            u1 = int(u1)
            # Create a new empty list to store our randomly
            # generated set of Xigglyxuff's
            xiglist = []
            # Dealing with errors because fewer than 1 is
            # silly and nobody needs more than 500 Xigglyxuff's
            if u1 < 1 or u1 > 500:
                print('\nWOAH! Are you crazy? That number is totally ridiculous.')
                continue
            # This is where we start picking things from
            # our listy list, randomly of course
            for i in range(u1):
                # It'd be silly if both parts of our
                # Xigglyxuff were the same string
                c1 = random.choice(listy)
                c2 = random.choice(listy)
                while c2 == c1:
                    # So we pick a different random string!
                    c2 = random.choice(listy)
                # Save our choices to a string
                xig = c1.title() + e1 + c2 + e2
                # Add that string to our list of Xigglyxuffs!
                xiglist.append(xig)
            # Saving a recommendation for Prof. Oak to suggest
            # later on in the script
            professor = random.choice(xiglist)
            # This defines how many columns we want to output
            groupsize = 4
            # This outputs all our Xigglyxuff's in a nice format
            # so that everything lines up nicely, and is where
            # Xigglyxuff's finally get printed on the screen
            while len(xiglist) > 0:
                tmp = [xiglist[i] for i in range(groupsize) if i < len(xiglist)]
                print(('{:20s} ' * len(tmp)).format(*tmp))
                xiglist = xiglist[len(tmp):]
            # End our timer
            end = time.time()
            # Calculate how long it took
            elapsed = end - start
            # Print that calculation
            print('\nTime taken:', elapsed, 'seconds.')
            # Print Prof. Oak's recommendation which we
            # saved earlier
            print('\nProfessor Oak thinks', professor, 'is a good choice.')
            # Delete the contents of the list so we can
            # do everythng all over again if the user
            # wants more Xigglyxuffs
            del xiglist[:]
        # Prevents the user from entering non-integers
        except ValueError:
            print('\nOnly integers are accepted. Sort your life out.')

if __name__ == "__main__":
    main()
