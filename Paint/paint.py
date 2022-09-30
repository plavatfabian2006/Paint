
from tkinter import *
from email.mime import image
from fileinput import filename
import tkinter
from tkinter import ttk
import tkinter as tk
from numpy import spacing
import pygame 
import time

 
colorrrr = "white"
root = Tk()
root.title("Paint Application")
root.geometry("1920x1080")
root.attributes('-fullscreen', True)
wn=Canvas(root, width=1420, height=780, bg='white')
paintok=0
color="black"
DIMENSION=100

def line1(event):
    global positions,paintok
    ok=0
    global x1,x2,y1,y2
    x1=event.x
    y1=event.y
    positions.append(x1)
    positions.append(y1)
    wn.create_polygon(positions[0]+DIMENSION/50,positions[1]+DIMENSION/50,positions[0]-DIMENSION/50,positions[1]-DIMENSION/50,positions[-4]-DIMENSION/50,positions[-3]-DIMENSION/50,positions[-4]+DIMENSION/50,positions[-3]+DIMENSION/50,fill="white",outline="white")
    wn.create_polygon(positions[0]+DIMENSION/50,positions[1]+DIMENSION/50,positions[0]-DIMENSION/50,positions[1]-+DIMENSION/50,positions[-2]-DIMENSION/50,positions[-1]-DIMENSION/50,positions[-2]+DIMENSION/50,positions[-1]+DIMENSION/50,fill=color,outline=color)
    paintok=4

def line(event):
    global positions
    ok=0
    global x1,x2,y1,y2
    x1=event.x
    y1=event.y
    positions.append(x1)
    positions.append(y1)
    if ok==0:
        ok=1
        wn.bind('<B1-Motion>', line1)
    

def paint(event):
    global x1,x2,y1,y2,paintok
    x1, y1 = (event.x-DIMENSION/25*3), (event.y-DIMENSION/25*3)
    x2, y2 = (event.x+DIMENSION/25*3), (event.y+DIMENSION/25*3)
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    paintok=1

def circle(event):
    global x1,x2,y1,y2,paintok
    x1, y1 = (event.x-DIMENSION), (event.y-DIMENSION)
    x2, y2 = (event.x+DIMENSION), (event.y+DIMENSION)

    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    paintok=1

def radiera(event):
    global x1,x2,y1,y2
    x1, y1 = (event.x-DIMENSION/25*3), (event.y-DIMENSION/25*3)
    x2, y2 = (event.x+DIMENSION/25*3), (event.y+DIMENSION/25*3)
    color = "white"
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def ractangle(event):
    global x1,x2,y1,y2,paintok
    x1, y1 = (event.x-DIMENSION*2), (event.y-DIMENSION)
    x2, y2 = (event.x+DIMENSION*2), (event.y+DIMENSION)
    wn.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    paintok=2

def square(event):
    global x1,x2,y1,y2,paintok
    x1, y1 = (event.x-DIMENSION), (event.y-DIMENSION)
    x2, y2 = (event.x+DIMENSION), (event.y+DIMENSION)
    wn.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    paintok=2

def triangle(event):
    global x1,x2,y1,y2,x3,y3,paintok
    x1, y1 = (event.x-DIMENSION), (event.y)
    x2, y2 = (event.x+DIMENSION), (event.y)
    x3, y3 = (event.x), (event.y-DIMENSION)
    wn.create_polygon(x1, y1, x2, y2,x3,y3, fill=color, outline=color)
    paintok=3

def trianglepress():
    T["state"] = DISABLED
    P["state"] = NORMAL 
    H["state"] = NORMAL
    PL["state"] = NORMAL 
    SQUARE["state"] = NORMAL
    F["state"] = NORMAL
    RADIERA["state"] = NORMAL
    wn.bind('<B1-Motion>', triangle)

def paintpress():
    P["state"] = DISABLED
    T["state"] = NORMAL 
    PL["state"] = NORMAL 
    H["state"] = NORMAL
    SQUARE["state"] = NORMAL
    F["state"] = NORMAL
    RADIERA["state"] = NORMAL
    wn.bind('<B1-Motion>', paint)

def circlepress():
    H["state"] = DISABLED 
    P["state"] = NORMAL 
    PL["state"] = NORMAL 
    F["state"] = NORMAL
    T["state"] = NORMAL
    SQUARE["state"] = NORMAL
    RADIERA["state"] = NORMAL
    wn.bind('<B1-Motion>', circle)
    
def radierapress():
    H["state"] = NORMAL 
    P["state"] = NORMAL
    F["state"] = NORMAL
    PL["state"] = NORMAL
    T["state"] = NORMAL
    SQUARE["state"] = NORMAL
    RADIERA["state"] = DISABLED
    wn.bind('<B1-Motion>', radiera)

