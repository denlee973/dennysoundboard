
import tkinter as tk
import tkinter.font as tkFont
from playsound import playsound
from PIL import ImageTk, Image
import os
import sys
from abc import ABCMeta, abstractmethod

class Master:
    __metaclass__ = ABCMeta
    text = []

    def __init__(self):
        self.csfont = tkFont.Font(family="Comic Sans MS", size=24)
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=12)
    
    # creates a new window
    # @param: windname(window name):class, *args
    # @return: none
    # def newPage(self,windname,*args):
    #     self.window.withdraw()
    #     self.window = windname(tk.Toplevel(self.window),*args)

    
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

class Board(Master):

    def make_button(self,blist,x,y,img):
        btext = self.soundnames[x][y]
        if (img):
            photo = ImageTk.PhotoImage(Image.open(self.resource_path("images/"+btext+".jpg")).resize((350,350)))
            self.soundbutton = tk.Button(window, text=btext, image=photo, command= lambda sn=self.resource_path("sounds/"+btext+'.mp3'): playsound(sn, False), height=350, width=350)
            self.soundbutton.image = photo
        else:
            self.soundbutton = tk.Button(window, text=btext, command= lambda sn=self.resource_path("sounds/"+btext+'.mp3'): playsound(sn, False), height=5, width=15)
            self.soundbutton['font'] = self.csfont
        blist.append(self.soundbutton)
        self.soundbutton.grid(column=y, row=x)
        return blist

    def __init__(self,window):
        Master.__init__(self)
        self.window = window
        window.title("A Denny Soundboard")

        # self.menubar = tk.Menu(window)
        # self.filemenu = tk.Menu(self.menubar, tearoff=False)
        # self.viewmenu = tk.Menu(self.menubar, tearoff=False)
        # self.helpmenu = tk.Menu(self.menubar, tearoff=False)

        self.soundnames = [['hmm','lol','huh'],['gn','yawn','zzz'],['waitasec','henlo','ono']]

        self.blist = []
        for i in range(len(self.soundnames)):
            for j in range(len(self.soundnames[i])):
                self.blist = self.make_button(self.blist,i,j,True)


window = tk.Tk()
home = Board(window)
window.mainloop()
print ("program exited.")