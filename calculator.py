import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height = 410, width = 310, bg = 'black')
canvas.pack()

number_frame = tk.Frame(root, bg = 'red')
number_frame.place(relwidth = .98, relheight = .15, relx = .01, rely = .01)

root.mainloop()
