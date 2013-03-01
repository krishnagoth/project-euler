'''
Created on 28.02.2013

@author: v.vlasov
'''
import math

prev_iter_ctr = 1
iter_ctr = 1
nums = []

#n = 600851475143
n = 638836

nums.append(0)
nums.append(n)

n0 = int(math.floor(math.sqrt(n))) + 1
x = n0
y = 0
k = 1

while n!=1:
    
    for i in range(prev_iter_ctr**2, iter_ctr**2):
            
        n = nums[i]
        
        if (n == 1):
            break
        
        print 'search for ' + str(n),
        
        n0 = int(math.floor(math.sqrt(n))) + 1
        x = n0
        y = 0
        k = 1
        
        while x**2 - n != y**2:    
            x = n0 + k
            prop = math.sqrt(x**2 - n) 
            k+=1
            if prop%round(prop) == 0:
                y = int(prop)
        
        answx = x + y
        answy = x - y
        nums.append(answx)
        nums.append(answy)
        print 'p',answx,
        print 'p',answy, 
        print 'check ' + str(answx * answy)
        
    prev_iter_ctr = iter_ctr
    iter_ctr += 1


