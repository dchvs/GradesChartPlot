import os
import Tkinter
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


class Canvas():
    def __init__(self, root, data, nombres, ind, width):
        self.root = root
        self.data = data        
        self.nombres = nombres
        self.ind = ind
        self.width = width
        self.canvas()
        self.canvas = self.canvas()

    def canvas(self):
        f = Figure(figsize=(5,4), dpi=100)     
        ax = f.add_subplot(111)
        
        ax.set_xlabel("estudiantes")        
        ax.set_ylabel("notas")
        ax.set_xticks(self.ind+self.width/2)
        ax.set_xticklabels(self.nombres) #
        rects = ax.bar(self.ind, self.data, self.width)
        canvas = FigureCanvasTkAgg(f, master=root)#self.root)
        #canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas.show()
        return canvas



class Pages():
    def __init__(self, canvas):
        self.canvasS = canvas[0]
        self.canvasE = canvas[1]
        self.canvas_clase = canvas[2]
        #self.canvasS_clase = canvas[2]
        #self.canvasE_clase = canvas[3]

        self.back = back
        self.page0btn = Tk.Button(master=self.back, text="Inicio", command=self.page0)
        self.page1btn = Tk.Button(master=self.back, text="Notas por estudiante", command=self.page1)
        self.page1btn_clase = Tk.Button(master=self.back, text="Notas por clase", command=self.page1_clase)

        self.page2btnE = Tk.Button(master=self.back, text="Español", command=self.pageE)
        self.page2btnS = Tk.Button(master=self.back, text="Sociales", command=self.pageS)

        #self.page2btnE_clase = Tk.Button(master=self.back, text="Español", command=self.pageE_clase)
        #self.page2btnS_clase = Tk.Button(master=self.back, text="Sociales", command=self.pageS_clase)

    def page0(self):           # inicio
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        ##self.canvasS_clase.get_tk_widget().pack_forget()
        ##self.canvasE_clase.get_tk_widget().pack_forget()
        self.page0btn.pack_forget()
        self.page2btnE.pack_forget()
        self.page2btnS.pack_forget()
        ##self.page2btnE_clase.pack_forget()
        ##self.page2btnS_clase.pack_forget()          

        self.back.pack()
        root.title("Graficar notas")
        self.page1btn.pack(fill=Tk.BOTH, expand=1)
        self.page1btn_clase.pack(fill=Tk.BOTH, expand=1)

    def page1(self):          # notas por estudiante 
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        ##self.canvasS_clase.get_tk_widget().pack_forget()
        ##self.canvasE_clase.get_tk_widget().pack_forget()        
        #self.page0btn.pack_forget()
        self.page1btn.pack_forget()
        self.page1btn_clase.pack_forget()

        self.back.pack()
        root.title("Notas por estudiante")
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
        self.page2btnE.pack(fill=Tk.BOTH, expand=1)  # plot boton de notas de español 
        self.page2btnS.pack(fill=Tk.BOTH, expand=1)  # plot boton de notas de sociales 

    def page1_clase(self):    # notas por clase        
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        ##self.canvasS_clase.get_tk_widget().pack_forget()
        ##self.canvasE_clase.get_tk_widget().pack_forget()        
        #self.page0btn.pack_forget()        
        self.page1btn.pack_forget()
        self.page1btn_clase.pack_forget()

        self.back.pack()
        root.title("Notas por clase")
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
        self.canvas_clase.get_tk_widget().pack(fill=Tk.BOTH, expand=1) 
        ##self.page2btnE_clase.pack(fill=Tk.BOTH, expand=1)  # plot de notas de español 
        ##self.page2btnS_clase.pack(fill=Tk.BOTH, expand=1)  # plot de notas de sociales 

        
    def pageE(self):        
        self.page1btn.pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvas_clase.get_tk_widget().pack_forget()
        ##self.canvasS_clase.get_tk_widget().pack_forget()
        ##self.canvasE_clase.get_tk_widget().pack_forget()        

        self.back.pack()
        root.title("Notas de español promediadas por estudiante")
        self.canvasE.get_tk_widget().pack(fill=Tk.BOTH, expand=1)       
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
    def pageS(self):        
        self.page1btn.pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        self.canvas_clase.get_tk_widget().pack_forget()
        ##self.canvasS_clase.get_tk_widget().pack_forget()
        ##self.canvasE_clase.get_tk_widget().pack_forget()        

        self.back.pack()
        root.title("Notas de Sociales promediadas por estudiante")
        self.canvasS.get_tk_widget().pack(fill=Tk.BOTH, expand=1)       
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
"""
    def pageE_clase(self):
        self.page1btn_clase.pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()        
        self.canvasS_clase.get_tk_widget().pack_forget()

        self.back.pack()
        root.title("Notas de español promediadas por clase")
        self.canvasE_clase.get_tk_widget().pack(fill=Tk.BOTH, expand=1)       
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
        
    def pageS_clase(self):        
        self.page1btn_clase.pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()        
        self.canvasE_clase.get_tk_widget().pack_forget()

        self.back.pack()
        root.title("Notas de Sociales promediadas por clase")
        self.canvasS_clase.get_tk_widget().pack(fill=Tk.BOTH, expand=1)       
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
"""


i = 0
a = []
data = []
nombres = []
f = open('data.txt', 'r')
for line in f.readlines():
    a = line.split()    
    nombres += [a[0]]
    data += [a[1:]]
    i += 1 


print(str(data[0]))   
# parametros y datos

clase= ['Sociales', 'Espa_ol', 'Matemanticas']
ind = numpy.arange(len(data))  # the x locations for the groups
width = .5

# ventana
root = Tk.Tk()
back = Tk.Frame(master=root, width=500, height=500, bg='black')


# graficos de barras
canvasS = Canvas(root, data, nombres, ind, width).canvas
canvasE = Canvas(root, data2, nombres, ind, width).canvas
canvas_clase = canvasS = Canvas(root, data3, clase, ind, width).canvas
 

canvas = [canvasS, canvasE, canvas_clase] 
pages = Pages(canvas)

# pagina de inicio
pages.page0()


Tk.mainloop()

