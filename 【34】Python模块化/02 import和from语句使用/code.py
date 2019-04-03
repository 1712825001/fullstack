print(dir())
import os, sys, os.path as ospath
print(dir())
# 第一种方法
from os.path import exists
print(exists)
# 第二种方法
import os
print(os.path.exists)
# 第三种方法
print(os.path.__dict__['exists'])
# 第四种方法
print(getattr(os.path, 'exists'))