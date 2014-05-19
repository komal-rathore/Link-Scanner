from Tkinter import *
from depth_class import *
import time

class Application(Frame):
    def say_hi(self):
        print "call here fuction of search"

    def createWidgets(self):
        self.label1 = Label( self, text="Enter URL")
        self.E1 = Entry(self, bd =5)
        self.label1.pack()
        self.E1.pack()
        self.submit = Button(self, text ="Submit", command =self.start)
        self.submit.pack(side =BOTTOM)
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "Black"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Report"
        self.hi_there["command"] = self.show_report

        self.hi_there.pack({"side": "left"})
        self.l1=Label(self,text="Parent",borderwidth=5)
        self.l2=Label(self,text="Child",borderwidth=5)
        self.l3=Label(self,text="Dangling",borderwidth=5)
        self.l4=Label(self,text="Pattern",borderwidth=5)
        self.l5=Label(self)
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()
        self.l4.pack()
        self.l5.pack()
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def show_report(self):
        
        i=0
     
        while i<len(self.__l.result):
            r=[]
            r=self.__l.result[i]
            for x in range(len(r)):
                self.l5["text"]=r[x]
            self.l5.pack()
        i=i+1
        print pattern_list
        
        
    def start(self):
        url = self.E1.get()
        self.__l=linkScan(url,4)
        self.__l.linkScanner()
        
        
    '''
    def getURL(self):
        url = self.E1.get()
        start_time = time.time()
	start_clock=time.clock()
	#block = "This is a simple example"
	#print "This is an example search on the string \"", block, "\"."
	#l=["ple","example","simple"," imple"]
	pat=["http:","https:","<script>",".exe"]
	#for i in l:
	#	print i,"  :", BMSearch(block, i)
	L2 = get_all_links(get_page(url))
	index=[] # to store the links which contains the pattern
	broken = [] # to store the links which are broken
	for r in L2:
	    for p in pat:
		print r,": ",BMSearch(r,p)
		if BMSearch(r,p)!=-1:
		     add_to_index(index,p,r)
	for br in L2:
	    lc = LinkChecker(br)
	    if lc.check():
   		 print "Check is sussessful"
   		 if not lc.follow():
       		 	print("there were problems")
       		 	print("\n".join(lc.failed))
        		print("\n".join(lc.other))
    		 else:
        		print("website OK")
	    else:
		 broken.append(br)
    		 print("cannot open website or homepage is not html")
		
	print "----------------------------------------------------------------------------"	
	print index
	print"-----------------------------------------------------------------------------"
	print pprint(index)
	print "CPU Time:"
	print time.clock()-start_clock, "seconds"
	print "Execution Time:"
	print time.time() - start_time, "seconds"
	print "broken links:"
	print broken
	return url
    '''
    
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
#http://www.ittc.ku.edu/~niehaus/classes/448-s04/448-standard/simple_gui_examples/
