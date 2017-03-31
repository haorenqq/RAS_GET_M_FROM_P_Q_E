# -*- coding: cp936 -*-
import math
import base64

#扩展欧几里德算法
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def compute_d(p, q, e):
    phi = (p - 1) * (q - 1) 
    tup = egcd(e, phi)
    d = tup[1]
    #e * d - k * phi = 1 , e和k均大于0
    if d < 0:
        d += phi
    return d

m = 0x52222222

e = 0x10001
n = 0x80C07AFC9D25404D6555B9ACF3567CF1

#www.factordb.com分解n得到下面两个
p = 11913259462948888787
q = 14365556249124810923

c = pow(m,e,n)
print("cipher is" + hex(c))

d = compute_d(p, q, e)
calc_m = pow(c, d, n)
print("message is" + hex(calc_m))

