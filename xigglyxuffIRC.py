__module_name__ = 'Xigglyxuff'
__module_version__ = '1.0'
__module_description__ = 'Randomly generates a Xigglyxuff nick'

import random
import hexchat

listy = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n',
        'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',
        'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
        'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',
        ]

c1 = random.choice(listy)
c2 = random.choice(listy)

while c2 == c1:
    c2 = random.choice(listy)
    
print(hexchat.command('nick '+c1.title()+'iggly'+c2+'uff'))
