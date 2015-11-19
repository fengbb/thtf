def dump(value):
    print (value,"=>", dir(value))

import sys
import os
dump(0)
dump(1.0)
dump(0.0j)
dump([])
dump({})
dump("string")
dump(len)
dump(sys)
#print (eval("__import__('os')."))
eval("'*'*10000000*2*2*2*2*2*2*2")
