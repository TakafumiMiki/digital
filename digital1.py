def answer1():
    result = []
    for i in range(x_leng):
        res = 0
        for j in range(h_leng):
            res += h[j]*x[i-j]
        result.append(res)
    return result

h = [0.3,1.0,0.5,0.0,-0.3]
h_leng = len(h)
x = [1.0,1.0,-1.0,-1.0,1.0,0.0,0.0,0.0,0.0] 
x_leng = len(x)

print(str(answer1()))