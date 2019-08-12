s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace(",","").replace(".","")
s = s.split()

l = [1,5,6,7,8,9,15,16,19]
d = {}

for i in range(len(s)):
    if i+1 in l:
        d[s[i][0]] = i+1
    else:
        d[s[i][0:2]] = i+1

# d = sorted(d.items(), key=lambda x:x[1])
# print(d)
# d = dict(d)

print(d)
