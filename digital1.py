import matplotlib.pyplot as plt
import numpy as np

def answer1():
    result = []
    for i in range(x_leng):
        res = 0
        for j in range(h_leng):
            if i - j < 0:
                res += h[j]*0  
            else:
                res += h[j]*x[i-j]
        result.append(round(res,2))
    return result

h = [-0.3,0.0,0.5,1.0,0.7,0.3]
h_leng = len(h)

x = [1.0,1.0,0.5,0.5,0.1,0.1,0.0,0.0,0.0]
x_leng = len(x)

print(str(answer1()))

plt.plot([-1,9], [0,0])

w = 0.4
left = np.arange(len(x))
height1 = answer1()
height2 = x
plt.bar(left+w/2, height1, width = w, color="#d97343")
plt.bar(left-w/2, height2, width = w, color="#404cd9")
#日本語使えない
plt.xlabel("n")
plt.ylabel("Signal level")

plt.show()