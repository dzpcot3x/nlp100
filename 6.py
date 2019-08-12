#文字N-gram
def c_gram(s, N):
    c = ''.join(s.split())
    cs = []
    for i in range(len(c)-N+1):
        cs.append(c[i:(i+N)])
    return cs

s1, s2 = "paraparaparadise", "paragraph"

N = 2
X = c_gram(s1, N)
Y = c_gram(s2, N)

#和集合
print(list(set(X+Y)))
#積集合
print(list(set(X)&set(Y)))
#差集合
print(list(set(X)^set(Y)))

# 'se'がXおよびYに含まれるかどうか
print('se' in X, 'se' in Y)
