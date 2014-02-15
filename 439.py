# This file was *autogenerated* from the file 439.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_100 = Integer(100); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
def bf(n) :
    ans = _sage_const_0 
    for i in (ellipsis_range(_sage_const_1  ,Ellipsis, n)) :
        for j in (ellipsis_range(_sage_const_1  ,Ellipsis, n)) :
            ans += sum(divisors(i * j))
    return ans

def sphi(n) :
    ans = _sage_const_0 
    for i in (ellipsis_range(_sage_const_1  ,Ellipsis, n)) :
        ans += sum(divisors(i))
    return ans

print sphi(_sage_const_100 )
# f = {}
# for i in [1 .. 30] :
#     f[i] = bf(i)
#     a = 0
#     for j in [1 .. i] :
#         a += f[i // j] * j
#     b = sphi(i)^2
#     print f[i]
