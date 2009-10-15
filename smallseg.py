import re
class SEG(object):
    def __init__(self):
        self.d = {}
    
    #set dictionary(a list)
    def set(self,keywords):
        p = self.d
        q = {}
        k = ''
        for word in keywords:
            word = chr(11)+word
            p = self.d
            ln = len(word)
            for i in xrange(ln-1,-1,-1):
                char = word[i].lower()
                if p=='':
                    q[k] = {}
                    p = q[k]
                if not (char in p):
                    p[char] = ''
                    q = p
                    k = char
                p = p[char]
        
        pass
    
    def _suffix_ary(self,s):
        ln = len(s)
        R = []
        for i in xrange(0,ln):
            tmp = s[i:]
            if len(tmp)>1:
                R.append(tmp.encode('utf-8'))
        return R
    
    def _pro_unreg(self,piece):
        R = []
        tmp = re.sub("。|，|,|！|…|!|《|》|<|>|\"|'|:|：|？|\?|、|\||“|”|‘|’|；|—|（|）|·|\(|\)|　"," ",piece).split()
        
        for t in tmp:
            ut = t.decode('utf-8')
            mc = re.findall(r"([0-9A-Za-z\-\+#@_\.]+)",ut)
            if (mc!=None) and (len(mc)>0):
                R.extend([xx.encode('utf-8') for xx in mc])
                han = re.split(r"[0-9A-Za-z\-\+#@_\.]+",ut)
                for h in han:
                    R.extend(self._suffix_ary(h))
            else:
                R.extend(self._suffix_ary(ut))
        return R
        
    def cut(self,text):
        """
        """
        p = self.d
        ln = len(text)
        i = ln 
        j = 0
        z = ln
        recognised = []
        unrecognised = []
        
        while i-j>0:
            t = text[i-j-1].lower()
            if not (t in p):
                j = 0
                i -= 1
                p = self.d
                continue
            p = p[t]
            j+=1
            if chr(11) in p:
                p = self.d
                #print i,j
                recognised.append(text[i-j:i])
                if(i<ln):
                    unrecognised.extend(self._pro_unreg(text[i:z]))
                i = i-j
                z = i
                j = 0
        unrecognised.extend(self._pro_unreg(text[i-j:z]))
        return (recognised,unrecognised)
        