"""
练习：通过代码获取两段内容，并且计算他们长度的和。123
"""
# a = input("请输入内容：")
# b = input("请输入内容：")
# print(len(a+b))

"""
练习：
获取用户输入的个人信息，并且存储到字典中。
个人信息包括了：name，age，sex。
"""

# a = input("请输入你的姓名：")
# b = input("请输入你的年龄：")
# c = input("请输入你的性别：")

# xx = {"name":a,"age":b,"sex":c}
# print(xx)

# 第二种方法
# userinfo = {}
# userinfo.update(name=a,age=b,sex=c)
# print(userinfo)

# 第三种方法
# userinfo = {}
# userinfo["name"] = a
# userinfo["age"] = b
# userinfo["sex"] = c
# print(userinfo)

"""
练习：现在有10个学生的成绩，需要录入到系统中，
这10个人分别是：张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠
并且名字和成绩需要对应上 而已大于60和小于60的要分开存放
"""
"""
high = {}  # 定义了一个空字典 用来存储大于60的成绩
low = {}  # 定义了一个空字典 用来存储小于60的成绩
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠"]  # 定义了一个列表 用来存储姓名
a = 0  # 定义了一个变量 用来控制数组的下标变化
while a < len(studentlist):  # 因为所有的录入都是要用input，所以写了循环，len判断了数组的长度
    chengji = int(input("请输入"+studentlist[a]+"的成绩："))  # 录入信息 为了方便判断 所以转换成整数
    if chengji >= 60:  # 判断分数
        high[studentlist[a]] = chengji  # 存到字典中
    else:
        low[studentlist[a]] = chengji
    a = a + 1  # 控制下标变化 每一次循环 都+1
print("大于60的：",high)
print("小于60的：",low)
"""
# for方法
"""
high = {}  # 定义了一个空字典 用来存储大于60的成绩
low = {}  # 定义了一个空字典 用来存储小于60的成绩
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠"]  # 定义了一个列表 用来存储姓名
for i in studentlist:
    chengji = int(input("请输入"+i+"的成绩："))  # 录入信息 为了方便判断 所以转换成整数
    if chengji >= 60:  # 判断分数
        high[i] = chengji  # 存到字典中
    else:
        low[i] = chengji
print("大于60的：",high)
print("小于60的：",low)
"""

"""
练习：打印九九乘法表
"""