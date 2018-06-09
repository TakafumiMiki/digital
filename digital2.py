import math
import matplotlib.pyplot as plt

def reh():
    result = []
    for i in range(f_leng):
        res = h[0]
        for j in range(1,h_leng):
            res += h[j]*math.cos(-2*math.pi*f[i]*j/fs)
        result.append(res)
    return result

def lmh():
    result = []
    for i in range(f_leng):
        res = 0
        for j in range(1,h_leng):
            res += h[j]*math.sin(-2*math.pi*f[i]*j/fs)
        result.append(res)        
    return result

def absh(re,lm):
    result = []
    for i in range(f_leng):
        res = math.sqrt(re[i]**2 + lm[i]**2)
        result.append(round(res,2))
    return result

fs = 8
#hの値を変更すれば3,4番の問題に対応できる
#4はdigital1の答えをコピー

h = [0.3, 1.0, 0.5, 0.0,-0.3]
# h = [1.0, 1.0, -1.0, -1.0, 1.0] <= 3 
# h = [0.3, 1.3, 1.2, -0.8, -1.5, 0.2, 0.8, 0.3, -0.3] <= 4
h_leng = len(h)
f = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]
f_leng = len(f)
ans1 = reh()
ans2 = lmh()
ans3 = absh(ans1,ans2)

print("実部は" + str(list(map(round, ans1, [2]*len(ans1)))))
print("虚部は" + str(list(map(round, ans2, [2]*len(ans2)))))
print("振幅特性は" + str(ans3))

left = f
height = ans3
plt.bar(left,height,width = 0.3,color="#1da1f2", linewidth=0)
plt.show()