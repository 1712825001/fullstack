# hasattr(object, name) 判断一个对象里面是否有属性或者方法，返回bool值
class Test:
    name = 'aaa'
    def run(self):
        return 'Hello'
test = Test()
print(hasattr(Test, 'name')) # True
print(hasattr(Test, 'run')) # True
print(hasattr(test, 'name')) # True
print(hasattr(test, 'run')) # True

# getattr(object, name[,default])
'''
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号。
'''
print(getattr(test, 'name')) # aaa 存在就打印出来
print(getattr(test, 'run')) # 打印内存地址 <bound method Test.run of <__main__.Test object at 0x000001EC7F2E5438>>
print(getattr(test, "run")()) # hello 后面加括号可以将这个方法运行
# print(getattr(test, 'age')) 不存在的会报错
print(getattr(test, 'age', '18')) # 18 若属性不存在，返回一个默认值

# setattr(object, name, values) 给对象的属性赋值，若属性不存在，先创建再赋值。
setattr(test, "age", "18")
print(hasattr(test, 'age')) # True
