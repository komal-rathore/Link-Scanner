import Tkinter
from depth_class import *
def show_report(result):
    root = Tkinter.Tk(  )
    i=0
    Tkinter.Label(root,text="Parent",borderwidth=5).grid(row=0,column=0)
    Tkinter.Label(root,text="Child",borderwidth=5).grid(row=0,column=1)
    Tkinter.Label(root,text="Dangling",borderwidth=5).grid(row=0,column=2)
    Tkinter.Label(root,text="Pattern",borderwidth=5).grid(row=0,column=3)
    while i<len(result):
        r=[]
        r=result[i]
        for x in range(len(r)):
            Tkinter.Label(root,text=r[x],borderwidth=5).grid(row=i+1,column=x)
        i=i+1
    root.mainloop( )
def display_dangling(result):
    root = Tkinter.Tk(  )
    i=0
    dl=[]
    while i<len(result):
        r=[]
        r=result[i]
        if r[2]==1:
            dl.append(r[1])
        i=i+1
    print "dangling links:*******************************************************"
    for x in range(len(dl)):
        Tkinter.Label(root,text=dl[x],borderwidth=5).grid(row=x,column=x)
    root.mainloop( )
   
l=linkScan("http://localhost/DepthTest2/A.html",4)
l.linkScanner()
show_report(l.result)
