from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
grass = drawpad.create_rectangle(0,250,800,600, fill = "green")
road = drawpad.create_rectangle(0,350,800,500, fill = "gray")
water = drawpad.create_rectangle(0,250,800,0, fill = "blue")
lillypad1 = drawpad.create_rectangle(70,0,110,30,  fill = "DarkGreen")
lillypad2 = drawpad.create_rectangle(180,0,220,30, fill = "DarkGreen")
lillypad3 = drawpad.create_rectangle(270,0,310,30, fill = "DarkGreen")
lillypad4 = drawpad.create_rectangle(390,0,430,30, fill = "DarkGreen")
lillypad5 = drawpad.create_rectangle(500,0,540,30, fill = "DarkGreen")
lillypad6 = drawpad.create_rectangle(610,0,650,30, fill = "DarkGreen")
lillypad7 = drawpad.create_rectangle(720,0,760,30, fill = "DarkGreen")
truck1 = drawpad.create_rectangle(0,450,60,480, fill = "yellow")
truck2 = drawpad.create_rectangle(150,450,210,480, fill = "purple")
truck3 = drawpad.create_rectangle(300,450,360,480, fill = "yellow")
truck4 = drawpad.create_rectangle(450,450,510,480, fill = "yellow")
truck5 = drawpad.create_rectangle(600,450,660,480, fill = "purple")
truck6 = drawpad.create_rectangle(200,350,260,380, fill = "blue")
truck7 = drawpad.create_rectangle(350,350,410,380, fill = "red")
truck8 = drawpad.create_rectangle(500,350,560,380, fill = "black")
truck9 = drawpad.create_rectangle(650,350,710,380, fill = "black")
truck10= drawpad.create_rectangle(20,350,80,380, fill = "blue")
car1 = drawpad.create_rectangle(40,400,80,430, fill = "red")
car2 = drawpad.create_rectangle(240,400,280,430, fill = "blue")
car3 = drawpad.create_rectangle(440,400,480,430, fill = "forestgreen")
car4 = drawpad.create_rectangle(640,400,680,430, fill = "red")









player = drawpad.create_oval(350,575,375,600, fill = "lightgreen")






























# Caden's part
    
    
    
    
    
    
    
    
    
    
    
    
class myApp(object):
    def __init__(self, parent):    
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()
        self.prompt = "Lives Left:"
        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        





































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
                
        
            
            






































































root.mainloop()