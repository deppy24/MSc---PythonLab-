from tkinter import *
class MyApp:
    def __init__(self):
        self.root = Tk()
        self.fm = Frame(self.root, width=200, height=100)
        self.fm.bind('<Button-1>', self.onLeftClick)
        self.fm.bind('<Enter>', self.onMouseEnter)
        self.fm.bind('<Key>', self.onKeyPress)
        self.fm.pack()
        self.fm.focus_set()
        self.root.mainloop()
    def onLeftClick(self, event):
        print('Left click at: ', event.x, event.y)
    def onMouseEnter(self, event):
        print('Hello mouse')
    def onKeyPress(self, event):
        print ( 'Key pressed: ', event. keysym, event. keycode)
if __name__=='__main__':
    app = MyApp()
