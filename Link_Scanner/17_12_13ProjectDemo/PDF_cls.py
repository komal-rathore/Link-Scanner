from fpdf import FPDF
from depth_class import *
from LinkExtractor.add_to_result import add_to_index
import time

class PDF(FPDF):
        def __init__(self,result,exetime,clocktime):
                self.result=result
                self.ExeTime=exetime
                self.Processortime=clocktime

        def header(self):
                #Arial bold 15
                self.set_font('Arial','U',20)
                #Calculate width of title and position
                w=self.get_string_width(title)+6
                self.set_x((210-w)/2)
                #Colors of frame, background and text
                #self.set_draw_color(0,80,180)
                self.set_fill_color(255,255,255)
                self.set_text_color(0,0,255)
                #Thickness of frame (1 mm)
                #self.set_line_width(1)
                #Title
                self.cell(w,9,title,0,0,'C',0)
                #Line break
                self.ln(10)
                self.chapter_dateTime()
		self.chapter_heading()
		#self.cell(30,10,'Link Scan Report')
                self.ln(10)
                #print line in the header
                self.print_line('____________')
                self.ln(10)
        def footer(self):
                #Position at 1.5 cm from bottom
                self.set_y(-15)
                #Arial italic 8
                self.set_font('Arial','I',8)
                #Text color in gray
                self.set_text_color(128)
                #Page number
                self.cell(0,10,'Page '+str(self.page_no()),0,0,'C')

        def chapter_title(self,num,label):
                #Arial 12
                self.set_font('Arial','B',10)
                #Background color
                #self.set_fill_color(200,220,255)
                #Title
		
                self.cell(0,6,"%d. %s"%(num,label))
                #Line break
                self.ln(4)
        def chapter_dateTime(self):
                #Arial 12
                self.set_font('Arial','B',8)
                #Background color
                #self.set_fill_color(200,220,255)
                #Title
		self.set_text_color(0,0,0)
                self.cell(10,10,time.strftime("%d/%m/%Y")) # for date
		self.ln(5)
                self.cell(10,10,time.strftime("%I:%M:%S %p")) # for time %p for am/pm 12 hr
		self.ln(5)
                #Line break
                self.ln(4)
        def print_line(self,ch):
                self.set_font('Arial','U',8)
                for i in range(20):
                     self.cell(10,10,str(ch))    
        def chapter_heading(self):
		heading = "Link Scan Report"
                #Arial bold 15
                self.set_font('Arial','U',15)
                #Calculate width of title and position
                w=self.get_string_width(heading)+6
                self.set_x((210-w)/2)
                #Colors of frame, background and text
                #self.set_draw_color(0,80,180)
                #self.set_fill_color(230,230,0)
                self.set_text_color(0,0,0)
                #Thickness of frame (1 mm)
                #self.set_line_width(1)
                #Title
                self.cell(w,9,heading)

        def chapter_body(self):
		self.chapter_title(1,"Malicious Pattern Found:")
		self.display_malicious_pattern(self.result)
		self.ln(10)
                self.chapter_title(2,"Broken Links Found:")
                self.display_dangling(self.result)
		self.ln(10)
                self.chapter_title(3,"Complete List of Dangling/broken Links and Patterns:")
		self.complete_list(self.result)
                self.ln(20)
                self.chapter_title(4,"Performance Details:")
		self.display_performance()
                '''                
		#Read text file
                txt=file(name).read()
                #Times 12
                self.set_font('Times','',12)
                #Output justified text
                self.multi_cell(0,5,txt)
                #Line break
                self.ln()
                #Mention in italics
                self.set_font('','I')
                self.cell(0,5,'(end of excerpt)')
		'''

        '''def print_chapter(self,num,title,name):
                self.add_page()
                self.chapter_title(num,title)
                self.chapter_body(name)
        '''
	def complete_list(self,lists):
	    self.ln(10)
            self.set_font('Arial','',10)
            self.cell(12,12,"Parent page                  Child page                    Dangling/Broken Links      Patterns found in Child Page")
            self.ln(10) 
            for i in lists:
                con = ""
	        for j in i :
		    con = con + "    " + str(j)
                self.cell(12, 10, con)
	        self.ln(10)   
       	def display_malicious_pattern(self,result):
            pat=["html","sk","http:"]
            self.set_font('Arial','',10)
            link_list=[]
            for p in pat:
                for r in result:
		    if p in r[3]:
                        add_to_index(link_list,p,r[1])

	    print "/////////////////////////////////////////////////////////////////////"
            print link_list
	    print "////////////////////////////////////////////////////////////////////"
            self.cell(12,12,"    Pattern                  Pattern found in links         " )
            self.ln(10)
	    for i in link_list:
                self.cell(12,10,str(i[0]))
                self.ln(10)
	        for j in i[1] :
		    con = "    " + str(j)
                    self.cell(12, 10, con)
	            self.ln(10)   
        def display_dangling(self,result):
            self.ln(10)
            self.set_font('Arial','',10)
            self.cell(12,12,"Child page                                             Parent page")
            self.ln(10)
            
                       
            for r in result:
		x=[]
		x=r
		if 1 in x:
                    self.cell(15,15,str(x[1] + "                                            "+x[0]))
                    #self.cell(15,15,str("     "+ x[0]))
                    self.ln(10)
            
        def display_performance(self):
            self.ln(10)
            self.set_font('Arial','',10)
            self.cell(10,10,"   Execution time  : ")
            self.ln(10) 
            self.cell(10,10,str(self.ExeTime))
            self.ln(10)
            self.cell(10,10," Clock time :")
            self.ln(10)
            self.cell(10,10,str(self.Processortime))
		

        def print_chapter(self):
                self.add_page()

                self.chapter_body()
def Start_Scan():
    title='Link Scanner -- Finding Broken links and Patterns'
    start_time = time.time()
    start_clock=time.clock()
    l=linkScan("http://localhost/DepthTest2/A.html",4)
    l.linkScanner()
    ExeTime= time.time() - start_time,"seconds"
    Processortime=time.clock()-start_clock,"seconds"
    print l.result
    pdf=PDF(l.result,ExeTime,Processortime)
    pdf.set_title(title)
    pdf.set_author('Jules Verne')
    #pdf.print_chapter(1,'A RUNAWAY REEF','20k_c1.txt')
    #pdf.print_chapter(2,'THE PROS AND CONS','20k_c2.txt')
    pdf.print_chapter()
    pdf.output('tuto3.pdf','F')
Start_Scan()