def ractanglepress():
    H["state"] = NORMAL 
    P["state"] = NORMAL
    T["state"] = NORMAL
    SQUARE["state"] = NORMAL
    PL["state"] = NORMAL
    F["state"] = DISABLED
    RADIERA["state"] = NORMAL
    wn.bind('<B1-Motion>', ractangle)

def squarepress():
    H["state"] = NORMAL 
    T["state"] = NORMAL
    P["state"] = NORMAL
    PL["state"] = NORMAL
    SQUARE["state"] = DISABLED
    RADIERA["state"] = NORMAL
    F["state"] = NORMAL
    wn.bind('<B1-Motion>', square)

def linepress():
    global positions
    positions=[]
    H["state"] = NORMAL 
    T["state"] = NORMAL
    P["state"] = NORMAL
    PL["state"] = DISABLED
    SQUARE["state"] = NORMAL
    RADIERA["state"] = NORMAL
    F["state"] = NORMAL
    wn.bind('<B1-Motion>', line)
    
   

def black():
    global color
    color="black"
    BLACK["state"] = DISABLED
    RED["state"] = NORMAL
    ORANGE["state"] = NORMAL
    YELLOW["state"] = NORMAL
    GREEN["state"] = NORMAL
    BLUE["state"] = NORMAL

def back():
    if paintok==1:
        wn.create_oval(x1-5, y1-5, x2+5, y2+5, fill=colorrrr, outline=colorrrr)
    if paintok==2:
        wn.create_rectangle(x1-5, y1-5, x2+5, y2+5, fill=colorrrr, outline=colorrrr)
    if paintok==3:
        wn.create_polygon(x1-5, y1+5, x2+5, y2+5,x3-5,y3-5, fill=colorrrr, outline=colorrrr)
    if paintok==4:
        wn.create_polygon(positions[0]+DIMENSION/50,positions[1]+DIMENSION/50,positions[0]-DIMENSION/50,positions[1]-+DIMENSION/50,positions[-2]-DIMENSION/50,positions[-1]-DIMENSION/50,positions[-2]+DIMENSION/50,positions[-1]+DIMENSION/50,fill=colorrrr,outline=colorrrr)

def red():
    global color
    color="red"
    BLACK["state"] = NORMAL
    RED["state"] = DISABLED
    ORANGE["state"] = NORMAL
    YELLOW["state"] = NORMAL
    GREEN["state"] = NORMAL
    BLUE["state"] = NORMAL

def green():
    global color
    color="green"
    BLACK["state"] = NORMAL
    RED["state"] = NORMAL
    ORANGE["state"] = NORMAL
    YELLOW["state"] = NORMAL
    GREEN["state"] = DISABLED
    BLUE["state"] = NORMAL

def blue():
    global color
    color="blue"
    BLACK["state"] = NORMAL
    RED["state"] = NORMAL
    ORANGE["state"] = NORMAL
    YELLOW["state"] = NORMAL
    GREEN["state"] = NORMAL
    BLUE["state"] = DISABLED

def yellow():
    global color
    color="yellow"
    BLACK["state"] = NORMAL
    RED["state"] = NORMAL
    ORANGE["state"] = NORMAL
    YELLOW["state"] = DISABLED
    GREEN["state"] = NORMAL
    BLUE["state"] = NORMAL

def orange():
    global color
    color="orange"
    BLACK["state"] = NORMAL
    RED["state"] = NORMAL
    ORANGE["state"] = DISABLED
    YELLOW["state"] = NORMAL
    GREEN["state"] = NORMAL
    BLUE["state"] = NORMAL

def big():
    global DIMENSION
    BIG["state"] = DISABLED
    MB["state"] = NORMAL
    MEDIUM["state"] = NORMAL
    SMALL["state"] = NORMAL
    DIMENSION=75

def mb():
    global DIMENSION
    MB["state"] = DISABLED
    BIG["state"] = NORMAL
    MEDIUM["state"] = NORMAL
    SMALL["state"] = NORMAL
    DIMENSION=50

def medium():
    global DIMENSION
    MEDIUM["state"] = DISABLED
    MB["state"] = NORMAL
    BIG["state"] = NORMAL
    SMALL["state"] = NORMAL
    DIMENSION=36

def small():
    global DIMENSION
    SMALL["state"] = DISABLED
    MB["state"] = NORMAL
    MEDIUM["state"] = NORMAL
    BIG["state"] = NORMAL
    DIMENSION=15

