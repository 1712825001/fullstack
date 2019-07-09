class A:pass
def b():pass
print(A.__module__) # __main__
print(b.__module__) # __main__
print(A.__name__) # A
print(b.__name__) # b
print(A.__dict__)

class B(A):pass
class C(B):pass
print(C.__bases__) # (<class '__main__.B'>,)
class D(B,A):pass
print(D.__bases__) # (<class '__main__.B'>, <class '__main__.A'>)