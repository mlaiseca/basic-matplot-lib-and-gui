#written by Mario Laiseca-Ruiz
#medical robotics

from Tkinter import *
import json

import numpy as np

from tkFileDialog import askopenfilename
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

someVAr = False
inputLoaded = False

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

variance1 = 0
variance2 = 0

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111) #one chart with 1x1 dimensions

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"
        global someVAr 
        someVAr = True

    

    def file_reader(self):
        print("set up function")    
        file_name = askopenfilename()  

        with open(file_name) as data_file:    
            data = json.load(data_file)

        global x1
        global y1
        global x2
        global y2
        x1 = [1,2,3,4,5,6,7,8,9,10]
        y1 = data['input1']
        x2 = x1
        y2 = data['input2']

        print (y1)
        print (y2)
    
        global inputLoaded
        inputLoaded = True
        self.display_graph()


    def display_graph(self):

        #a.clear()
        a.plot(x1,y1, label='Data 1')
        a.plot(x2,y2, label='Data 2')
        a.plot(x3,y3, label='Average')

        #plt.legend()
        #plt.show()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()           
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

        print(someVAr)

    def getAverage(self):
        print("average function")
        print(y1)
        print(y2)

        average = []

        counter = 0
        for num in y1:
            average.append(float(num + y2[counter])/2)
            counter+=1

        
        print(average)
        global x3
        global y3
        x3 = [1,2,3,4,5,6,7,8,9,10]
        y3 = average
        
        self.display_graph()


    def make_output_file(self):
        fo = open("output.txt", "w")

        #write to file
        fo.write("Name of the file: " + fo.name + "\n")
        fo.write("data set 1\n")
        for num in y1:
            fo.write(str(num) + "\n")

        fo.write("data set 2\n")
        for num in y2:
            fo.write(str(num) + "\n")

        fo.write("average of both data sets\n")
        for num in y3:
            fo.write(str(num) + "\n")


        fo.write("variance of data set 1" + "\n" + str(variance1) + "\n")
        fo.write("variance of data set 2" + "\n" + str(variance2) + "\n")
        
        #close file
        fo.close()        

    def getVariance(self):

        global variance1
        global variance2
        variance1 = np.var(y1)
        variance2 = np.var(y2)
        print (variance1)
        print (variance2)




    def createWidgets(self):


        button0 = Button(self, text="Quit", fg = "red", command= self.quit)
        button0.pack()

        button1 = Button(self, text="Load Input File", command= self.file_reader )
        button1.pack()

        button2 = Button(self, text="Get Average", command= self.getAverage)
        button2.pack()

        button3 = Button(self, text="Get Variance", command= self.getVariance)
        button3.pack()

        button4 = Button(self, text="Make output file", command= self.make_output_file)
        button4.pack()
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()