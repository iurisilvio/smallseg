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
A,B = seg.cut(s3) #A是识别出的登录词列表，B是未登录词列表
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
    


def test1(text):
    A,B = seg.cut(text) #A是识别出的登录词列表，B是未登录词列表
    print "********************************"
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
        
if __name__=="__main__":
    test1("这是一个伸手不见五指的黑夜。我叫孙君意，我爱北京，我爱Python和C++。")
    test1("我不喜欢日本和服。")
    test1("雷猴回归人间。")
    test1("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")