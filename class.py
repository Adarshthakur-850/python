# # # t = input("what is your ques: ")
# # # print("answer:", eval(t))
# # # def calc_gcd(num1, num2):
# # #     #x=max(num1,num2)
# # #     #y=min(num2,num1)
# # #     if (num2 == 0):
# # #         return num1
# # #     else:
# # #         return calc_gcd(num2, num1 % num2)


# # # num1 = int(input("a: "))
# # # num2 = int(input('b: '))
# # # res = calc_gcd(num1, num2)
# # # print("GCD: ", res)

# # # using function
# # # def find_odd(a):
# # #     if a % 2 == 0:
# # #         return "even"
# # #     else:
# # #         return "odd"


# # # a = int(input("n: "))
# # # print(find_odd(a))

# # # using recursion
# # # def check(num):
# # #     if num < 2:
# # #         return (check(num-2))


# # # mynumber = int(input())
# # # if (check(mynumber) == True):
# # #     print("Even")
# # # else:
# # #     print("Odd")
# # # def fibo(a):
# # #     if a <= 1:
# # #         return a
# # #     else:
# # #         return (fibo(a-1)+fibo(a-2))


# # # a = int(input())
# # # for i in range(a):
# # # #     print(fibo(i))
# # # a = "This is my first String"
# # # print(a[::-2], sep="\n")

# # # a = int(input("year: "))
# # # b = int(input("month: "))
# # # c = int(input("days: "))
# # # print(a, b, c, sep="\n")


# # # x = int(input("birth year: "))
# # # y = int(input("birth month: "))
# # # z = int(input("birth date: "))
# # # print(x, y, z)

# # #  days = (a-x)*365+(y-b)*30+(z-c)
# # #  print(days)
# # # a = "Python"
# # # b = "Java"
# # # c = a[1:]
# # # d = b[1:]
# # # print(c+d)
# # # a = "How are you?"
# # # print(a[2], a[4])
# # a = "somyadip "
# b = ["anzar", "ali"]
# print(b.join(l1))
# # # # a = "Soumya"
# # # # print(a.(199, " "))
# a = "java is simple"
# print(a.replace("java", "python"))
# # # t = "ojha"
# # a = "soumya is loser"
# # print(a.upper())
# # print(*a, sep=",")
# # print(*a, sep="@")
# # w = a.split()
# # print(w)
# # print(a.title())
# # print(t.join(w))
# # print(a.replace("soumya", "anuj"))
# #
# #import string
# # print(string.punctuation)
# # print(string.printable)

# # a = "!@#$%^&*()_+:jtfy"
# # for i in range(0, len(a)):
# #     if a[i] in string.punctuation:
# #         pass
# #     else:
# #         print(a[i], end=" ")
# # a = "jgfvybiuhyuy"
# # c = a.split()
# # d = list(a)
# # print(c)
# # print(d)
# #
# #
# # a = input("data: ").split(",")
# # print(a)
# # ind = int(input())
# # if (ind <= len(a)-1):
# #     print("list:",a[ind])
# #     #
#  input("data: ").split(",")
#  =t("list:", list(a))
# tuple1 = tuple(a)
# print(tuple1)
# # i = int(input())
# # if i < len(a) and i >= -(len(a)):
# #     print(tuple1(i))
# # else:
# #     print("jo marji wo kr")

# # data = input("data: ").split(",")
# # tuple = tuple(data)
# # index = int(input())
# # list2 = []
# # if index < len(data) and index >= -len(data):
# #     value = input("value:")
# #     list2 = list(data)
# #     list2[index] = value
# #     tuple2 = tuple(list2)
# #     print(tuple2)
# # else:
# #     print("chal na c")
# # TUPLE1 = ("H1", "HELLO", "wow")
# # print(TUPLE1)
# # print(type(TUPLE1))
# # list1 = list(TUPLE1)
# # print(list1)
# # print(type(list1))

# # # print(a[-4:-1])
# # # print(a[-2:-5:-1])
# # # print(a[8:13])
# # # a = "Active"
# # # if len(a) == 1:
# # #     print(a)
# # # elif len(a) == 0:
# # #     print("null")
# # # else:

# # #     print(a[-1]+a[1:-1]+a[0])

# ##############################################################################################

# # n = int(input("Enter a number: "))
# # i = 1
# # sum = 0
# # while (i <= n):
# #     if (i % 2 == 0):
# #         sum = sum+i
# #     i += 1
# # print("The sum of even numbers is: ", sum)
# ##########
# # n = int(input("n: "))
# # counter = 0
# # while counter <= n:
# #     print("Good")
# #     counter += 1
# # else:
# #     print("Not Good")
# #################
# # i = 0
# # while i <= 0:
# #     print("soumya")
# #     i += 1
# ##############
# # number = int(input("Enter number: "))
# # i = 0
# # sum = 0
# # while i <= number:
# #     sum = sum+i
# #     i += 1
# # print("sum: ", sum)
# a = "apple", " mango", " banana"
# b = "123", "3s"
# print(list(a+b))
##################################################
# mydict = {"one": 1, "Two": 2}
# print(type(mydict))
# l = [1, 2, 3, 4, ]
# l2 = ["One", "Two", "Three", "Four"]
# b = dict([(1, "One"), (2, "Two")])
# print(b)
# a = dict(zip(l, l2))
# print(type(a))
# print(mydict['one'])
# print(mydict['Two'])
# foods = {"punjab": "parota", "west bengal": "rosogolla"}
# print(foods.get("punjab"))
# print(foods.get("himachal"))

