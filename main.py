from tkinter import *
import time
import random
root = Tk()
root.geometry('800x600+120+10')
root.title('Roll Ball')

canvas=Canvas(root,width=800,height=600)
canvas.pack()
class RollBall:
    def __init__(self,color,size):
        self.ball=canvas.create_oval(10,10,size,size,fill=color)
        self.xspeed=random.randrange(1,8)
        self.yspeed=random.randrange(1,8)
    def Animate(self):
        canvas.move(self.ball,self.xspeed,self.yspeed)
        pos=canvas.coords(self.ball)
        if pos[3]>=600 or pos[1]<=0:
            self.yspeed=-self.yspeed
        if pos[2]>=800 or pos[0]<=0:
            self.xspeed=-self.xspeed
color=['red','orange','blue','green','black','gray','gold']
ball=[]
for i in range(100):
    ball.append(RollBall(random.choice(color),50))
while True:
    for j in ball:
        j.Animate()
    root.update()
    time.sleep(0.01)
root.mainloop()