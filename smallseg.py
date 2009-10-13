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
            word += chr(11)
            p = self.d
            for char in word:
                char = char.lower()
                if p=='':
                    q[k] = {}
                    p = q[k]
                if not (char in p):
                    p[char] = ''
                    q = p
                    k = char
                p = p[char]
        
        pass
        
    def _pro_unreg(self,piece):
        return re.sub("。|，|,|！|…|!|《|》|<|>|\"|'|:|：|？|\?|、|\||“|”|‘|’|；|—|（|）|·|\(|\)|　"," ",piece).split()
    
    def cut(self,text):
        """
        """
        p = self.d
        i = 0 
        j = 0
        z = 0
        recognised = []
        unrecognised = []
        ln = len(text)
        while i+j<ln:
            t = text[i+j].lower()
            if not (t in p):
                j = 0
                i += 1
                p = self.d
                continue
            p = p[t]
            j+=1
            if chr(11) in p:
                p = self.d
                recognised.append(text[i:i+j])
                unrecognised.extend(self._pro_unreg(text[z:i]))
                i = i+j
                z = i
                j = 0
        unrecognised.extend(self._pro_unreg(text[z:i+j]))
        return (recognised,unrecognised)
        