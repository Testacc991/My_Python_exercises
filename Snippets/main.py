import sys
import math
from datetime import datetime

def print1():
    print ("hello.py")
# Get python version
def version():
    print(sys.version)
# area of circle
def area(radius):
    area = math.pi * radius ** 2
    print (area)
# print date
def date():
    now1 = datetime.now()
    dt_string = now1.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
#  get name
def getinput():
    fname = input("Enter your name")
    sname = input("Enter your surname")
    print ("Hello: "+ sname + " " + fname)
# print list using commas
def list_tuple():
    text = input()
    list1 = text.split(",")
    tuple1 = tuple(list1)
    print(list1)
    print(tuple1)
# Write a Python program to print all even numbers
#  from a given numbers list in the
#  same order and stop the printing if
#  any numbers that come after 237 in the sequence.
#  Go to the editor
def odd_even():
    numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

    for x in numbers:
        if x == 237:
            break 
        if x % 2 == 0:
            print(x, end = " ")
    print("\n")
# 32. Write a Python program to get the least
#  common multiple (LCM)
#  of two positive integers.
# найменше спільне кратне
def lcm():
    a = input()
    b = input()
#Спільні кратні
def common_mult(numbers):
    inta = 0
    intb = 0
    starta = 0
    startb = 0
    a = input()
    b = input()
    list1 = []
    list2 = []
    starta = int(a)
    startb = int(b)
    for i in range(numbers):
        inta += starta
        list1.append(inta)
        intb += startb
        list2.append(intb)
        set1 = set(list1)
        set2 = set(list2)
    finalset = set1.symmetric_difference(set2) 
    print(finalset)

def multinum():
    list5 = []
    list7 = []
    for i in range(1500,2700):
        if i % 5 == 0:
            list5.append(i)
        elif i % 7 == 0:
            list7.append(i)
    print(list5)
    print(list7)

multinum()