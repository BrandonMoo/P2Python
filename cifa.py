import dis
import os

# file = open("code.txt", "r")
# line = file.readline()
# row = 1
# while(line):
#     gen(line, row)
#     line = file.readline()
#     row += 1

# file.close()

# def gen(line, row:int):
#     words = line.split()

f = "global"

def f1():
    f = "1"
    print ("f1 " + f)
    f2()
    f3()
    def f12():
        print ("f12 " + f)
        f13()
        f14()
    def f13():
        
        print ("f13 " + f)
    def f14():
        f = "14"
        print ("f14 " + f)    
    f12()

def f2():
    f = "2"
    print ("f2 " + f)
    def f22():
        print ("f22 " + f)
    f22()

def f3():
    print ("f3 " + f)
    def f32():
        print ("f32 " + f)
    f32()

x = 10
y = 20
z = 3
def f4():
    x = 1
    y = 2
    g = lambda x:x*2
    w = lambda y:x+y
    h = lambda x,y:x+y
    k = lambda : max(x,y,z)+5
    print(g(4))
    print(w(7))
    print(h(4,4))
    print(k())

x = 2
def outer():
    x = 1
    print("outer x " + str(x))
    def inner():
        nonlocal x 
        x = 0
        print("inner x " + str(x))
    inner()
    print("outer x " + str(x))

if __name__ == "__main__":
    outer()
    print("---------------")
    print("global x " + str(x))
    







