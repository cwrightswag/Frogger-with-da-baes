from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
grass = drawpad.create_rectangle(0,250,800,600, fill = "green")
road = drawpad.create_rectangle(0,350,800,500, fill = "gray")
water = drawpad.create_rectangle(0,250,800,0, fill = "blue")


root.mainloop()