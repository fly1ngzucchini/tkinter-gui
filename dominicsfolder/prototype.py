//real fast change to commit
from tkinter import *

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

root = Tk()
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

bottom_frame = Frame()
bottom_frame.pack(side=BOTTOM, fill=Y)

while True:
    root.update()
    if 500 < x < 1000:
        color = 'green'
    else:
        color = 'red'
    x = x+1

    target_number = str(x)
    aim_number = str(x)

    target = Label(top_left_frame, fg=color, text='Target = ' + target_number)
    target.config(font=('Courier', 44))
    target.grid(row=0, column=0)

    aim = Label(top_right_frame, fg=color, text='Current = ' + aim_number)
    aim.config(font=('Courier', 44))
    aim.grid(row=0, column=0)

#main loop
root.mainloop()