# a = (2, 3, 34, 5)
# print(a)
# res = zip(a)
# print(list(res))
# a = input("data1:").split(",")
# b = input("data2:").split(",")

# dict1 = dict(zip(a, b))
# dict2 = dict(zip(b, a))
# print(dict1)
# print(dict2):
# dict1 = {"apple": "red", "orange": "orange"}
# print(dict1.copy)
# # dict1.clear()
# print(dict1)
# print(dict1.get("apple", "mango"))
# print(dict1.fromkeys("apple"))
# print(dict1.get("mango", "mango"))


# keys1 = ("one", "two")
# mydict = dict.fromkeys(keys1)
# print(mydict)
# mydict2 = (1, 2)
# print(mydict.update(mydict2))
#
# n = 10
# for i in range(n):
#     if i > n:
#         i += 1
#     print(i)
# a = [1, 2, 3]
# print(a)
# print(tuple(a))


# print(sorted(mydict.keys()))
# # print(sorted(mydict.values()))
# b = [i for i in range(1, 11) if (not i % 2)]
# print(b)
# my_students = {
#     "name": "john",
#     "grades": [48, 47, 49]
# }


# def average_grade(student):
#     return sum(student["grades"])/len(student["grades"])


# print(average_grade(my_students))


# class Student:
#     def __init__(self, new_name, new_grades):
#         self.name = new_name
#         self.grades = new_grades

#     def average(self):
#         return sum(self.grades)/len(self.grades)


# stud1 = Student("Smith", [70, 80, 90])
# stud2 = Student("Jose", [30, 70, 90])
# print(stud1.name)
# print(stud1.__class__)
# print(stud2.name)
# print(stud2.__class__)
# print(stud1.average())
# print(stud1.grades)
# print(Student.average(stud2))


# def average(stud1):
#     return sum(stud1.grades)/len(stud1.grades)


# print(average(stud1))


# class Cars:
#     def __init__(self, colour, model):
#         self.colour = colour
#         self.model = model

#     def mychoice(self):
#         return self.colour, self.model


# car1 = Cars("red", "lambo")
# car2 = Cars("black", "audi")
# print(car1.mychoice())
# print(car2.mychoice())


# class cars:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def show(self):
#         return "name:", self.name, "model:", self.model, "color:", self.color


# car1 = cars("soumya", "audi", "black")
# print(car1.show())


# class student:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email

#     def show(self):
#         return "name: ", self.name, "age", self.age, "email:", self.email


# name1 = input()
# age1 = int(input())
# email1 = input()
# stud1 = student(name1, age1, email1)
# print(stud1.show())
# name2 = input()
# age2 = int(input())
# email2 = input()
# stud2 = student(name2, age2, email2)
# print(stud2.show())
# Method Overloading


# class Greeting():
#     def sayHello(self, name=None, wish=None):
#         if (name is not None and wish is not None):
#             print(("Hello"+name+wish))
#         elif (name is not None and wish is None):
#             print("Hello"+name)
#         else:
#             print("Hello")


# obj1 = Greeting()
# obj1.sayHello()
# obj1.sayHello("John")
# obj1.sayHello("John", "GoodMorning!")
#############################################
# inharotance

# class Games:
#     def cons(self, cons):
#         self.cons = cons

#     def conse(self):
#         print("Console Name: ", self.cons)

#     def selcat(self, cat):
#         self.cat = cat

#     def selcate(self):
#         print("Category: ", self.cat)


# class PCgames(Game):
#     def name(self, name):

#         self.name = name

#     def namee(self):

#         print("Name: ", self.name)

#     def tour(self, tour):

#         self.tour = tour

#     def toure(self):

#         print("Tournament Name: ", self.tour)


# mg = PCgames()
# print("Details: ")
# mg.cons(input("Enter Console: "))
# mg.selcat(input("Enter Category: "))
# mg.name(input("Enter Name: "))
# mg.tour(input("Enter tourney name: "))
# mg.conse()
# mg.selcate()
# mg.namee()
# mg.toure()
# ####################
# parent class####################
# class Animal:
#     def __init__(self, name="This animal"):
#         self.name = name

#     def eat(self):
#         print(self.name, "eats biscuit")


# class Mammal(Animal):
#     def eat(self):
#         print(self.name, " eat nothing")


# class Winganimal(Animal):
#     def eat(self):
#         print(self.name, "eat everything")


# class Nightowl(Winganimal, Mammal):
#     def sleep():
#         print("sleeps at day")


# class vulture(Mammal, Winganimal):
#     def sleep():
#         print("sleep at night")


