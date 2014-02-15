# This file was *autogenerated* from the file 440.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_987898789 = Integer(987898789); _sage_const_0 = Integer(0); _sage_const_10 = Integer(10); _sage_const_1 = Integer(1)
R = Integers(_sage_const_987898789 )
n = _sage_const_2 
f = [_sage_const_0 ] * (n + _sage_const_1 )

def calc(n) :
    x = matrix(R, [_sage_const_0 , _sage_const_1 ])
    y = matrix(R, [[_sage_const_0 , _sage_const_1 ], 
                   [_sage_const_1 , _sage_const_10 ]])
    return (x * y**n)[_sage_const_0 ][_sage_const_1 ]

ans, single = _sage_const_0 , _sage_const_0 
for i in (ellipsis_range(_sage_const_1  ,Ellipsis, n)) :
    print 'phrase 1:', i
    for j in (ellipsis_range(_sage_const_1  ,Ellipsis, n)) :
        x = gcd(i, j)
        if is_odd(i // x) and is_odd(j // x) :
            f[x] += _sage_const_1 
        else :
            single += _sage_const_1 

for i in (ellipsis_range(_sage_const_1  ,Ellipsis, n)) :
    print 'phrase 2:', i
    x = matrix(R, [_sage_const_0 , _sage_const_1 ])
    y = matrix(R, [[_sage_const_0 , _sage_const_1 ], 
                   [_sage_const_1 , _sage_const_10 ]])
    for j in (ellipsis_range(_sage_const_1  ,Ellipsis, n)) :
        y = y**i
        ans += f[j] * (x * y)[_sage_const_0 ][_sage_const_1 ] # calc(i^j)
    if is_odd(i) :
        ans += single * _sage_const_10 
    else :
        ans += single * _sage_const_1 
print ans, f, single
