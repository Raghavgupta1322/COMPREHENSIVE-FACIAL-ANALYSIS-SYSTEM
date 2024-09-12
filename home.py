#Import all the necessary libraries
from tkinter import *
from PIL import ImageTk, Image
import os

#Define the tkinter instance
win = Tk()
win.title("Home Page")

#Define the size of the tkinter frame
win.geometry("1500x844")
win.geometry('%dx%d+%d+%d' % (1500, 844, 5, 0))
img =Image.open('Input/img/home/home.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(win, image=bg)
label.pack()

#Define the working of the button
#========Load home page=================

# function for face detection using image button
def my_command1():
   win.destroy()
   os.system("python countMultipleFace_image.py")

# function for face detection using web button
def my_command2():
   win.destroy()
   os.system("python countface_webcam.py")

# function for eye detection using image button
def my_command3():
   win.destroy()
   os.system("python eye.py")

# function for eye detection using web button
def my_command4():
   win.destroy()
   os.system("python Blink_Eye_Detect.py")

# function for age detection button
def my_command5():
   win.destroy()
   os.system("python age_detection.py")

# function for gender detection button
def my_command6():
   win.destroy()
   os.system("python gender_detection.py")

# function for about us button
def my_command8():
   win.destroy()
   os.system("python about.py")

# Exit function
def my_command9():
   win.destroy()


#Import the image using PhotoImage function
click_btn1= PhotoImage(file='Input/img/home/uig.png')

# Let us create a dummy button and pass the image
# face detection using image
btnUsingImg= Button(win, image=click_btn1,command = my_command1, borderwidth=0)
btnUsingImg.place(x=1050, y=177)

# face detection using web
click_btn2= PhotoImage(file='Input/img/home/uwg.png')
btnUsingImg= Button(win, image=click_btn2,command = my_command2, borderwidth=0)
btnUsingImg.place(x=1300, y=177)

# eye detection using img
click_btn3= PhotoImage(file='Input/img/home/uiy.png')
btnUsingImg= Button(win, image=click_btn3,command = my_command3, borderwidth=0)
btnUsingImg.place(x=1050, y=430)

# eye detection using web
click_btn4= PhotoImage(file='Input/img/home/uwY.png')
btnUsingImg= Button(win, image=click_btn4,command = my_command4, borderwidth=0)
btnUsingImg.place(x=1300, y=430)

# Age Detection
click_btn5= PhotoImage(file='Input/img/home/ad.png')
btnUsingImg= Button(win, image=click_btn5,command = my_command5,borderwidth=0)
btnUsingImg.place(x=1100, y=580)

# gender Detection
click_btn6= PhotoImage(file='Input/img/home/gd.png')
btnUsingImg= Button(win, image=click_btn6,command = my_command6,borderwidth=0)
btnUsingImg.place(x=1100, y=660)

# About us
click_btn8= PhotoImage(file='Input/img/home/about.png')
btnUsingImg= Button(win, image=click_btn8,command = my_command8,borderwidth=0)
btnUsingImg.place(x=115, y=700)

# Exit
click_btn9= PhotoImage(file='Input/img/home/exit.png')
btnUsingImg= Button(win, image=click_btn9,command = my_command9,borderwidth=0)
btnUsingImg.place(x=800, y=700)

win.mainloop()

