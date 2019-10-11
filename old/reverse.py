#!/usr/bin/python

a=str(12345)
def reversef(x, y):
    return y+x
b=reduce(reversef,a)
print b
a=list(a)
a.reverse()
print "".join(a)
