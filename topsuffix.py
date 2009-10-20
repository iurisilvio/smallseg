"""nd = {}
for l in file("main.dic"):
    word = l.rstrip().decode('utf-8')
    nd[word]=1"""

d={}
for l in file("main.dic"):
    word = l.rstrip().decode('utf-8')
    su = word[-1]
    
    if not (su in d):
        d[su]=0
    d[su]+=1
    
for l in file("main.dic"):
    word = l.rstrip().decode('utf-8')
    su = word[-1]
    if word[:-1] in d:
        d[su]+=10
    
r = d.items()
r.sort(key=lambda x:x[1],reverse=True)
top = r[:101]
for t in top:
    print t[0],t[1]

