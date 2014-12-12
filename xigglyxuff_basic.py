import random

listy = ['b', 'd', 'f', 'g', 'j', 'l', 'm', 'n',                                                                                                                
        'r', 's', 't', 'w', 'z', 'br', 'bl', 'p',                                                                                                               
        'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',                                                                                                               
        'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'wr',                                                                                                               
        'ch', 'cl', 'kl', 'kr', 'schw', 'sch',                                                                                                                  
        'schl', 'y']                                                                                                                                            

		c1 = random.choice(listy)                                                                                                                                       
c2 = random.choice(listy)                                                                                                                                       

while c2 == c1:                                                                                                                                                 
    c2 = random.choice(listy)                                                                                                                                   

	xig = c1.title()+'iggly'+c2+'uff'                                                                                                                               

print xig  