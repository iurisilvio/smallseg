#encoding=utf-8
import math
import random

def readDict():
    d ={}
    for line in open('SogouLabDic.dic'):
        #print line
        tup = line.split('\t')
        word = tup[0].decode('utf-8')
        freq = float(tup[1])
        prop = tup[2].rstrip()
        d[word]=(freq,prop)
    return d

g_dict = readDict()

def rank(solu,hanSentence):
    buf = hanSentence[0]
    ct = solu.count(1)
    pre_buf = None
    for i in xrange(0,len(solu)):
        b = solu[i]
        if b ==0:
            buf += hanSentence[i+1]
        else:
            if buf in g_dict:
                #print g_dict[buf][0]
                if pre_buf:
                    pp1 = g_dict[pre_buf][1]
                    pp2 = g_dict[buf][1]
                    if pp1.find('ADV,')!=-1 and pp2=='V,':
                        ct+=20
                    if pp1=='V,' and pp2.find('N,')!=-1:
                        ct+=20
                    if pp1=='ADJ,' and pp2.find('N,')!=-1:
                        ct+=20
                    if pp1=='CLAS,' and pp2.find('N,')!=-1:
                        ct+=20
                ct+= math.log(g_dict[buf][0])
                pre_buf = buf

            buf = hanSentence[i+1]
    if buf in g_dict:
        ct+= math.log(g_dict[buf][0])

    return ct

def output(solu,hanSentence):
    buf = hanSentence[0]
    result = []
    for i in xrange(0,len(solu)):
        b = solu[i]
        if b ==0:
            buf += hanSentence[i+1]
        else:
            result.append(buf)
            buf = hanSentence[i+1]
    result.append(buf)
    return result
    
def segHanGen(hanSentence):
    def fun_mute(solu):
        n_solu = solu[:]
        c = random.randint(0,len(n_solu)-1)
        if n_solu[c]==0:
            n_solu[c]=1
        else:
            n_solu[c]=0
        return n_solu
        
    def cross(sa,sb):
        i = random.randint(1,len(sa)-1)
        return sa[0:i]+sb[i:]
    
    n = len(hanSentence)-1
    if n<=1: return hanSentence
    pop_size = 50
    elite=0.2
    mute=0.2
    maxiter=100
    population = [[random.randint(0,1) for i in xrange(0,n) ] for j in xrange(pop_size)]
    i_elite = int(elite*pop_size)
    for i in xrange(maxiter):
        population = [s for (r,s) in sorted([(rank(solu,hanSentence),solu) for solu in population],reverse=True)]
        #print population
        population = population[0:i_elite]
        elite_pop = population[:]
        for j in xrange(i_elite,pop_size):
            if random.random()<mute:
                c = random.choice(elite_pop)
                population.append(fun_mute(c))
            else:
                sa = random.choice(elite_pop)
                sb = random.choice(elite_pop)
                population.append(cross(sa,sb))
    population = [s for (r,s) in sorted([(rank(solu,hanSentence),solu) for solu in population],reverse=True)]
    return output(population[0],hanSentence)
    
def segHanAnt(hanSentence):
    pass