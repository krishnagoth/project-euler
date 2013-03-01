'''
Created on 01.03.2013

@author: v.vlasov
'''

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

print reduce(lambda x, y: x+y, primef(2000000))