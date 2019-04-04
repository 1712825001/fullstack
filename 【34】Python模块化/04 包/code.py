# 如果目录有__init__可以叫包
import m.m1
print('============================')

print(dir(m))
print('=============================')

print(m.__name__)
print('============================')

print(type(m))
print('=============================')

# dir locals globals是一回事
print(dir())
print(sorted(locals().keys()))
print(sorted(globals().keys()))

import m.m2.m22
import m.m2.m21

import os
print(__file__)
print(os.path.dirname(__file__))