# print("First instance of Animal class . Parent class")
# dog = Animal("priyangshu")
# dog.eat()
# print("Creating an instance of Mammal Class")
# cow = Mammal("Cow")
# cow.eat()
# Nightowll = Nightowl("sujal")
# Vulture = vulture("ashish")
# Nightowll.eat()
# Nightowl.sleep()
###############################
# data hiding method

# class Student:
#     def __init__(self, name):
#         self.__name = name

#     def printname(self):
#         print(self.__name)


# stu1 = Student("Soumya")
# # for public
# stu1.printname()
# # for private
# stu1.__name()
#########
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def setdetails(self, group, report):
#         self.__group = group
#         self.__report = report

#     def getdetails(self):
#         print(self.name)
#         print(self.age)
#         print(self.__group)
#         print(self.__report)


# obj = Student("student", "18",)
# obj.setdetails("k22lr", "g1")
# obj.getdetails()
#######################
# file handling
# fr = open("for_check.txt", "r")
# fw = open("for_check1.py", "w")

# # content = fr1.read()
# # con2 = fw1.write(content)
# fw.write(fr.read())

# fr.close()
# fw.close()

# fr1 = open("for_check.py", "r+")
# # print(fr1.read(12))
# # print(fr1.tell())
# print(fr1.write("yes,you can do"))
# print(fr1.seek(0))
# print(fr1.read())
# print(fr1.seek(0))
# print(fr1.read())
# fr1.close
# a = "This is my first string"
# i = "f"

# myfile = open('file.txt', 'r+')
# file_content = myfile.readlines()
# myfile.write('''soumya
# dip
# ojha''')
# myfile.close()
# print(file_content)

# myfile = open('file1.txt', 'r+')
# myfile.write('''Hello
# How are you!!
# Good Morning''')

# myfile.close()
# new = open('file1.txt', 'r')
# data1 = new.readlines()
# print(data1)
# res = 0
# words = 0
# for line in data1:
#     res += 1
#     words += len(line.split(" "))

# print("no. of words:", words)
# print("no of lines: ", res)
# replicate = open('newfile.txt', 'w+')
# for line in data1:
#     replicate.write(line)
# replicate.close()


# try:
#     a = 0
#     b = 0
#     c = a+b
#     d = a/b
#     print("all operations are successful", c, d)
# except ZeroDivisionError:
#     print("A number can't be devided by zero")
# except ArithmeticError:
#     print("An Arithmetic error")
try:
    a = [1, 2, 3]
    print(a[3])
except LookupError:
    print("Index out of bound occur")
else:
    print("success")
    # username = input("Enter username: ")
# newfile = open('file.txt', 'r')
# # newfile.write(username)
# newfile.write("hello how r u")
# newfile.close()
# fr3 = open("file.txt")
# print(fr3.seek(0))


def checkage(age):
    if age < 0:
        raise ValueError("0 se bada hona chahiye")
    print("age is valid")


try:
    age =int(input())
    checkage(age)
except ValueError as err:
    print(err.args)
finally:
    print("Executed in any condition")


# c="s"
# if i in a or c in a:
# print(i,c,sep="\n")
# print(a[:])

# python math module
# maths using recursion how return works

# def factorial(x):
# if x==1:
# return x
# else:
# return x*factorial(x-1)
# x=int(input())
# print(factorial(x))

# def recur_fibo(n):
# if n <= 1:
# return n
# else:
# return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 5

# # check if the number of terms is valid
# if nterms <= 0:
# print("Plese enter a positive integer")
# else:
# print("Fibonacci sequence:")
# for i in range(nterms):
# print(recur_fibo(i))


# def check_odd_even(num):
# if (num<2):
# return (num%2==0)
# return(check_odd_even(num-2))
# my=int(input())
# if (check_odd_even(my)==True):
# print("Even")
# else:
# print("odd")


# def gcd(a, b):
# if a == b:
# return a
# elif a < b:
# return gcd(b, a)
# else:
# return gcd(b, a - b)

# a = 32
# b = 12
# print(gcd(a, b))

# def gcd(a,b):
# x=max(a,b)
# y=min(a,b)
# if b==0:
# return a
# else:
# return gcd(y,x%y)
# a=int(input())
# b=int(input())
# print(gcd(a,b))


# recursion

# def add(x,y):
# if y==0:
# return(x)
# else:
# return add(x,y-1)+1
# a=int(input())
# b=int(input())
# print(add(a,b))

# recurtion( a function that calls its self)(base and recursive criterion )what is recurtion

# def rc(n):
# if n==0:
# f=1
# return f
# elif n>0:
# f=n*rc(n-1)
# return f
# num=10
# if num<0:
# print("factorial no",)
# else:
# print("factorial",rc(num))

# factorial using recursion
# def factorial(n):
# if n==0:
# return 1
# return n*factorial(n-1)
# n=int(input())
# result=factorial(n)
# print(result)
############################

# adding no up to range usin recursion
# def add(n):
# if n==0:
# return 0
# return n+add(n-1)
# r=add(4)
# print(r)
#########################################

