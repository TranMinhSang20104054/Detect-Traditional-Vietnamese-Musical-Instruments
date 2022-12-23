import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import re
from tensorflow import keras
from winsound import *
from tensorflow.keras.utils import load_img, img_to_array



#Load Model-------------------------------------
new_model = tf.keras.models.load_model("C:\\Users\\tranm\\Downloads\\nhaccu.h5")

#Def button import image--------------------------
def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()
    

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 200 # Processing image for displaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    panel_image = tk.Label(frame, image=img).pack()

    
#Def CLASSIFY

def classify():
    original = Image.open(image_data)
    original = original.resize((150, 150), Image.ANTIALIAS)
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    #processed_image = new_model.preprocess_input(image_batch.copy())
    result = new_model.predict(image_batch)
    global prediction
    if round(result[0][0]) == 1:
        prediction = 'Đàn Bầu'
    if round(result[0][1]) == 1:
        prediction = 'Đàn Đáy'
    if round(result[0][2]) == 1:
        prediction = 'Đàn Nguyệt'
    if round(result[0][3]) == 1:
        prediction = 'Đàn Nhị'
    if round(result[0][4]) == 1:
        prediction = 'Đàn Tranh' 
    if round(result[0][5]) == 1:
        prediction = 'Sáo Trúc'

    print("Đây là :", str(prediction).upper())
    
    
    loainhaccu = tk.Label(wd, text = str(prediction).upper(), bg = '#F0F0F0',fg = 'sienna', font= ("", 22))
    loainhaccu.place(x= 250, y = 315)
   
    #sound
    root = Tk() # create tkinter window
    play = lambda: PlaySound("D:\\AI\\nhaccu\\"+str(prediction)+".wav", SND_FILENAME)
    button= tk.Button(wd)
    button["bg"] = "grey"
    button['font'] = ("Candara", 12)
    button["fg"] = "cyan"
    button["justify"] = "center"
    button["text"] = 'Phát âm thanh của '+str(prediction)
    button.place(x=195,y=260,width=210,height=30)
    button["command"] = play 
    root.mainloop()

    
#Def GIAO DIEN
wd = Tk()
wd.title('VIETNAMESE INSTRUMENTS DETECT')
wd.iconbitmap("D:\\AI\\nhaccu\\download-_1_.ico")
wd.geometry('600x400')
wd.resizable(width=False, height=False)


Label01=tk.Label(wd)
Label01["activebackground"] = "#58a5de"
Label01['font'] = ("Candara", 20)
Label01["fg"] = "#333333"
Label01['bg'] = 'azure'
Label01["justify"] = "center"
Label01["text"] = "  NHAC CU DAN TOC VIET NAM "
Label01["relief"] = "flat"
Label01.place(x=0,y=0,width=600,height=50)

frame = Frame(wd)
frame['bg'] = 'white'
frame['bd'] = 5
frame.place(x=200, y =60, width = 200, height = 200)

#INFORMATION:--------------------------------------------------------
Label02=tk.Label(wd)
Label02['font'] = ("Candara", 14)
Label02["fg"] = "black"
Label02["justify"] = "right"
Label02["text"] = "Đây Là:"
Label02["relief"] = "flat"
Label02.place(x=150,y=325,width=100,height=25)


#Def button
Button_01=tk.Button(wd)
Button_01["bg"] = "yellow"
Button_01['font'] = ("Candara", 10)
Button_01["fg"] = "#000000"
Button_01["justify"] = "center"
Button_01["text"] = "THÊM ẢNH"
Button_01.place(x=20,y=150,width=118,height=30)
Button_01["command"] = load_img 



#Button classify
Button_02=tk.Button(wd)
Button_02["bg"] = "cyan"
Button_01['font'] = ("Candara", 10)
Button_02["fg"] = "#000000"
Button_02["justify"] = "center"
Button_02["text"] = "NHẬN DIỆN"
Button_02.place(x=450,y=150,width=116,height=30)
Button_02["command"] = classify


wd.mainloop()