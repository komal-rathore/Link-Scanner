from LinkExtractor.Get_all_links import get_all_links
from LinkExtractor.GetPage import get_page
from Scanner.boyerMoore import *
from linkchecker.linkcheck import *
import time
class linkScan:
    result=[]# to store the result
    def __init__(self,seed,Max_depth):
        self.__seed = seed
        self.__max_depth= Max_depth
        p=[]
        p=[None,seed]
        self.result.append(p)
        
        
    def store_into_parentpage_ChildPage(self,List,parent):
        #print "Parent :"+parent+"\n Child :"
        #print List
        while List:
            p=[]
            child = List.pop()
            p.append(parent)
            p.append(child)
            self.result.append(p)
        #print len(self.result),self.result
        # Retriving of result
        i=0
        while i<len(self.result):
            Pc=self.result[i]
            print Pc[0],Pc[1]
            i = i+1
    
    def union(self,p,q):
        for e in q:
            if e not in p:
                p.append(e)
        return p
    def crawl(self):
        tocrawl = [self.__seed]
        crawled = []
        next_depth = []
        depth = 0
        while tocrawl and depth < self.__max_depth:
            page = tocrawl.pop()
            if page not in crawled:
                self.store_into_parentpage_ChildPage(get_all_links(get_page(page)),page)
                next_depth = self.union(next_depth,get_all_links(get_page(page)))
                crawled.append(page)
            if not tocrawl:
                tocrawl,next_depth = next_depth,[]
                depth = depth+1
        return crawled
    def scan(self):
        #print "############################################################################################################\n"    
        #print self.result
        #print "############################################################################################################\n"  
        i=0
        while i<len(self.result):
            r=[]
            r=self.result[i]
            #print r[1]
            lc = LinkChecker(r[1])
            if lc.check():
               # print "Check is sussessful"
                if not lc.follow():
                   # print("there were problems")
                    print("\n".join(lc.failed))
                    print("\n".join(lc.other))
                else:
                    #print("website OK")
                    self.result[i].append(0)# sets result[parent,child,broken] notbrokenlink=0
            else:
                self.result[i].append(1)#sets result[parent,child,broken] brokenlink=1
                print("cannot open website or homepage is not html")
            #print self.result[i]
            i=i+1
        
    def pattern_search(self):
        pat=["http:","https:","<script>",".exe","html"]
        i=0
        while i<len(self.result):
            r=[] #to store particular row of result
            r=self.result[i]
            if r[2]!=1: #searches for pattern only when the link is not broken
                l=[]#to store patterns found in the child link/page,we use list because it may be one or more.
                for p in pat:
                    if BMSearch(r[1],p)!=-1:
                        l.append(p) #appends pattern found in the child link
            if l:
                self.result[i].append(l)    
            i=i+1
    def linkScanner(self):
        self.crawl()
        self.scan()
        self.pattern_search()
    def putResult(self):
        return self.result
        



