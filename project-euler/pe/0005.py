'''
Created on 28.02.2013

@author: Vladimir
'''

import math
n = 2*3*5*7*2*3*2*11*13*17*19*2
print 2*3*5*7*2*3*2
print n
for i in range(1, 21):
    res = True
    res = res and (n%i == 0)
    if res == False:
        print i

print res