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


def cuttest(text):
    wlist = seg.cut(text)
    wlist.reverse()
    tmp = " ".join(wlist)
    print tmp
    print "================================"
        
if __name__=="__main__":
    cuttest("这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。")
    cuttest("我不喜欢日本和服。")
    cuttest("雷猴回归人间。")
    cuttest("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")
    cuttest("我需要廉租房")
    cuttest("永和服装饰品有限公司")
    cuttest("我爱北京天安门")
    cuttest("abc")
    cuttest("隐马尔可夫")
    cuttest("雷猴是个好网站")
    cuttest("“Microsoft”一词由“MICROcomputer（微型计算机）”和“SOFTware（软件）”两部分组成")
    cuttest("草泥马和欺实马是今年的流行词汇")
    cuttest("伊藤洋华堂总府店")
    cuttest("中国科学院计算技术研究所")
    cuttest("罗密欧与朱丽叶")