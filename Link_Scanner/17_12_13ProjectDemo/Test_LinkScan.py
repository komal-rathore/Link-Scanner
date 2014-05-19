from depth_class import *
import Tkinter
start_time = time.time()
start_clock=time.clock()
l=linkScan("http://localhost/DepthTest2/A.html",4)
l.linkScanner()
print time.time() - start_time
print time.clock()-start_clock, " Processors time in seconds"
    

import Tkinter
root = Tkinter.Tk(  )
print l.result
i=0


while len(l.result):
    r=[]
    r=l.result[i]
    for c in range(len(r)):
        Tkinter.Label(root, text=(r[i],c),borderwidth=5 ).grid(row=r,column=c)
root.mainloop(  )
