'''
Created on 01.03.2013

@author: v.vlasov
'''

sum = 1000

a = b = c = 0

fact500 = []

for i in range(1, 500):
    if 500 % i == 0:
        fact500.append(i)

for m in fact500:
    n = (500 / m) - m
    if (m ** 2 - n ** 2) ** 2 + (2 * m * n)**2 == (m ** 2 + n ** 2) ** 2 and n > 0 and m > n:
        print m, n, (m ** 2 - n ** 2) * 2 * m * n * (m ** 2 + n ** 2)
