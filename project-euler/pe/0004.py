'''
Created on 28.02.2013

@author: v.vlasov
'''
import math

prev_pal = 0
pal = 1
for i in range(999, 99, -1):    
    for j in range(i, 99, -1):
        pal = i*j
        s_pal = str(pal)
        digs = len(s_pal)
        
        res = True
       
        for n in range(int(math.floor(digs/2)) + 1):
            res = res and (s_pal[n] == s_pal[digs - n - 1])
        if (res):
            print pal, i,j
            break
    if prev_pal < pal:
        prev_pal = pal
print prev_pal        