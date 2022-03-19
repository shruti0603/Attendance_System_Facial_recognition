from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import place

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPERS",font=("Algerian",20,"bold"),bg="yellow",fg="Blue")
        title_lbl.place(x=0,y=0,width=1500,height=35)
        
        # img_top=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\re2.jpg")
        # img_top = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re2.jpg")
        img_top = Image.open(r"Images\developer.png")
        img_top=img_top.resize((1366, 700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1500,height=650)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white",)
        main_frame.place(x=1000,y=0,width=500,height=800)

        #dev info
        dev_label=Label(main_frame,text="Hello, We are TE A Students,", font=("Comic Sans MS",20,"bold"),fg="Green",bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Department- Computer Enginnering", font=("Comic Sans MS",18,"bold"),fg="red",bg="white")
        dev_label.place(x=0,y=65)

        dev_label=Label(main_frame,text="Group Members are:", font=("Comic Sans MS",18,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=130)

        dev_label=Label(main_frame,text="A627- Mrunal Gavit", font=("Helvetica",18,"bold"),bg="white",fg="black")
        dev_label.place(x=0,y=165)

        dev_label=Label(main_frame,text="A637- Shruti Halde", font=("Helvetica",18,"bold"),bg="white",fg="black")
        dev_label.place(x=0,y=200)

        dev_label=Label(main_frame,text="A638- Rhea Indurkar", font=("Helvetica",18,"bold"),bg="white",fg="black")
        dev_label.place(x=0,y=235)

        dev_label=Label(main_frame,text="A641- Hinal Jethava", font=("Helvetica",18,"bold"),bg="white",fg="black")
        dev_label.place(x=0,y=270)

        dev_label=Label(main_frame,text="Project Guide- Prof. B N Panchal", font=("Comic Sans MS",18,"bold"),fg="#3c3c3c",bg="white")
        dev_label.place(x=0,y=320)

if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()