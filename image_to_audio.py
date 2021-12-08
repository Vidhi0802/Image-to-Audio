from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
import pytesseract
from pygame import mixer
import os
import requests
import PySimpleGUI as sg


def image_to_sound(path_to_image):
  
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        sample_text.insert(0, cleaned_text)
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="en")
        sound.save('sound.mp3')
        messagebox.showinfo('Message', 'Completed')
        return True
    except Exception as bug:
        print("The bug thrown while excuting the code\n", bug)
        return

     
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'



def playsong():
 mixer.init()   
 mixer.music.load("sound.mp3")
 mixer.music.play()
def pausesong():
 mixer.music.pause()
def stopsong():
 mixer.music.stop()
def resumesong():
 mixer.music.unpause()
def convert():
 image_to_sound("image.jpeg")    
 


window = tkinter.Tk()
window.title("Image To Audio")
window.geometry("300x300")
  
# Creating our text widget.
sample_text = tkinter.Entry(window)
sample_text.pack()
  
# Creating the function to set the text 
# with the help of button

  
# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Play", 
                    command=playsong)
set_up_button2 = tkinter.Button(window, height=1, width=10, text="Pause", 
                    command=pausesong)
set_up_button3 = tkinter.Button(window, height=1, width=10, text="Stop", 
                    command=stopsong)
set_up_button4 = tkinter.Button(window, height=1, width=10, text="Resume", 
                    command=resumesong)
set_up_button5 = tkinter.Button(window, height=1, width=10, text="Convert", 
                    command=convert)
                  
set_up_button.pack()
set_up_button2.pack()
set_up_button3.pack()
set_up_button4.pack()
set_up_button5.pack()


  
window.mainloop()