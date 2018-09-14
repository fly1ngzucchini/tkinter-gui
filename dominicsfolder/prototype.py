"""
todos::
learn how to get data from rasp pi into python
    (it's in C)
have camera feed displayed in bg of gui
    maybe w crosshair
streamline program
"""
import tkinter as tk
#from tkinter import *
from tkinter import Label
root = tk.Tk()

root.bind('<Escape>', lambda e: root.destroy())

#w = tk.Label(root, text="Hello world")
#w.pack() #tells tkinter to fit the size of the window to text

counter = 0
def count():
    global counter
    counter +=1

def counter_label_left(label):
    label.config(text = "target = " + str(counter))
    label.after(1, count)
    count()
def counter_label_right(label):
    label.config( text = "current = " + str(counter))
    label.after(1,count)
    count()
root.title("proto toto type")
label = tk.Label(root, fg="green")
label.pack(padx=50, side=tk.LEFT)
label = tk.Label(root, fg="green")
label.pack()
counter_label_left(label)


"""
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self._fullscreen = True
        master.bind('<Escape>', self.toggle_fullscreen)
    def toggle_fullscreen(self,event):
        fullscreen = self._fullscreen
        #print(fullscreen, self._fullscreen)
        self.master.attributes('-fullscreen', self._fullscreen)
        if fullscreen == True :
            self._fullscreen = False
        else:
            self._fullscreen = True


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
app = FullScreenApp(root)

#main window properties
root.title("Prototype")
#root.attributes('-fullscreen', True)
root.geometry("%dx%d+0+0" % (w/2, h/2))
root.state('zoomed')

#root.resizable(width=FALSE, height=FALSE)

x = 0


# data labels
top_frame = Frame()
top_frame.pack(side=TOP, fill=X)

top_right_frame = Frame(top_frame)
top_right_frame.pack(side=RIGHT)

top_left_frame = Frame(top_frame)
top_left_frame.pack(side=LEFT)

#bottom_frame = Frame()
#bottom_frame.pack(side=BOTTOM, fill=Y)

while True:
    root.update()
    if 500 < x < 1000:
        color = 'green'
    else:
        color = 'red'
    x = x+1

    target_number = str(x)
    aim_number = str(x)

    target = Label( fg=color, text='Target = ' + target_number)
    target.config(font=('Courier', 44))
    target.grid(row=0, column=0)
    #target.pack()

    aim = Label( fg=color, text='Current = ' + aim_number)
    aim.config(font=('Courier', 44))
    aim.grid(row=0, column=0)
    #aim.pack()
"""
#main loop
root.mainloop()
