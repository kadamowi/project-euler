# This file was *autogenerated* from the file 28.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_1001 = Integer(1001); _sage_const_4 = Integer(4)
ans = _sage_const_1 
now = _sage_const_1 
delta = _sage_const_2 
LMT = _sage_const_1001 **_sage_const_2 
while now < LMT :
    for i in (ellipsis_range(_sage_const_1  ,Ellipsis, _sage_const_4 )) :
        now += delta
        ans += now
    delta += _sage_const_2 
print ans