# using return statemnet of a function as an argument in another#(function compositon)
# def square(x):
# x=x*2
# return x
# def double(x):
# x=2*x
# return x
# num=2
# print(" das din may paisa double ",square(double(num)))
########################

# gobal vs local
# a=int(input())
# def cg():
# global a
# a=500
# def cl():
# a=200
# print(a)
# print(a)
# cg()
# print(a)
# cl()
##################################
# anomes function,lamda function,map function,filter function,list comprehesnion,fruitful funciton,global and local variabels,recurtion,parameters and arguments

# while True:
# tax=lambda salary:salary*20/100
# salary=int(input())
# print("tax to be paid",tax(salary))
###########################################
# d=lambda x:x*2
# x=int(input())
# print(d(x))
#########################

# #map function
# def square(x):
# return x**2
# l=[1,2,3,4,5]
# print(list(map(square,l)))
############################
# def a(x):
# return(x*3)
# listt=[1,2,3,4,45,6,7,8,9]
# a=list(map(a,listt))
# print(a)
################################
# local variabels
# def test1():
# a=50
# b=30
# print(a,b)
# test1()
################################
# num=[1,2,3,4,5,6,7,7,78]
# even=list(filter(lambda n:n%2==0,num))
# print(even)
###############################

#############################
# filter function
# a=[1,2,3,4,5,7,9]
# b=[2,3,6,7,9,8]
# print(list(filter( lambda x:x in a,b)))
##################################################
# def largest(a,b,c):
# if a >b and a>c:
# return a
# elif b>a and b>c:
# print(b)
# else:
# print(c)
# largest(1,2,3)
###################
# def h(x,y):
# mod=1
# while(mod!=0):
# mod=y%x
# g=x
# y=x
# x=mod
# return g
# print(h(50,20))
#####################


# functions
# def cal(s=3,p=20):
# print(s*p/100)
# x=int(input())
# y=int(input())
# cal(s=x)
# cal(s=x,p=y)
########################################
# def lar(*nu):
# max=0
# for i in nu:
# if i>max:
# max=i
# print(max)

# lar(1,3,4,5,6)
# def lar(*nu):
# print(max(nu))
# lar(1,2,3,4,5)
########################################
###dont know how many arguments##########
# def add(*args):
# sum=0
# for i in args:
# sum=sum+i
# print(sum)
# add(1,2)
# add(1,2,3,4,5,6,7,87,8,9,9,0)
##################################
#####function#######
# def add (a,b):
# """addition"""
# print(a+b)
# a=3
# b=4
# add(a,b)
# print(add.__doc__)
########################
# a=int(input())
# b=int(input())
# def add (a,b):
# print(a+b)
# def sub (a,b):
# print(a-b)
# def mul (a,b):
# print(a*b)
# add(a,b)
# sub(a,b)
# mul(a,b)
########################
# def add(a):
# return a*2
# a=int(input())
# print("the sum is", add(a))

# def e(isrich,isyoung,ishandsome):
# if(isrich):
# print("boy is rich")
# elif not (isrich):
# print("boy is poor ")
# if (isyoung):
# print("boy is young")
# if(ishandsome):
# print("boy is handsome ")

# # e(isrich=True,isyoung=True,ishandsome=True)
# e(False,True,True)

##########################################
# def name(*,n,a):
# print(n,a)
# name(a=62,n="sujal")
# name(n="anzar",a=100)
# name(a=98,n="sandeep kaur")

#################################
# default arguments
# def add(a=2,b=3):
# print(a+b)
# add()
# def sub (a=5,b=7):
# print(a-b)
# sub()
# def mul(a=10,b=10):
# a=3
# b=6
# print(a*b)

# mul()
####################################
# positional argument

########################
# def printmesage():
# print("ola la ola la ")
# printmesage()


#diffrence between arguments and functions#
#diffrence between parameters and arguments#


# ###########################
# hcf in python
# a=int(input())
# b=int(input())
# if b <a:
# sm=b
# else:
# sm=a
# for i in range (1,sm+1):
# if a%i==0 and b%i==0:
# print(i)
# ############################
# a=[1,2,3,4,5,6,7,8,9,0]
# for i in a:
# if i%2!=0:
# pass
# else:
# print(i,"is a even no")
##############################
# varaibles and arguments


################################
# a=["a","b","c"]
# for i in a:
# if "a" in i :
# pass
# else:
# print(i)
###############################
# to seprate no into its elements
# a=123
# s=0
# for i in str(a) :
# c=int(i)**2
# s=s+c
# print(s)

# negative addition in python
# uses of modules
# add
# maths in python
# from operator import mod
# fibonacci series
# matrix in python
# logic in python and errors
# prime no in python
# and trigonmetry in python
# how to add numbers of a no togther
# how to add output of for loop to itself
# armstrong no
# n = int(input("Enter a number: "))
# s = 0
# t = n
# while t > 0:
# digit = t % 10
# s += digit * 3
# t //= 10
# if n == s:
# print(n,"is an Armstrong number")
# else:
# print(n,"is not an Armstrong number")
# n=int(input())
# t=n
# d=len(str(n))
# sum=0
# while(t>0):
# dig=t%10
# sum+=dig**d
# t=t//10
# print("sum of powers ",sum)
# if (sum==n):
# print(" this is a armstrong no")
# else:
# print("not an armstrong no ")


