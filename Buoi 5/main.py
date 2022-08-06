import math

try:
    a = 5
    b = 0
    a/b
except:
    print("Da co loi")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

import os
os.listdir()

try: # đoạn code có thể gây ra lỗi     pass
    a = 10
    b = 0
    c = a/b
    print(x)
except (NameError, ZeroDivisionError):
    print("Python Quiz")


print("ax**2 + b*x + c = 0")
while True:
    a = int(input("Moi ban nhap a: "))
    b = int(input("Moi ban nhap b: "))
    c = int(input("Moi ban nhap c: "))
try:
    int




delta = (b**2) / (4*a*c)

if delta < 0:
    print("Phuong trinh vo nghiem")
if delta == 0:
    no = -b/2*a
    print("Phuong trinh co nghiem kep la: ", no)
elif delta > 0:
    no_1 = (-b + math.sqrt(delta)) / 2*a
    no_2 = (-b - math.sqrt(delta)) / 2*a
    print("Nghiem cua phuong trinh la: ", no_1, "va", no_2)

