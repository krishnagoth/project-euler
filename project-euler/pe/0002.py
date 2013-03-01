'''
Created on 28.02.2013

@author: v.vlasov
'''
import math

last_fib_n = round(math.log(4000000 * (5 ** 0.5), ((1 + 5 ** 0.5) / 2)))
last_fib_n = int(last_fib_n)

print last_fib_n

sum = 0

for n in range(3, 34, 3):
    fib = ((((1 + 5 ** 0.5) / 2) ** n) - ((1 - 5 ** 0.5) / 2) ** n) / (5 ** 0.5)
    print n, fib
    sum+= fib

print int(sum)

