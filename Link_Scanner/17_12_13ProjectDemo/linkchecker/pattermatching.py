class BoyerMooreMatch:
    def LastOccuranceFunction(self,c,P):
        j=len(P)-1
        while j>-1:
            if P[j] == c:
                return j
            j = j-1
        return -1
       
    
    def BoyerMoore(self,T,P):
        i=len(P)-1
        j=len(P)-1
        m=len(P)
        n=len(T)
        while i <= n-1:
          #  print T[i]==P[j]
            if T[i]==P[j]:
                print T,P
                if j==0:
                    return i
                else:
                    i = i-1
                    j = j-1
            else:
                l=self.LastOccuranceFunction(T[i],P)
                #print
                i=i+m-min(j,l+1)
                j=m-1
        return -1

    

class inputAndText:
    st=["aaaaaaahaaa","abacaabadcabacabaabb","aaaaaa/e%AAA"]
    pat=["aaah","abacab","/e%"]

#i = inputAndText
#r = BoyerMooreMatch()
#res = r.BoyerMoore(i.st[0],i.pat[0])
#print res
#print i.st[0]
#print i.pat[0]

class patmatch:
    inn=inputAndText()
    try1 = BoyerMooreMatch()
    def mai(self):
        m = len(self.inn.st)
        n = len(self.inn.pat)
        print m,n
        res=[]
        print "length is", m ,"and",n
        for i in range(n):
            for j in range(m):
                match = self.try1.BoyerMoore(self.inn.st[i],self.inn.pat[j])
                if match != -1:
                    print "String",self.inn.st[i],"contain pattern",self.inn.pat[j]
                    res.append(1)
                else:
                    res.append(0)
        print res
       
p = patmatch()
p.mai()

        

            
                    
                

        
        
                    
        
