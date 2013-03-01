'''
Created on 01.03.2013

@author: Vladimir
'''

n = 10001

def primef(n):
    lst = [2]
    for i in xrange(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst

def sieve(n):
        s = xrange(3, n + 1, 2)
        r = set(s)
        [r.difference_update(xrange(n << 1, s[-1] + 1, n)) for n in s if n in r]
        return r.union([2])

a = []
lim = 0

while len(a) < n:
    a = primef(lim)
    lim += 2
    print len(a)

print a.pop()