wn.bind('<B1-Motion>', radiera)
button_frame1 = tk.Frame()
button_frame1.pack(side = 'top', fill = 'x')

photoq=PhotoImage(file = "assets\BACK.png")
BACK = tkinter.Button(button_frame1, image=photoq, command = back)
BACK.pack(side = 'left', ipadx = 3, ipady = 1,padx=(150,20),pady=10)

photoa=PhotoImage(file = "assets\BIG.png")
BIG = tkinter.Button(button_frame1, image=photoa, command = big)
BIG.pack(side = 'left', ipadx = 3, ipady = 1,padx=(150,20),pady=10)

photow=PhotoImage(file = "assets\MB.png")
MB = tkinter.Button(button_frame1, image=photow, command = mb)
MB.pack(side = 'left', ipadx = 3, ipady = 1,padx=20,pady=10)



photob=PhotoImage(file = "assets\MEDIUM.png")
MEDIUM = tkinter.Button(button_frame1, image=photob, command = medium)
MEDIUM.pack(side = 'left', ipadx = 3, ipady = 1,padx=20,pady=10)

photoc=PhotoImage(file = "assets\LITTLE.png")
SMALL = tkinter.Button(button_frame1, image=photoc, command = small)
SMALL.pack(side = 'left', ipadx = 3, ipady = 1,padx=20,pady=10)

photo05=PhotoImage(file = "assets\colors\Black.png")
BLACK = tkinter.Button(button_frame1, image=photo05, command = black)
BLACK.pack(side = 'right', ipadx = 3, ipady = 1,padx=10,pady=20)
BIG["state"] = DISABLED
BLACK["state"] = DISABLED

photo0=PhotoImage(file = "assets\colors\BLUE.png")
BLUE = tkinter.Button(button_frame1, image=photo0, command = blue)
BLUE.pack(side = 'right', ipadx = 3, ipady = 1,padx=20,pady=10)

photo01=PhotoImage(file = "assets\colors\GREEN.png")
GREEN = tkinter.Button(button_frame1, image=photo01, command = green)
GREEN.pack(side = 'right', ipadx = 3, ipady = 1,padx=20,pady=10)

photo02=PhotoImage(file = "assets\colors\Orange.png")
ORANGE = tkinter.Button(button_frame1, image=photo02, command = orange)
ORANGE.pack(side = 'right', ipadx = 3, ipady = 1,padx=20,pady=10)

photo03=PhotoImage(file = "assets\colors\Yellow.png")
YELLOW = tkinter.Button(button_frame1, image=photo03, command = yellow)
YELLOW.pack(side = 'right', ipadx = 3, ipady = 1,padx=20,pady=10)

photo04=PhotoImage(file = "assets\colors\RED.png")
RED = tkinter.Button(button_frame1, image=photo04, command = red)
RED.pack(side = 'right', ipadx = 3, ipady = 1,padx=20,pady=10)


button_frame = tk.Frame()
button_frame.pack(side = 'left', fill = 'x')

photo=PhotoImage(file = "assets\creion.png")
P = tkinter.Button(button_frame, image=photo, command = paintpress)
P.pack(side = 'bottom', ipadx = 3, ipady = 1,padx=10,pady=10)

photoe=PhotoImage(file = "assets\line.png")
PL = tkinter.Button(button_frame, image=photoe, command = linepress)
PL.pack(side = 'bottom', ipadx = 3, ipady = 1,padx=10,pady=10)

photo1=PhotoImage(file = "assets\cerc.png")
H = tkinter.Button(button_frame, image=photo1, command = circlepress)
H.pack(side = 'bottom', ipadx = 3, ipady = 1,padx=10,pady=10)

photo2=PhotoImage(file = "assets\Ractangle.png")
F = tkinter.Button(button_frame, image=photo2, command = ractanglepress)
F.pack(side = 'bottom', ipadx = 3, ipady = 1,padx=10,pady=10)

photo3=PhotoImage(file = "assets\Triunghi.png")
T = tkinter.Button(button_frame, image=photo3, command = trianglepress)
T.pack(side = 'bottom', ipadx = 3, ipady = 1,padx=10,pady=10)

photo4=PhotoImage(file = "assets\Radiera.png")
RADIERA = tkinter.Button(button_frame, image=photo4, command = radierapress)
RADIERA.pack(side = 'bottom', ipadx = 3, ipady = 1,padx=10,pady=10)

photoy=PhotoImage(file = "assets\square.png")
SQUARE = tkinter.Button(button_frame, image=photoy, command = squarepress)
SQUARE.pack(side = 'bottom', ipadx = 3, ipady = 1,padx=10,pady=10)
wn.pack(side = 'bottom',anchor=SE)


root.mainloop()