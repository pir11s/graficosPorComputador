from tkinter import *
import math
# import messagebox from tkinter module
import tkinter.messagebox

from functools import partial
    
def basicDraw(x_list,y_list,img):
    for i in range(300,400):
        img.put("#000000", (100,i))
        x_list.append(100)
        y_list.append(i)
    for i in range(100,200):
        img.put("#000000", (i,400))
        x_list.append(i)
        y_list.append(400)
    for i in range(100,200):
        img.put("#000000", (i,300))
        x_list.append(i)
        y_list.append(300)
    for i in range(150,200):
        img.put("#000000", (i,200+i))
        x_list.append(i)
        y_list.append(200+i)
    for i in range(150,200):
        img.put("#000000", (i,300-i+200))
        x_list.append(i)
        y_list.append(300-i+200)
    return x_list,y_list

def draw_scale(x_list,y_list,scale_box,img):
    scale_value = scale_box.get()
    print(str(scale_value))
    if not isinstance(scale_value, (int, float)):
        tkinter.messagebox.showinfo("INVALID VALUE",  "Can't scale string")
        return False
    clean_pixels(x_list,y_list,img)
    for i in range(len(x_list)):
        img.put("#000000",(int(x_list[i]*scale_value),int(y_list[i]*scale_value)))


def clean_pixels(x_list,y_list,img):
    for i in range(len(x_list)):
        img.put("#ffffff",(x_list[i],y_list[i]))

def draw_move(x_list,y_list,move_x,move_y,img):
    for i in range(len(x_list)):
            img.put("#000000",(int(x_list[i]+move_x),int(y_list[i]+move_y)))
def draw_rotate(x_list,y_list,angle,img):
    radian = math.radians(angle)
    for i in range(len(x_list)):
            x = int(x_list[i]*math.cos(radian)-y_list[i]*math.sin(radian))
            y = int(x_list[i]*math.sin(radian)+y_list[i]*math.cos(radian))
            if (x < 0 or y < 0):
                tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
            img.put("#000000",(x,y))
def draw_ref_x(x_list,y_list,x_point,img):
    for i in range(len(x_list)):
            x = x_list[i]
            y = int(y_list[i] - 2*(y_list[i]-x_point))
            if (x < 0 or y < 0):
                tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
            img.put("#000000",(x,y))

def draw_ref_y(x_list,y_list,y_point,img):
    for i in range(len(x_list)):
            x = int(x_list[i] - 2*(x_list[i]-y_point))
            y = y_list[i]
            if (x < 0 or y < 0):
                tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
            img.put("#000000",(x,y))

def draw_shearing(x_list,y_list,sh_x,sh_y,img):
    for i in range(len(x_list)):
        x = int(x_list[i] + y_list[i]*sh_x)
        y = int(y_list[i] + x_list[i]*sh_y)
        if (x < 0 or y < 0):
            tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
            return False
        img.put("#000000",(x,y))
def draw_ref_ref_origin(x_list,y_list,img):
    for i in range(len(x_list)):
        x = y_list[i]
        y = x_list[i]
        if (x < 0 or y < 0):
            tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
            return False
        img.put("#000000",(x,y))

window=Tk()

x_list = []
y_list = []

# add widgets here

width = 1400
height = 700
window.title('Práctica 2')
window.geometry(str(width) + "x" + str(height) +"+10+20")
canvas=Canvas(window,bg="#ffffff")
canvas.place(x=int(width/2),y=0,height=height,width=int(width/2))
img = PhotoImage(width=width, height=height)
canvas.create_image((width/2, height/2), image=img, state="normal")

entry1 = Entry(window,width=10,)
entry1.place(x=125, y=100)

entry2 = Entry(window,width=10,)
entry2.place(x=125, y=200)

entry3 = Entry(window,width=10,)
entry3.place(x=125, y=300)


entry4 = Entry(window,width=10,)
entry4.place(x=125, y=400)

entry5 = Entry(window,width=10,)
entry5.place(x=125, y=500)

entry6 = Entry(window,width=10,)
entry6.place(x=125, y=600)

entry7 = Entry(window,width=10,)
entry7.place(x=325, y=500)

button1=Button(window, text="scale",width=10,height=1
,command=partial(draw_scale,x_list,y_list,entry1,img))
button1.place(x=200, y=100)

button2=Button(window, text="move",width=10,height=1)
button2.place(x=200, y=200)

button3=Button(window, text="rotate",width=10,height=1)
button3.place(x=200, y=300)

button4=Button(window, text="shear",width=10,height=1)
button4.place(x=200, y=400)

button5=Button(window, text="reflect x",width=10,height=1)
button5.place(x=200, y=500)

button6=Button(window, text="reflect y",width=10,height=1)
button6.place(x=200, y=600)

button7=Button(window, text="reflect rect",width=10,height=1)
button7.place(x=400, y=500)


x_list,y_list = basicDraw(x_list,y_list,img)

window.mainloop()