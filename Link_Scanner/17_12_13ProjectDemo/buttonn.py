from Tkinter import *
import ttk
import subprocess
class Application(Frame):
    def say_hi(self):
        print "call here fuction of search"

    def createWidgets(self):
        self.f = Frame(self, height=30, width=42)
        self.f.pack_propagate(0) # don't shrink
        self.f.pack()

        self.label1 = Label( self, text="Enter URL")
        self.E1 = Entry(self, bd =5)
        self.label1.pack()
        self.E1.pack()
        self.submit = Button(self, text ="Submit", command =self.getURL)
        self.submit.pack(side =BOTTOM)
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "Black"
        self.QUIT["command"] =  self.viewReport
        
        self.QUIT["state"]=DISABLED
        

        self.hi_there = Button(self)
        self.hi_there["text"] = "start",
        self.hi_there["command"] = self.say_hi
        
        self.QUIT.pack({"side": "left"})
        self.hi_there.pack({"side": "left"})
        self.pb = ttk.Progressbar(self,orient ="horizontal",length = 200, mode ="determinate")
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def getURL(self):
        self.pb.pack()
        self.pb.start()
        print self.E1.get()
        i=0
        self.QUIT["state"]=DISABLED
        while True:
            
            self.QUIT["state"]=DISABLED
            print i
            i=i+1
            
            if i >1000:
                break
        self.pb.stop()

            
        self.QUIT["state"]=NORMAL
        self.QUIT.pack({"side": "left"})
    def viewReport(self):
        import platform
        if platform.system() =='Windows':
            pdf = "E:\Books\IMpORtant-komal_2013\2611ProjectDemo\17_12_13ProjectDemo\tuto3.pdf"
            acrobatPath = r'C:\Program Files\Adobe\Reader 8.0\Reader\AcroRd32.exe'
            subprocess.Popen("%s %s" % (acrobatPath, pdf))
        if platform.system() =='Linux':
            pdf = "C:\Documents and Settings\Administrator\Desktop\MMW_BM_report.pdf"
            acrobatPath = r'C:\Program Files\Adobe\Reader 8.0\Reader\AcroRd32.exe'
            subprocess.Popen("%s %s" % (acrobatPath, pdf))
        
    
        

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
#http://www.ittc.ku.edu/~niehaus/classes/448-s04/448-standard/simple_gui_examples/