# how to make costum eror message

# a=int(input())
# if type(a)!=int:
# raise TypeError("n must be a positive integer")


# #fibonnnac series using for loop
# a=0
# b=1
# c=0
# for i in range(0,10):
# a=b
# b=c
# c=a+b
# print(c)
# fibonaccic series using while loop
# a=0
# b=1
# c=0
# i=0
# while i < 10:
# a=b
# b=c
# c=a+b
# print(c)
# i+=1


# x=int(input())
# y=int(input())
# for num in range(x,y+1):
# for i in range(2,num//2+1):
# if num%i==0:
# break #used to break loop and start over agian
# else:
# print(num)

# n=int(input())
# a=0
# b=1
# print(a)
# if n>0:
# print(b)
# ne=a+b
# while (ne<=n):
# print(ne)
# a=b
# b=ne
# ne=a+b

# a="lets learn"
# for i in a :
# if i=="e":
# continue
# print(i)

# for n in range (1,21):
# if (n<=10):
# continue
# print(n)


# a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# r=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# for i in range (len(a)):
# for j in range(len(a[0])):
# r [j][i]=a[i][j]
# print(r)


# for i in range(1,11):
# for j in range()
# a=["red","big","tasty"]
# f=["apple","bannana","cherry"]
# for i in a:
# for j in f:
# print(i,j)
# a=int(input("no:"))
# sum=0
# r=[]
# for i in range(1,a):
# sum=sum+i
# r.append(i)
# print("factors:",r)
# if sum==a:
# print("perfect no")
# else:
# print("non perfect")

# a=int(input("give no:"))
# b=int(input("give range:"))
# for i in range(1,b+1):
# if i > 20:
# print("limit is 20")
# break
# s=i*a
# print(a,"x",i,"=",s)

# while True:
# g=int(input("give a number and get the table up to ten:"))
# for i in range(1,11):
# s=i*g
# print( g,"x",i,"=",s)

# for i in range (1,11):
# print(i)
# if ,i>=10:
# print("broken")
# break
# else:
# print("no break")

# for i in range (1,10):
# print(i)
# break
# else:
# print("no break")


# for i in range(1,20):
# for j in range(0,20-i):
# print(" ",end="")
# for k in range(1,2*i+1):
# print(0,end="")
# print()

# str1="python"
# x=""
# for i in str1:
# x+=i
# print(x)


# def fib(n):
# a=0
# b=1
# for i in range(2,n,2):
# c=a+b
# a=b
# b=c
# print(c)
# fib(20)

# for i in range(1,7,2):
# print(i)

# i="anzar"
# ie=0
# for it in i:
# print(ie,it)
# ie+=1

# n=[1,10,20,30,40,50]
# sum=0
# for i in n:
# sum=sum+i
# print(sum)

# x=int(input())

# while x<20:

# if x%2==0:
# print("even",x)
# else:
# print("odd",x)
# x+=1

# n=int(input())
# i=0
# a=0
# b=1
# s=0
# while (i<n):
# if (i<=1):
# s=i
# else:
# s=a+b
# a=b
# b=s
# print(s)
# i+=1


# a=int(input())
# b=int(input())
# c=a
# d=b
# m=1
# while (m!=0):
# c%d
# g=c
# c=d
# d=mod
# print(d)


# n1=int(input())
# n2=int(input())
# i=1
# h=0
# while i<=n1:
# if n1%i==0 and n2%i==0:
# h=i
# i=i+1
# print(n1,n2,h)


# c=0
# while c<3:
# c+=1
# print("inside while")
# else:
# print("inside else")
# n=int(input("enter n0:"))
# i=1
# sum=0
# while (i<=n):
# if(i%2==0):
# sum=sum+i
# i=i+1
# print("sum=",sum)

# num=int(input())
# i=int(input())
# while num<=i:
# print(num)
# num=num+1

# import random
# a=input("r for rock or s for scissor p for paper")
# b=("r","s","p")
# c=random.choice(b)
# while True:
# if a=="r" and c=="p":
# print("you lose")
# if a=="s" and c=="p":
# print("you lose")
# if a=="r" and c=="p":
# print("you lose")


# # def checkYear(year):
# # import calendar
# return(calendar.isleap(year))

# year = int(input())
# if year==1900 :
# print("its a leap year")
# elif (checkYear(year)):
# print("Leap Year")
# else:
# print("Not a Leap Year")


# while True:
# y=int(input())
# if y%4==0 and y%100!=0:
# print("leap year")
# elif y%400==0:
# print("leap year")
# else:
# print("not a leap year")


# m=int(input())
# if m>=95:
# print("Marks:5")
# elif m>=90:
# print("Marks:4")
# elif m>=80:
# print("Marks:3")
# elif m>=70:
# print("Marks:2")
# #a={"keyword":12}
# print(type(a))


