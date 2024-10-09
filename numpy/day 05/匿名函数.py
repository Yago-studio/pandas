# 匿名函数的语法格式为：lambda arguments: expression。其中，arguments 是参数列表，
# expression 是一个表达式。当匿名函数被调用时，它将返回 expression 的结果。
from functools import reduce

my_list = [1, 2, 3, 4, 5]
# 将列表中的所有元素加 1
list_plus_1 = list(map(lambda x: x+1, my_list))
print(list_plus_1)
# [2, 3, 4, 5, 6]
# 将列表中的所有元素分别求平方
list_squared = list(map(lambda x: x**2, my_list))
print(list_squared)


# 创建了一个名为 "Chicken" 的类
class Chicken:
    def __init__(self, name, age, color, weight):
# 初始化对象的属性
# 设置实例变量self.name来存储小鸡名字
      self.name = name
# 设置实例变量self.age来存储小鸡年龄
      self.age = age
# 设置实例变量self.color来存储小鸡体色
      self.color = color
# 设置实例变量self.weight来存储小鸡体重
      self.weight = weight
# 调用Chicken类
chicken_01 = Chicken("小红", 1, "黄色", 1.5)
chicken_02 = Chicken("小黄", 1.2, "红色", 2)
print('==小鸡的名字=='); print(chicken_01.name)
print('==小鸡的年龄，yr=='); print(chicken_01.age)
print('==小鸡的颜色=='); print(chicken_01.color)
print('==小鸡的体重，kg=='); print(chicken_01.weight)

total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(total)
