import tkinter as tk

win=tk.Tk()
canvas=tk.Canvas(bg='blue',width=700,height=700)
canvas.create_polygon(125,350,175,350,225,425,275,350,325,350,)
canvas.pack()
win.mainloop()