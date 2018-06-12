import math 

f = 2.4 
fs = 16
n = 10
t = 1/fs
x = []

for i in range(n + 1):
    x.append(math.cos(2*math.pi*f*i*t))

print(x)