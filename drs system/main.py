# All media file is available for download as a zip file (See description)
import tkinter 
from cv2 import cv2 # pip install opencv-python
import PIL.Image, PIL.ImageTk # pip install pillow
from functools import partial
import threading
import time
import imutils # pip install imutils

stream = cv2.VideoCapture('clip.mp4')
text =True
def play(speed):
    global text
    frame1 =stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)
    grabbed, frame =stream.read()
     
    if not grabbed:
         exit()
    frame =imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0,anchor=tkinter.NW,image=frame)
    if text:
        canvas.create_text(134,26,text="Decsion Pending", fill="black",font="Times 24 bold")
    text = not text
    print(f"The speed of video is {speed}")

def pending(decesion):
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame =imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0,anchor=tkinter.NW,image=frame)

    time.sleep(1.5)

    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame =imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0,anchor=tkinter.NW,image=frame)
    time.sleep(2.5)

    if decesion =='out':
        show_img ="out.png"
    else:
        show_img ="not_out.png"
    
    frame = cv2.cvtColor(cv2.imread(show_img),cv2.COLOR_BGR2RGB)
    frame =imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0,anchor=tkinter.NW,image=frame)

def out():
    thread =threading.Thread(target=pending,args=("out",))
    thread.daemon =1
    thread.start()

    print("The out is clicked")

def not_out():
    thread =threading.Thread(target=pending,args=("not_out",))
    thread.daemon =1
    thread.start()
    print("The not out is clicked")

SET_WIDTH = 656
SET_HEIGHT = 370

window = tkinter.Tk()
window.title('Arnav DRS System')
cv_image =cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
canvas =tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo_image = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image))
image_on_canvas =canvas.create_image(0,0,anchor=tkinter.NW,image = photo_image)
canvas.pack()

btn =tkinter.Button(window,text =">>Previous(slow)",width=50,command=partial(play,-2))
btn.pack()
btn =tkinter.Button(window,text =">>Previous(fast)",width=50,command=partial(play,-25))
btn.pack()
btn =tkinter.Button(window,text ="Next (slow)<<",width=50,command=partial(play,2))
btn.pack()
btn =tkinter.Button(window,text ="Next (fast)<<",width=50,command=partial(play,25))
btn.pack()
btn =tkinter.Button(window,text ="Give out",width=50,command=out)
btn.pack()
btn =tkinter.Button(window,text ="Give Not out",width=50,command=not_out)
btn.pack()

tkinter.mainloop()