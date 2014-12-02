from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
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
car1 = drawpad.create_rectangle(40,400,80,430, fill = "red")
# first row of logs
Log4 = drawpad.create_rectangle(450,70,530,30, fill = "brown")
Log5 = drawpad.create_rectangle(600,70,680,30, fill = "brown")
#second row of logs
Log8 = drawpad.create_rectangle(300,150,380,190, fill = "brown")
Log9 = drawpad.create_rectangle(450,150,530,190, fill = "brown")
Log10= drawpad.create_rectangle(600,150,680,190, fill = "brown")
 

player = drawpad.create_oval(350,575,375,600, fill = "lightgreen")











collisionlist = [truck1,truck2,truck3,truck4,car1,Log4,Log5,Log8,Log9,Log10,lillypad1,lillypad2,lillypad3,lillypad4,lillypad5,lillypad6,lillypad7,water,player]

animation = [truck1,truck2,truck3,truck4,car1,Log4,Log5,Log8,Log9,Log10,lillypad1,lillypad2,lillypad3,lillypad4,lillypad5,lillypad6,lillypad7,water,player]






































# Caden's part
    
    
    
    
    
    
    
    
    
    
    
    
class myApp(object):
    def __init__(self, parent):    
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.label1 = Label(root, text="Lives Left", bg='green')
        self.label1.pack()
        self.prompt = "Lives Left:"
        self.lives = 3
        
        self.livesTxt = Label(root, text=str(self.lives), width=len(str(self.lives)), bg='red')
        self.livesTxt.pack()
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

    def animate(self): 
        global player
        global lillypad1
        global lillypad2
        global lillypad3
        global lillypad4
        global lillypad5
        global lillypad6
        global lillypad7
        global truck1
        global truck2
        global truck3
        global truck4
        global car1
        global car2
        global car3
        global car4
        global Log4
        global Log5
        global Log8
        global Log9
        global Log10
        px1,py1,px2,py2 = drawpad.coords(player)
        lp1x1, lp1y1, lp1x2, lp1y2 = drawpad.coords(lillypad1)
        lp2x1, lp2y1, lp2x2, lp2y2 = drawpad.coords(lillypad2)
        lp3x1, lp3y1, lp3x2, lp3y2 = drawpad.coords(lillypad3)
        lp4x1, lp4y1, lp4x2, lp4y2 = drawpad.coords(lillypad4)
        lp5x1, lp5y1, lp5x2, lp5y2 = drawpad.coords(lillypad5)
        lp6x1, lp6y1, lp6x2, lp6y2 = drawpad.coords(lillypad6)
        lp7x1, lp7y1, lp7x2, lp7y2 = drawpad.coords(lillypad7)
        t1x1, t1y1, t1x2, t1y2 = drawpad.coords(truck1)
        t2x1, t2y1, t2x2, t2y2 = drawpad.coords(truck2)
        t3x1, t3y1, t3x2, t3y2 = drawpad.coords(truck3)
        t4x1, t4y1, t4x2, t4y2 = drawpad.coords(truck4)
        c1x1, c1y1, c1x2, c1y2 = drawpad.coords(car1)
        l4x1, l4y1, l4x2, l4y2 = drawpad.coords(log4)
        l5x1, l5y1, l5x2, l5y2 = drawpad.coords(log5)
        l8x1, l8y1, l8x2, l8y2 = drawpad.coords(log8)
        l9x1, l9y1, l9x2, l9y2 = drawpad.coords(log9)
        l10x1, l10y1, l10x2, l10y2 = drawpad.coords(log10)
        
        
        drawpad.move(truck1, 5, 0)
        if t1x2 > 800:
            drawpad.move(truck1,-800,0)
        
        drawpad.move(truck2, 6, 0)
        if t2x2 > 800:
            drawpad.move(truck2, -800,0)
        
        drawpad.move(truck3, -5, 0)
        if t3x1 < 0:
            drawpad.move(truck3, 800,0)
        
        
        drawpad.move(truck4, 5, 0)
        if t4x2 > 800:
            drawpad.move(truck4, -800,0)
        
        
        
        
        drawpad.move(log4, -3, 0)
        
        
        drawpad.move(log5, 3 ,0)
        
        
        drawpad.move(log8, 3, 0)
        
        
        drawpad.move(log9, -3, 0)
        
        
        drawpad.move(log10, 3, 0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        drawpad.after(1, self.animate)



























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
        if event.char == " ":
            if y1 > 0:
                drawpad.move(player,0,-80)        
        
            
            





































































app = myApp(root)

root.mainloop()