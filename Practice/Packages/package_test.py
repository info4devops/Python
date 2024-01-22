# Importing package: Pack1
print('--Version:1--')
import Pack1.Module1
Pack1.Module1.f1()
# Module2
Pack1.Module1.f2(10,20)

print('--Version:1--')
from Pack1.Module1 import f2
f2(111,222)



