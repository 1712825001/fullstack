# 如果目录有__init__可以叫包
import n.m1
print('============================')

print(dir(n))
print('=============================')

print(n.__name__)
print('============================')

print(type(n))
print('=============================')

# dir locals globals是一回事
print(dir())
print(sorted(locals().keys()))
print(sorted(globals().keys()))

import n.m2.m22
import n.m2.m21

import os
print(__file__)
print(os.path.dirname(__file__))
