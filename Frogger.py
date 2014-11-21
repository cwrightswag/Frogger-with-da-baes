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
# first row of logs
Log1 = drawpad.create_rectangle(0,50,80,90, fill = "brown")
Log2 = drawpad.create_rectangle(150,50,230,90, fill = "brown")
Log3 = drawpad.create_rectangle(300,50,380,90, fill = "brown")
Log4 = drawpad.create_rectangle(450,50,530,90, fill = "brown")
Log5 = drawpad.create_rectangle(600,50,680,90, fill = "brown")
#second row of logs
Log6 = drawpad.create_rectangle(0,150,80,190, fill = "brown")
Log7 = drawpad.create_rectangle(150,150,230,190, fill = "brown")
Log8 = drawpad.create_rectangle(300,150,380,190, fill = "brown")
Log9 = drawpad.create_rectangle(450,150,530,190, fill = "brown")
Log10= drawpad.create_rectangle(600,150,680,190, fill = "brown")
 























player = drawpad.create_oval(350,575,375,600, fill = "lightgreen")






























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
        global truck5
        global truck6
        global truck7
        global truck8
        global truck9
        global truck10
        global car1
        global car2
        global car3
        global car4
        global Log1
        global Log2
        global Log3
        global Log4
        global Log5
        global Log6
        global Log7
        global Log8
        global Log9
        global Log10
        px1,py1,px2,py2 = drawpad.coords(player)
        lp1x1, lp1y1, lp1x2, lp1y2 = drawpad.coords(lillypad1)
        lp2x1, lp2y1, lp2x2, lp2y2 = drawpad.coords(lillypad2)
        lp3x1, lp3y1, lp3x2, lp3y2 = drawpad.coords(lillypad3)































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
            drawpad.move(player,0,-80)        
        
            
            





































































app = myApp(root)

root.mainloop()