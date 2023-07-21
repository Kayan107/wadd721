from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='black',height=250,width=300)

canvas.create_rectangle(50, 60, 220, 160, fill='red',
                        outline='blue')

canvas.create_text(100, 100, text='KayanWong',
                   anchor='nw',font='TkMenuFont',fill='white')

canvas.create_line(100, 115, 165, 115)
canvas.pack()
frame.mainloop()
