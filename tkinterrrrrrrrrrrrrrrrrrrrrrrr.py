from tkinter import *

def keydrawing(x,y):
    global cur_y,cur_x,line
    new_x=cur_x+x
    new_y=cur_y+y
    if draw or None:
        line=canvas.create_line(cur_x,cur_y,new_x,new_y,width=3)
    else:
        canvas.coords(line,cur_x,cur_y,new_x,new_y)

    cur_x=new_x
    cur_y=new_y

def move_up(event):
    keydrawing(0,-5)

def move_down(event):
    keydrawing(0,5)

def move_left(event):
    keydrawing(-5,0)

def move_rigjt(event):
    keydrawing(5,0)

def pen_up(event):
    global draw
    draw=False

def pen_down(event):
    global draw
    draw=True
    
def new_canvas(event):
    global line,draw,cur_y,cur_x
    canvas.delete(ALL)
    cur_x=250
    cur_y=250
    draw=False
    line=None

cur_x=250
cur_y=250
draw=False
line=None

win=Tk()
win.title("keyboard drawing")

canvas=Canvas(win,width=500,height=500)
canvas.pack()

win.bind("<Up>",move_up)
win.bind("<Down>",move_down)
win.bind("<Left>",move_left)
win.bind("<Right>",move_rigjt)
win.bind("<u>",pen_up)
win.bind("<d>",pen_down)
win.bind("<c>",new_canvas)
win.mainloop()