# a=("ravi")
# print("anzar is ")
# .format


# a=10
# b=10
# c=a is b
# print(c)
############
# practice
# r=7
# for i in range(0,r):#prints rows
# for j in range(r):#prints coloums
# print("*" ,end=" ")
# print("")
# r=7
# for i in range(r):
# for j in range (0,i+1): #because each coloumn is one longer than row no in 0 row there is one star in row 1 there is two stars
# print("*",end="")
# print()
# r=7
# for i in range(r):
# for j in range (i,r):#because i will increase every time printing less stars
# print("*",end=" ")
# print()
# r=7
# for i in range(r):
# for j in range(r-i-1):
# print(" ",end="")
# for j in range(0,i+1):
# print("*",end="")
# print()
# print right angle triangle
# r=7
# for i in range(r):
# print(" "*(r-i-1)+"*"*(i+1))
# print triangle
# r=7
# for i in range(r):
# for j in range(r-i-1):
# print(" ",end="")
# for j in range(0,i+1):
# print("*",end=" ")
# print()

# r=7
# for i in range(r):
# for j in range(0,i+1):
# print(" ",end="")
# for j in range(r-i):
# print("*",end=" ")
# print()
# replace alphabet in string
# m=""
# a="conses"
# b="d"
# c=4
# for i in range(0,len(a)):
# if i==4:
# m+="d"
# continue
# else:
# m=m+a[i]
# print(m)

# a=0
# b=1
# c=a+b
# print(a)
# print(b)
# for i in range(0,11):
# print(c)
# a=b
# b=c
# c=a+b

# a=9474
# b=len(str(a))
# s=0
# while a>0:
# d=a%10
# s+=d**b
# a=a//10
# print(s)

# armstrong function
# def armstrong(a):
# b=len(str(a))
# s=0
# while a>0:
# d=a%10
# s+=d**b
# a=a//10
# print(s)

# a=int(input())
# armstrong(a)
# febonacci function
# def febonacci():
# a=0
# b=1
# print(a)
# print(b)
# c=a+b
# for i in range(0,11):
# print(c)
# a=b
# b=c
# c=a+b
# febonacci()
# hfc function
# def hcf(a,b):
# s=0
# if a>b:
# x=b
# else:
# x=a
# for i in range(1,x+1):
# if a%i==0 and b%i==0:
# s=i
# else:
# continue
# print(s)
# hcf(3,6)

# def lamda():
# print (int(integer/5))
# integer=int(input())
# lamda()

# def no():
# pro=n1*n2
# print("{0:.2f}".format(pro))
# n1=float(input())
# n2=float(input())
# no()

# def str():
# if len(str1) ==len(str2):
# print("True")
# else:
# print("False")
# str1=input()
# str2=input()
# str()

# def alpha():
# x = chr(ord(ch) + 1)
# print (x)
# ch = input()
# alpha()


# str1="How are you?"
# print(str1[4:7])
# print(str1[2],str1[4])
# print(str1[8:-1])
# print(str1[-2:-5:-1])
# print(str1[8:])

# year=365
# leap_year=366
# s=0
# year_1=int(input())
# year_2=int(input())
# for i in range(year_1,year_2):
# if i%400==0 and i%100==0:
# s=s+leap_year
# elif i%4==0 and i%100!=0:
# s=s+leap_year
# else:
# s=s+year
# print(s)
# t=54.19
# print("%5.2f"%t)


# def prime():
# s=0
# for i in range (2,a):
# if a%i==0:
# s+=i
# else:
# continue
# if s==0:
# print("prime")

# else:
# print("not prime")
# a=int(input())
# prime()


# def prime():
# s=Trueg
# for i in range (2,a):
# if a%i==0:
# s=False
# else:
# continue
# if s==True:
# print("prime")

# else:
# print("not prime")
# a=int(input())
# prime()

# a="heeloo"
# b="str2"
# print(a,b)
# string is not mutable

# a="anzar"
# b=["ali khan","anzar"]
# print(a.capitalize())
# print(a.lower())
# print(a.title())
# print(a.center(11,"$"))
# print(a.upper())
# print(a.swapcase())
# # print(a.join(b))
# def add ():
# return a+b
# a=7
# b=3
# print(add())


# def And():
# return a&b
# def Or():
# return a|b
# def xor():
# return a^b
# a=10
# b=2
# print(And())
# print(Or())
# print(xor())


# n=10
# for i in range(n):
# for j in range(i,n):
# print(" ",end="")
# for t in range(i):
# print("*",end="")
# print()


# # n=10
# for i in range(n):
# for j in range(i):
# print(" ",end="")
# for t in range(i,n):
# print("*",end="")
# print()


# n=10
# for i in range(n):
# for j in range(i):
# print(" ",end="")
# for t in range(i,n):
# print("*",end="")
# print()

# def star():
# for i in range(n):
# for j in range(n):
# print("*",end=" ")
# print()
# n=int(input())
# star()

