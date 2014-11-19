from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
grass = drawpad.create_rectangle(0,250,800,600, fill = "green")
road = drawpad.create_rectangle(0,350,800,500, fill = "gray")
water = drawpad.create_rectangle(0,250,800,0, fill = "blue")









































# Caden's part
    
    
    
    
    
    
    
    
    
    
    
    
class myApp(object):
    def __init__(self, parent):    
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()
        self.prompt = "Lives left :"
        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def animate(self):






































    def key(self,event):
        global player
        x1,y1,x2,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 > 0:
                drawpad.move(player,0,-10)
        if event.char == "s":
            if y2 < 600:
                drawpad.move(player,0,10)
        if event.char == "a":
            if x1 > 0:
                drawpad.move(player,-10,0)
        if event.char == "d":
            if x2 < 800:
                drawpad.move(player,10,0)
                
        
            
            





































































app = myApp(root)
root.mainloop()