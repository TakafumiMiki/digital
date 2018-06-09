import math

def rey(f_n,y_n):
    result = []
    for i in range(f_leng):
        res = y_n[0]
        for j in range(1,y_leng):
            res += y[j]*math.cos(-2*math.pi*f[i]*j/fs) 
        result.append(res)
    return result

def lmy(f_n,y_n):
    result = []
    for i in range(f_leng):
        res = 0
        for j in range(1,y_leng):
            res += y[j]*math.sin(-2*math.pi*f[i]*j/fs) 
        result.append(res)
    return result
    
def absy(re,lm):
    result = []
    for i in range(f_leng):
        res = math.sqrt(re[i]**2 + lm[i]**2)
        result.append(round(res,2))
    return result

#digital1 の答えをyにコピー
fs = 8
y = [0.3, 1.3, 1.2, -0.8, -1.5, 0.2, 0.8, 0.3, -0.3]
y_leng = len(y)
f = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]
f_leng = len(f)
ans1 = rey(f,y)
ans2 = lmy(f,y)
ans3 = absy(ans1,ans2)

print("実部は" + str(list(map(round, ans1, [2]*len(ans1)))))
print("虚部は" + str(list(map(round, ans2, [2]*len(ans2)))))
print("振幅特性は" + str(ans3))