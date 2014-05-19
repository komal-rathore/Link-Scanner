#from PDF import *
from Tkinter import *
#from boyerMoore import *
#from linkchecker.linkcheck import * 
#from GetPage import get_page
#from Get_all_links import get_all_links
#from add_to_result import add_to_index
#from pprint import pprint
import time
url=[]
class Application(Frame):
    def say_hi(self):
        print "call here fuction of search"

    def createWidgets(self):
        self.label1 = Label( self, text="Enter URL")
        self.E1 = Entry(self, bd =5)
        self.label1.pack()
        self.E1.pack()
        self.submit = Button(self, text ="Start Scan", command =self.getURL)
        self.submit.pack(side =LEFT)
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "Black"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "right"})

        #self.hi_there = Button(self)
        #self.hi_there["text"] = "start",
        #self.hi_there["command"] = self.say_hi

        #self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def getURL(self):
	global url
        url = self.E1.get()
      
	from PDF import *
	return url
def Tkgui():
    
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
    #http://www.ittc.ku.edu/~niehaus/classes/448-s04/448-standard/simple_gui_examples/

