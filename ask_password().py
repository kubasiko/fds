'''
from tkinter import*

win=Tk()
win.title('BALL')
size=400
amount=8
step=size//amount
canvas=Canvas(bg='white',height=size,width=size)
for i in range(0,size,step):
    canvas.create_line((i,0),(i,size))
for l in range(0,size,step):
    canvas.create_line((0,l),(size,l))
for y in range (3):
    for x in range(4):
        x_real=(2*x+(y%2))*step
        y_real=y*step
        canvas.create_oval((x_real,y_real),(x_real+step),(y_real+step),fill='black')
        x_real=(2*x+((7-y)%2))*step
        y_real=(7-y)*step
        canvas.create_oval((x_real,y_real),(x_real+step),(y_real+step),fill='black')
canvas.pack()
win.mainloop()
'''

import tkinter as tk

def move_by_keys(event):
    info_coords=canvas.coords(oval)
    x=info_coords[0]
    y=info_coords[1]
    label.config(text=str(x)+' '+str(y))
    if event.keysym=='Up':
        canvas.move(oval,0,-20)
    elif event.keysym=='Down':
        canvas.move(oval,0,20)
    elif event.keysym=='Left':
        canvas.move(oval,-20,0)
    elif event.keysym=='Right':
        canvas.move(oval,20,0)
       
        
win=tk.Tk()
label=tk.Label(win,text='INGINIRIUM')
label.pack()
canvas=tk.Canvas(win,bg='#fff',width=700,height=700)
oval= canvas.create_oval((300,300),(400,400),fill='yellow')
canvas.pack()
win.bind('<KeyPress>',move_by_keys)
win.mainloop()   

