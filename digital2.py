import math

def reh(f_n,h_n):
    result = []
    for i in range(f_leng):
        res = h_n[0]
        for j in range(1,h_leng):
            res += h_n[j]*math.cos(-2*math.pi*f_n[i]*j/fs)
        result.append(res)
    return result

def lmh(f_n,h_n):
    result = []
    for i in range(f_leng):
        res = 0
        for j in range(1,h_leng):
            res += h_n[j]*math.sin(-2*math.pi*f_n[i]*j/fs)
        result.append(res)        
    return result

def absh(re,lm):
    result = []
    for i in range(f_leng):
        res = math.sqrt(re[i]**2 + lm[i]**2)
        result.append(round(res,2))
    return result

fs = 8
#hの値を変更すれば3番の問題に対応できる
h = [1.0,1.0,-1.0,-1.0,1.0]
h_leng = len(h)
f = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]
f_leng = len(f)
ans1 = reh(f,h)
ans2 = lmh(f,h)
ans3 = absh(ans1,ans2)

print("実部は" + str(list(map(round, ans1, [2]*len(ans1)))))
print("虚部は" + str(list(map(round, ans2, [2]*len(ans2)))))
print("振幅特性は" + str(ans3))
