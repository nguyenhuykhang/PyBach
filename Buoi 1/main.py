# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
x = "awesome"


def myfunc():
    print("Python is " + x)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


y = "0 fine"


def test():
    global y
    y = "fine"
    print_x()


def print_x():
    print(y)

    v = frozenset({"apple", "banana", "cherry"})

c = "hbjebdewhbfwhjbdfr fjwhfhef" \
    "ermnewmnwrmfer,"



d = "Hello, World!"
print(d[0])

age = 36
txt = "My name is John, and I am {}"
# co the dung array
print(txt.format(age))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

import random
print(random.randrange(1, 10))

A = [-10, -6, -4, -1, 0, 4, 8, 9]


def tongam(A):
    m = 0
    for b in A:
            if b < 0:
                m = m + b
    print(m)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
    myfunc()
    tongam(A)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
