import re
class SEG(object):
    def __init__(self):
        self.d = {}
        self.stopwords= set([u'了',u'的',u'时',u'上',u'下',u'里',u'外',u'中',u'是',u'有',u'都'])
    #set dictionary(a list)
    def set(self,keywords):
        p = self.d
        q = {}
        k = ''
        for word in keywords:
            word = (chr(11)+word).decode('utf-8')
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
    
    def _binary_seg(self,s):
        ln = len(s)
        if ln==1:
            return [s]
        R = []
        for i in xrange(ln,1,-1):
            tmp = s[i-2:i]
            R.append(tmp)
        return R
    
    def _pro_unreg(self,piece):
        #print piece
        R = []
        tmp = re.sub(u"。|，|,|！|…|!|《|》|<|>|\"|'|:|：|？|\?|、|\||“|”|‘|’|；|—|（|）|·|\(|\)|　"," ",piece).split()
        ln1 = len(tmp)
        for i in xrange(len(tmp)-1,-1,-1):
            mc = re.split(r"([0-9A-Za-z\-\+#@_\.]+)",tmp[i])
            for j in xrange(len(mc)-1,-1,-1):
                r = mc[j]
                if re.search(r"([0-9A-Za-z\-\+#@_\.]+)",r)!=None:
                    R.append(r)
                else:
                    R.extend(self._binary_seg(r))
        return R
        
        
    def cut(self,text):
        """
        """
        text = text.decode('utf-8','ignore')
        p = self.d
        ln = len(text)
        i = ln 
        j = 0
        z = ln
        recognised = []
        mem = None
        while i-j>0:
            t = text[i-j-1].lower()
            #print i,j,t,mem
            if not (t in p):
                if mem!=None:
                    i,j,z = mem
                    p = self.d
                    if((i<ln) and (i<z)):
                        recognised.extend(self._pro_unreg(text[i:z]))
                    recognised.append(text[i-j:i])
                    i = i-j
                    z = i
                    j = 0
                    mem = None
                    continue
                
                j = 0
                i -= 1
                p = self.d
                continue
            p = p[t]
            j+=1
            if chr(11) in p:
                if j<=2:
                    mem = i,j,z
                    #print text[i-1]
                    if text[i-1] in self.stopwords:
                        p = self.d
                        i -= 1
                        j = 0
                    continue
                    #print mem
                p = self.d
                #print i,j
                if((i<ln) and (i<z)):
                    recognised.extend(self._pro_unreg(text[i:z]))
                recognised.append(text[i-j:i])
                i = i-j
                z = i
                j = 0
                mem = None
       
        recognised.extend(self._pro_unreg(text[i-j:z]))
        return recognised