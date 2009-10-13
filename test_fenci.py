#encoding=utf-8
#import psyco
#psyco.full()

s3 = file("text.txt").read()
words = [x.rstrip() for x in file("main.dic") ]
from smallseg import SEG
seg = SEG()
print 'Load dict...'
seg.set(words)
print "Dict is OK."
A,B = seg.cut(s3) #A是识别出的登录词列表，B是为登录词列表
for t in A:
    try:
        print t.decode('utf-8')
    except:
        pass
print "============================" 
for t in B:
    try:
        print t.decode('utf-8')
    except:
        pass
    
print "********************************"

A,B = seg.cut("这是一个伸手不见五指的黑夜。我叫孙君意，我爱北京，我爱Python和C++。") #A是识别出的登录词列表，B是为登录词列表
for t in A:
    try:
        print t.decode('utf-8')
    except:
        pass
print "============================" 
for t in B:
    try:
        print t.decode('utf-8')
    except:
        pass
        