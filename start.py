#Import all the necessary libraries
from tkinter import *
from PIL import ImageTk, Image
import os

#Define the tkinter instance

win = Tk()
win.title("Start Page")

#Define the size of the tkinter frame

win.geometry("1500x844")
win.geometry('%dx%d+%d+%d' % (1500, 844, 5, 0))
img =Image.open('Input/img/start/start.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(win, image=bg)
label.pack()

#Define the working of the button

#========Load Start page=================

# function for start button
def my_command1():
   win.destroy()
   os.system("python home.py")

# function for Aboutus button
def my_command2():
   win.destroy()
   os.system("python about.py")

# function for Exit button
def my_command3():
   win.destroy()

#Import the image using PhotoImage function
click_btn1= PhotoImage(file='Input/img/start/start.png')

#Let us create a dummy button and pass the image
# start button
btnUsingImg= Button(win, image=click_btn1,command = my_command1, borderwidth=0)
btnUsingImg.place(x=634, y=730)

# About us button
click_btn2= PhotoImage(file='Input/img/start/about.png')
btnUsingImg= Button(win, image=click_btn2,command = my_command2, borderwidth=0)
btnUsingImg.place(x=100, y=730)

# Exit button
click_btn3= PhotoImage(file='Input/img/start/exit.png')
btnUsingImg= Button(win, image=click_btn3,command = my_command3, borderwidth=0)
btnUsingImg.place(x=1300, y=730)

win.mainloop()