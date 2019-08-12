#単語N-gram
def w_gram(s, N):
    s = s.split()
    ws = []
    for i in range(len(s)-N+1):
        ws.append(s[i:(i+N)])
    return ws

#文字N-gram
def c_gram(s, N):
    c = ''.join(s.split())
    cs = []
    for i in range(len(c)-N+1):
        cs.append(c[i:(i+N)])
    return cs

N = 2
# s = input()
s = "I am an NLPer"

s = s.replace(",","").replace(".","")
print(w_gram(s, N))
print(c_gram(s, N))
