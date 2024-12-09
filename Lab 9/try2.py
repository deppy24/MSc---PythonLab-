from tkinter import *
class MyApp():

    def __init__ (self):
        self.root = Tk()
        self.root.geometry('300x150')
        self.windowTitle = 'Linux'
        self.root.title(self.windowTitle)
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        self.fml = Frame( self. root)
        self.fml.pack(side=LEFT, fill=BOTH)
        self.rvar = IntVar()
        self.rvar.set(1)
        self.rbl = Radiobutton(self.fml, text='Linux', variable=self.rvar , value=1, command=self.onClick)
        self.rbl.pack(anchor=W)
        self.rb2 = Radiobutton(self.fml, text='Windows', variable=self.rvar, value=2, command=self.onClick)
        self.rb2.pack(anchor=W)
        self.rb3 = Radiobutton(self.fml, text='OS Χ', variable=self.rvar, value=3, command=self.onClick)
        self.rb3.pack(anchor=W)
        self.fm2 = Frame(self.root)
        self.fm2.pack(fill=BOTH, expand=1)
        self.cνar = IntVar()
        self.cb = Checkbutton(self.fm2, text='Show O.S. ', variable=self. cνar, command=self. onClick)
        self.cb.select()
        self.cb.pack()    
    def onClick(self):
        if self.rvar.get() == 1:
            self.windowTitle = 'Linux'
        elif self.rvar.get() == 2:
            self.windowTitle = 'Windows'
        elif self.rvar.get() == 3 :
            self.windowTitle = 'OS Χ'
        if self.cνar.get() == 1:
            self.root.title(self.windowTitle)
        else:
            self.root.title(' ')
if __name__=='__main__':    app = MyApp()

