# i=9
# while i>=1:
#     j=1
#     while j<=i:
#         print(j,"*",i,"=",j*i,end="  ")
#         j=j+1
#     print()
#     i=i-1
#
#
# count = 0
# username = "lwx"
# userpassword = "123456"
#
# name = input("登录用户名:")
# if name == username:
#       while count <3:
#           password = input("登录密码：")
#           if name == username and password == userpassword:
#                 print("欢迎，%s"  %name )
#                 break
#           else:
#             print("账号密码不匹配")
#             count=count+1
#       else:
#            print ("对不起，您的账号连续输错三次账号已锁定，请联系管理员。")
#            f=open("lwx.txt")
#            f.close()
# else:
#     print ("用户名不存在，请输入正确的用户名。")
#
#
#
# a=56
# b=78
# c=a+b
# b=c-b
# a=c-b
# print(a,b)
#
#
#
# day=0
# h=20
# s=0
# while True:
#     day=day+1
#     s=s+3
#     if s>=h:
#         break
#     else:
#         s=s-2
# print("需要",day,"天")
#
#
#
# a=input("a=")
# b=input("b=")
# c=input("c=")
# a=int(a)
# b=int(b)
# c=int(c)
# if a>0 and b>0 and c>0 and a==b and a==c:
#     print("等边三角形")
# elif a>0 and b>0 and c>0 and a==b and a!=c or a==c and a!=b or b==c and b!=a  and a+c>b and a+b>c and b+c>a:
#     print("等腰三角形")
# elif a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
#     print("普通三角形")
# else:
#     print("不构成三角形")
#
#
# import random
# num=random.randint(50,100)
# print(num)
#




i=1
while i<=7:
    j=1
    while j<=7-i:
        print (" ",end="")
        j=j+1
    k=1
    while k<=i:
        print(" *",end="")
        k=k+1
    print()
    i=i+1