# n=5
# for i in range(n):
# for j in range()
# n=5
# for i in range(n):
# for j in range(i,n):
# print("*",end=" ")
# print()
# a="java is simple"
# print(a.replace("java","python"))
#####################################################
#string #####
# t=""
# a=["www.","codetantra",".com"]
# print(t.join(a))
# import string
# a="python is high"
# print(a.upper())
# print(a.title())
# print(*a,sep="@")
# print(a.split(),sep=",")
# print(a.center(10))
# print(a.replace("python is","i am "))
# print(a.isalnum())
# print(a.isdigit())
# print(a.isalpha())
# print(a.isspace())
# print(a.istitle())
# print(string.punctuation)
# print(string.printable)
# import python
# a="&*$%^&*()_+!ptsd"
# for i in range(len(a)):
# if a[i] in string.punctuation:
# pass
# else:
# print(a[i],end="")
##########################
# a="book"
# b="school"
# print(a*3+b)
############################################
# how to acesses list in list
#########################################
# a="jfsialkf dsaljkfd"
# c=a.split()
#######
# l=list(a)
# print(l)
# print(c)
####
# a="adarsh","rade","wala"
# l=list(a)
# print(l)
######
# c=["red","green","fa"]
# print(type(c))
# print(c)

# l=[1,2,3,4,5,6]
# i=int(input())
# if i not in range(0,len(l)):
# print("index invalid")
# else:
# print(l[i])

# if there is a list inside a tuple it can be edited
# t=("hi","bye")
# s=["tt","rr"]
# r=("hi",s)
# print(r)
# a="anzar"
# print(tuple(a))
# print(type(t))
# print(t[-1])
# print(list(t))
# print(type(list(t)))
##############################################
# a=10,20,30,40,50
# b=list(a)
# c=tuple(a)
# ind=-1
# if ind >=len(a) or ind<0:
# print("invalid index ")
# else:
# print(b,"\n",c)
################################################
# d="10"
# l=d.split(",")
# mt=tuple(l)
# ind=-1
# if ind < len(mt) and ind >=-(len(mt)):
# print("elemt")
# else:
# print("invalid")
############################################
# a=[10,20,30,40]
# a.insert(0,20)
# print(tuple(a))
##############################


# num=input()
# for i in num:
# i=int(i)
# fact=1
# for j in range(1,i+1):
# fact=fact*j
# print(fact)

# def fibo():
# a=0
# b=1
# c=a+b
# print(a)
# print(b)
# print(c)
# for i in range(r):
# a=b
# b=c
# c=a+b
# print(c)
# r=int(input())
# fibo()

# num1=int(input())
# num2=int(input())
# if num1 <num2:
# min=num1
# else:
# min=num2
# while 1:
# if min%num1==0 and min%num2==0:
# print("lcm",min)
# break
# else:
# min=min+1

# def lcm():
# if num1 <num2:
# min=num1
# else:
# min=num2
# while 1:
# if min%num1==0 and min%num2==0:
# print("lcm",min)
# break
# else:
# min=min+1
# num1=int(input())
# num2=int(input())
# lcm()

# import math
# a=int(input())
# print(math.factorial(a))

# n=int(input())
# for i in range(n):
# for j in range(n):


# def recursion(n):
# print(n)
# if n ==2:
# pass
# else:
# return(recursion(n-2))
# n=int(input())
# recursion(n)

# a={"key":"value","key2":"Value2"}
# print(type(a))
# l=[1,2,3,4,5]
# l2=["an","az","er","tr","tl"]
# print(a)
# print(dict(zip(l2,l)))

# d=dict([("an",1),("at",2)])
# print(type(d))
# print(d)

# d={"key":"Value","l":"ty"}
# print(d.get("key")) #only works for key

# d={"punjab":"chandigarh"}
# print(d.get("punjab"))
# print(d)

# a=(1,6,2,3,4)
# print(sorted(a))
# l=list(a)
# print(l)
# print(type(l))
# print(sorted(a()))

# d={"punjab":"value",}
# a=input("value: ")
# b=input("key: ")
# if a==d.get(b):
# print("true")
# else:
# print("False")


# d=input().split(",")
# d2=input().split(",")
# dl=dict(zip(d,d2))
# for k,v in (dl.items()):
# print(k,v)

# a=input().split(",")
# b=input().split(",")
# print(dict(zip(a,b)))
# print(dict(zip(b,a)))


# d1={"a":300,"b":200}
# d2={"a":100,"b":200}
# c={}
# for i in d1:
# if i in d2:
# c=(d1.get(i)+d2.get(i))
# else:
# continue
# print(i,c)S

# a=[1,2,3,4]

# b=[ "hello" for x in a]
# a[2]=5
# del(a[0])
# print(a)
# print(b)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist.reverse()

# print(thislist)


# a="python"
# t=tuple()
# for i in range (len(a)):
# r=list(str(i))
# p=list(a[i])
# z=zip(r,p)
# t+=tuple(z)
# print(t)


