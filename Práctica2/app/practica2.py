from tkinter import *
import math
# import messagebox from tkinter module
import tkinter.messagebox
import time
from functools import partial

window=Tk()
# add widgets here

width = 1400
height = 700
window.title('Práctica 2')
window.geometry(str(width) + "x" + str(height) +"+10+20")
canvas=Canvas(window,bg="#ffffff")
canvas.place(x=0,y=0,height=height,width=width)
img = PhotoImage(width=width, height=height)
canvas.create_image((width/2, height/2), image=img, state="normal")

sh_x,sh_y = 0.7,0.5
scale_value = 1.2
move_x,move_y=200,200
x_point,y_point=100,100
angle = 10
rect_y_1 = 600
rect_y_2 = 200

rect_x_1 = 400
rect_x_2 = 300

def initialize_figure():
    x_list,y_list = [],[]
    for i in range(350,450): 
        x_list.append(int(width/2-300)+100)
        y_list.append(i)
    for i in range(100,200):     
        x_list.append(int(width/2-300) +i)
        y_list.append(450)
    for i in range(100,200):
        x_list.append(int(width/2-300)+i)
        y_list.append(350)
    for i in range(150,200):
        x_list.append(int(width/2-300)+i)
        y_list.append(250+i)
    for i in range(150,200):
        x_list.append(int(width/2-300)+i)
        y_list.append(350-i+200)
    return x_list,y_list

def draw_rect_y():
    a = canvas.create_rectangle(rect_y_1,rect_y_2,rect_y_1,rect_y_2+300,fill='black',tags="rect")

def delete_rect_y():
    a = canvas.delete("rect")

def draw_rect_x():
    a = canvas.create_rectangle(rect_x_1-300,rect_x_2,rect_x_1,rect_x_2,fill='black')

def delete_rect_x():
    a = canvas.delete("rect")


def clean_pixels(x_list,y_list):
    for i in range(len(x_list)):
        img.put("#ffffff",(x_list[i],y_list[i]))
 
def basicDraw():
    canvas.delete("default")
    canvas.create_text(int(width/2),10,fill="darkblue",font="Times 20 italic bold",
                        text="Basic Draw.",tags="default")
    x_list,y_list = initialize_figure()
    for i in range(len(x_list)):
        img.put("#000000",(x_list[i],y_list[i]))
    window.after(1000,clean_pixels,x_list,y_list)

def draw_scale():
    canvas.delete("default")
    canvas.create_text(int(width/2),10,fill="darkblue",font="Times 20 italic bold",
                        text="Draw scale.",tags="default")
    x_list,y_list = initialize_figure()
    for i in range(len(x_list)):
        img.put("#000000",(int(x_list[i]*scale_value),int(y_list[i]*scale_value)))
        x_list[i] = int(x_list[i]*scale_value)
        y_list[i] = int(y_list[i]*scale_value)
    window.after(1000,clean_pixels,x_list,y_list)
   
def draw_move():
    canvas.delete("default")
    canvas.create_text(int(width/2),10,fill="darkblue",font="Times 20 italic bold",
                        text="Draw move.",tags="default")
    x_list,y_list = initialize_figure()
    for i in range(len(x_list)):
        img.put("#000000",(int(x_list[i]+move_x),int(y_list[i]+move_y)))
        x_list[i] = int(x_list[i]+move_x)
        y_list[i] = int(y_list[i]+move_y)
    window.after(1000,clean_pixels,x_list,y_list)
def draw_rotate():
    canvas.delete("default")
    canvas.create_text(int(width/2),10,fill="darkblue",font="Times 20 italic bold",
                        text="Draw rotate.",tags="default")
    x_list,y_list = initialize_figure()
    radian = math.radians(angle)
    for i in range(len(x_list)):
        x = int(x_list[i]*math.cos(radian)-y_list[i]*math.sin(radian))
        y = int(x_list[i]*math.sin(radian)+y_list[i]*math.cos(radian))
        if (x < 0 or y < 0):
            tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
        img.put("#000000",(x,y))
        x_list[i]=x
        y_list[i]=y
    window.after(1000,clean_pixels,x_list,y_list)
def draw_ref_x():
    canvas.delete("default")
    canvas.create_text(int(width/2),10,fill="darkblue",font="Times 20 italic bold",
                        text="Draw ref x.",tags="default")
    x_list,y_list = initialize_figure()
    for i in range(len(x_list)):
        x = x_list[i]
        y = int(y_list[i] - 2*(y_list[i])-rect_x_2)
        if (x < 0 or y < 0):
            tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")  
            return False          
        img.put("#000000",(x,y))
        x_list[i]=x
        y_list[i]=y
    window.after(1000,clean_pixels,x_list,y_list)
def draw_ref_y():
    x_list,y_list = initialize_figure()
    canvas.delete("default")
    canvas.create_text(int(width/2),10,fill="darkblue",font="Times 20 italic bold",
                        text="Draw ref y.",tags="default")
    for i in range(len(x_list)):
        x = int(x_list[i] - 2*(x_list[i]-rect_y_1))
        y = y_list[i]
        if (x < 0 or y < 0):
            tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
            return False
        img.put("#000000",(x,y))
        x_list[i]=x
        y_list[i]=y
    window.after(1000,clean_pixels,x_list,y_list)
def draw_shearing():
    canvas.delete("default")
    canvas.create_text(int(width/2),10,fill="darkblue",font="Times 20 italic bold",
                        text="Draw shearing.",tags="default")
    x_list,y_list = initialize_figure()
    for i in range(len(x_list)):
        x = int(x_list[i] + y_list[i]*sh_x)
        y = int(y_list[i] + x_list[i]*sh_y)
        if (x < 0 or y < 0):
            tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
            return False
        img.put("#000000",(x,y))
        x_list[i]=x
        y_list[i]=y
    window.after(1000,clean_pixels,x_list,y_list)
def draw_ref_ref_rect(x_list,y_list):
    x_list,y_list = initialize_figure()
    for i in range(len(x_list)):
        x = y_list[i]
        y = x_list[i]
        if (x < 0 or y < 0):
            tkinter.messagebox.showinfo("INVALID VALUE",  "Can't rotate such angle")
            return False
        img.put("#000000",(x,y))
        x_list[i]=x
        y_list[i]=y
    window.after(1000,clean_pixels,x_list,y_list)
def main_loop():
    canvas.delete("default")
    canvas.create_text(int(width/2),10,fill="darkblue",font="Times 20 italic bold",
                        text="START",tags="default")
    # window.after(1000,basicDraw)
    # window.after(2000,draw_scale)
    # window.after(3000,basicDraw)
    # window.after(4000,draw_move)
    # window.after(5000,basicDraw)
    # window.after(6000,draw_rotate)
    # window.after(7000,basicDraw)
    # window.after(8000,draw_shearing)
    # window.after(9000,basicDraw)
    # window.after(9000,draw_rect_y)
    # window.after(10000,draw_ref_y)
    # window.after(11000,delete_rect_y)
    window.after(1000,basicDraw)
    # window.after(2000,draw_rect_x)
    # window.after(3000,draw_ref_x)
    # window.after(4000,delete_rect_x)
    # window.after(5000,basicDraw)
    window.after(2000,main_loop)

window.after(0,main_loop)
window.mainloop()