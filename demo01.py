# a = (1,2,3,4,"哈哈","哈哈","哈哈","嘻嘻",True,False)
# # print(a[-2])
# # print(a[0:4])
# # print(a.index("哈哈"))
# # print(a.count("哈哈"))
# b = (a,"呵呵","啧啧")
# print(b[0][3])

# a = [1,2,3,4,"哈哈","哈哈","哈哈","嘻嘻",True,False]
# # a.append("append1")
# # a.insert(4,"insert")
# print(a)
# b = a.pop(0)
# c = a.pop(1)
# print(b)
# print(c)
# print(a)

# a = {"name":"张三",0:"hello","age":25}
# print(a["name"])
# a["high"] = "188cm"
# print(a)
# a["name"] = "李四"
# print(a)

# a = {"name":"张三",0:"hello","age":25}
# a.update(name=111111)
# print(a)

# print("---------------------------------")
# print(a.get("name11"))
# print(a["name11"])

# a = [1,2,3,4,"哈哈","哈哈","哈哈","嘻嘻",True,False]
# b = {"name":"张三",0:"hello","age":25}

# del b["name"]
# print(b)

# del a[0]
# print(a)

# a = int(input())
# if a < 10 and a > 1:
#     print("哈哈哈")
# elif a > 10 and a < 100:
#     print("嘿嘿嘿")
# else:
#     print("爱吃奥里给")

# a = "你好"
# if a in "你好，今天吃了那个了吗？":
#     print("ok")
# else:
#     print("not ok")

# HighGrade = {}
# LowGrade = {}
# StudentList = ["张三","李四","王五","五五","六六","七七","一一","二二","三三","四四"]
# a = 0
# while a < len(StudentList):
#     Grade = int(input("请输入"+StudentList[a]+"的成绩："))
#     if Grade >= 60:
#         HighGrade[StudentList[a]] = Grade
#     else:
#         LowGrade[StudentList[a]] = Grade
#     a = a + 1
# print("大于60的：",HighGrade)
# print("小于60的：",LowGrade)
        
# HighGrade = {}
# LowGrade = {}
# StudentList = ["张三","李四","王五","五五","六六","七七","一一","二二","三三","四四"]
# a = 0
# for i in StudentList:
#     Grade = int(input("请输入"+ i +"的成绩："))
#     if Grade >= 60:
#         HighGrade[i] = Grade
#     else:
#         LowGrade[i] = Grade
#     a = a + 1
# print("大于60的：",HighGrade)
# print("小于60的：",LowGrade)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"x",j,"=",i*j,end="  ")
#     print()

# light = {"红灯":30,"绿灯":35,"黄灯":3}
# for i in light:
#     for j in range(light[i]):
#         print(i,j)

# light = {"红灯":30,"绿灯":35,"黄灯":3}
# for i in light:
#     for j in range(light[i]):
#         print(i,"倒计时还有",light[i]-j,"秒")

# username = input("请输入账号：")
# password = input("请输入密码：")
# if len(username) >= 5 and len(username) <= 8:
#     if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#         if len(password) >= 8 and len(password) <= 12:
#             print("注册成功！",{username:password})
#     else:
#         print("账号的首字母必须小写字母开头！")
# else:
#     print("账号的长度不符合规范，请输入5-8位的账号")

# for i in range(10):
#     if i == 4:
#         continue
#     print(i)

# for i in range(10):
#     if i == 4:
#         break
#     print(i)



# def checkname(username):
#     """
#     自动地判断账号长度是5~8位，并且账号必须小写开头
#     """
#     if len(username) >= 5 and len(username) <= 8:
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#             print("OK")
#         else:
#             print("账号的首字母必须小写字母开头！")
#     else:
#         print("账号的长度不符合规范，请输入5~8位的账号！")

# def plus(a,b):
#     """
#     本函数可实现将两个数字相加
#     """
#     if type(a) is int and type(b) is int:
#         print(a+b)
#     else:
#         print("输入的数据类型不正确！")

# a = []
# print(a.append("哈哈哈"))
# print(a.count("哈哈哈"))

# try:
#     print(fawefwef+1)
# except Exception as e:
#     print("代码错误！",e)

# a = input("请输入你的名字：")
# b = input("请输入你的年龄：")
# try:
#     if int(b) >= 18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except:
#     print("请输入正确的年龄！")

# import time
# for i in range(10):
#     time.sleep(1)
#     print(i)


# import random
# a = random.randint(100,1000)
# print(a)

# import pymysql
# db = pymysql.connect(host="127.0.0.1",user="root",password="admin",db="test")
# cur = db.cursor()
# try:
#     cur.execute("select * from t_class;")
#     res = cur.fetchall()
#     print(res)
# except:
#     print("sql语句错误！")

# page61

# class GirlFriend():
#     def __init__(self):
#         self.sex = "女"
#         self.high = "165cm"
#         self.weight = "50kg"
#         self.hair = "短头发"
#         self.age = "25岁"
    
#     def Talent(self,num):
#         """
#         才艺表演
#         """
#         if num == 1:
#             print("你的身高为"+self.high+"，体重为"+self.weight+"发型为"+self.hair+"的"+self.sex+"朋友"+"开始了胸口碎大石！")
#         elif num == 2:
#             print("你的身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"的"+self.sex+"朋友"+"开始了唱跳RAP篮球！")
#         else:
#             print("你的身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"的"+self.sex+"朋友"+"开始了单手开瓶盖！")

#     def Cooking(self):
#         """厨艺持家"""
#         print("精通八大菜系！")

#     def Job(self):
#         """
#         工作挣钱
#         """
#         print("开挖掘机！")

# 类的实例化
# She = GirlFriend()
# She.Talent(2)


# class GirlFriend():
#     def __init__(self,sex,high,weight,hair,age):
#         self.sex = sex
#         self.high = high
#         self.weight = weight
#         self.hair = hair
#         self.age = age
    
#     def Talent(self,num):
#         """
#         才艺表演
#         """
#         if num == 1:
#             print("你的身高为"+self.high+"，体重为"+self.weight+"发型为"+self.hair+"的"+self.sex+"朋友"+"开始了胸口碎大石！")
#         elif num == 2:
#             print("你的身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"的"+self.sex+"朋友"+"开始了唱跳RAP篮球！")
#         else:
#             print("你的身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"的"+self.sex+"朋友"+"开始了单手开瓶盖！")

#     def Job(self):
#         """
#         工作挣钱
#         """
#         print("开挖掘机！")

# # 继承
# class GirlFriend1(GirlFriend):
#     pass

# # 重写
# class GirlFriend2(GirlFriend):
#     def Job(self):
#         print("修电脑！")

# She = GirlFriend2("女","170cm","51kg","长头发","18岁")
# She.Talent(3)
# She.Job()

import time

now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天的心情：")
with open("e:\日记.txt","a",encoding="utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("-----------------------------------\n")