# a="python"
# l=[]
# for i in range (len(a)):
# l2=[]
# l2.append(i)
# l2.append(a[i])
# t=tuple(l2)
# l.append(t)
# print(l)


# s=input().split(" ")
# for i in range(len(s)):
# print(s[i],s.count(s[i]))

# dict.items()?

# a="10,12,14"
# b=a.replace(","," ")
# l2=[]
# for element in b:
# if element.isdigit()==True:
# l2.append(element)
# print(l2)


# a={"key":"value","key2":"value2"}
# d=a.update({"keys3":"value3"})
# print(a)
# d=input().split(",")
# d2=input().split(",")
# d3=sorted(d)
# d4=sorted(d2)
# b=dict(zip(d3,d4))
# print(b)
# print(b.values())
# print(b.keys())
# list comprehension

# a=int(input())
# print([i for i in range(0,a) if (i%2==0)])

# b=int(input())
# print([i**2 for i in range(0,b) if(i%2!=0)])

# a=int(input())
# print(["even" if a%2==0 else"odd"])

# transpose a matrix
# m=[[1,2,3,4,10,11],[5,6,7,8,9,0]]
# t=[]
# for i in range(len(m[0])):
# t.append([r[i]for r in m])
# print(t)
# dictonary comprehension,enumrate
# a=["a","b","c"]
# b=[1,2,3]
# print({i:v for (i,v) in zip(a,b)})
# print({i:"anzar" for (i) in a})


# oop in python
# class car:
# def _init_(self,name,model):
# self.name=name
# self.model=model
# def n(self):
# print(self.name)
# print(self.model)


# class Person:
# def __init__(self, name, age,value):
# self.name = name
# self.age = age
# self.value=value

# p1 = Person("trilock", 36,"500cr")

# print(p1.name)
# print(p1.age)
# print(p1.value)

# class cars:
# def __init__(self,name):
# self.name=name
# print("my fav car is",self.name)
# c=cars("tata nano")


# matrix in python sparz matrix
# def is_odd(n):
# return n%2!=0
# a=1,2,3,4,5,6,7,8
# odd=list(filter(is_odd,a))
# print(odd)
# from functools import reduce
# a=1,2,3,4,5,6,7,8
# odd=list(filter(lambda n:n%2!=0 ,a))
# sq=list(map(lambda n: n**2,odd))
# def add(a,b):
# return a+b
# sum=reduce(add,odd)
# su=reduce(lambda a,b:a+b,sq)
# print(odd)
# print(sq)
# print(sum)
# print(su)

# new
# list comprehension allows to write mor effecent code
# l=[x for x in range(0,10) if x%2==0 ]
# print(l)


# classes
# class apple:
# def __init__(self,name,color):
# self.name=name
# self.color=color
# def fruit(self):
# print("my name is",self.name)
# print("i am",self.color,"color")
# a=apple("apple","red")
# a.fruit()
# super is used in base class to acesses properties in parent class#method over riding
# parent class and child class
# class parent:
# def __init__(self,name):
# self.name=name
# print(name)
# class child(parent):
# def __init__(self,age):
# self.age=age
# print(age)
# p=parent("vikask")
# c=child("10")
# print(child.super().name)

# class Animal():
# def __init__(self, Name = "This Animal"):
# self.name = Name
# def eat(self, food = "Grass"):
# print(self.name, "eats" , food)
# class Mammal(Animal):
# def eat(self):
# print(self.name , "nothing")
# class WingedAnimal(Animal):
# def eat(self):
# print(self.name, "eat everything")

# class Nightowl(Mammal,WingedAnimal):
# def sleep():
# print("This creature does not sleep")
# class FruitBat(WingedAnimal, Mammal):
# def sleep():
# print("This creature sleeps a lot")

# print("First instance of Animal class parent class")
# dog = Animal("dog")
# dog.eat()
# print("Creating an instance of Mammal Class")

# data hiding in python

# class Solution:
# __privateCounter = 0

# def sum(self):
# self.__privateCounter += 1
# print(self.__privateCounter)


# count = Solution()
# count.sum()
# count.sum()
# count.sum()
# # Here we have accessed the private data
# # member through class name.
# print(count._Solution__privateCounter)


# class student:
# def __init__(self,name,age):
# self.name=name
# self.age=age

# def pr(self,group,report):
# self.__group=group
# self.__report=report
# def pro(self):
# print(self.name)
# print(self.age)
# print(self.__group)
# print(self.__report)
# s=student("sujal","15")
# s.pr("python","pass")
# s.pro()

# filename = open("text.txt", "w")
# print(filename.write("oooooooooooooooooooooooooooooooooooooohhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
# filename = open("text.txt", "r")
# print(filename.read())
# n=6
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()
# year1 = 2003
# year2 = 2022


# def leap(year1, year2):
#     days = 0
#     for year in range(year1, year2):
#         if year % 4 == 0 or year % 100 == 0:
#             if year % 400 == 0:
#                 days += 365
#                 continue
#             days += 366
#             continue
#         days += 365
#     return days


# daysforyears = leap(year1, year2)
# print(int(daysforyears/365), "Years ,")
