from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import place

class Help_desk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK",font=("Algerian",20,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1500,height=35)
        
        # img_top=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\re2.jpg")
        # img_top = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re2.jpg")
        img_top = Image.open(r"Images\helpdesk.png")
        img_top=img_top.resize((1366, 700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1500,height=650)

        dev_label=Label(f_lbl,text="MCT's Rajiv Gandhi Institute Of Technology,Andheri", font=("Comic Sans MS",20,"bold"),fg="#313545")
        dev_label.place(x=300,y=600)



if __name__=="__main__":
    root=Tk()
    obj=Help_desk(root)
    root.mainloop()