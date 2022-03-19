from ntpath import join

from pyttsx3 import speak
from student import Student
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re
import os
import numpy as np
from time import strftime
from datetime import datetime
import cv2 as cv
# import pyttsx3
from os.path import isfile,join
from os import listdir
import time
import pandas as pd
import csv
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Algerian",20,"bold"),bg="lightblue",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1366,height=35)

       #first image
        # img_top=Image.open(r"Images\n.jpg")
        # img_top=img_top.resize((630, 650),Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=45,width=630,height=650)
        
        # second image
        img_bottom=Image.open(r"Images\re1.jpg")
        # img_bottom = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        img_bottom = img_bottom.resize((1366, 700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=50,width=1366,height=650)
        
        # Button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Algerian",15,"bold"),bg="darkgreen",fg="yellow")
        b1_1.place(x=500,y=450,width=300,height=150)






    


        # =================Attendance ====================
    # def mark_attendance(self,i,r,n,d):
    def mark_attendance(self,i,r,n,d):
        with open("Teamkyzen23.csv","r+",newline="\n") as f:
            
            # f.drop_duplicates()
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (i not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                # d1 for date variable
                dtString=now.strftime("%H:%M:%S")
                # myDatalist.drop_duplicates(keep=False)
             

                f.writelines(f"\n{i},{r},{n},{d},{dtString}, {d1},Present")




                # DF_RM_DUP.write_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teamkyzen1.csv")




                
                
                # os.wait(5)
                # time.sleep(5) 

     # face recognition  command=self.face_recog
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)   

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h+20,x:x+w+20])
                # confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="shruti0603",database="face_recognizer")
                # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()

                
                print(n)
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                
                r = "+".join(r)

                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                
                d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                
                i = "+".join(i)
                # 
                # new code for accuracy calculation
                # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                # result = id.predict(img)

                if predict < 500:
                # if result[1] < 500:
                    confidence=int((100*(1-predict/300)))
                    # str2 = str(confidence)
                    # confidence = int(100 * (1 - (result[1])/300))
                    # display_string = str(confidence)+'% confidence it is user'
                # cv2.putText(img,display_string(250, 250), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Accuracy:{confidence}%",(x, y-100), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)



                if confidence> 80:
                    cv2.putText(img,f"Student_id: {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,0,255),3)
                    speak_va("Warning!!! Unknown Face")
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord 
            
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)   
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            # speak_va("Welcome to Face Recognition World")
            cv2.imshow("Welcome to face Recognition",img)


            if cv2.waitKey(1)==13:
                
                break
        video_cap.release()
        cv2.destroyAllWindows()


        # df_state=pd.read_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teamkyzen23.csv")
        df_state = pd.read_csv(r"D:\DWONLOD SSD\Facial-Recognition-Based-Student-Attendance-System-main\Teamkyzen23.csv")
    
        # Dup_Rows = df_state[df_state.duplicated()]

        DF_RM_DUP = df_state.drop_duplicates(keep=False) 

        # print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

        # DF_RM_DUP = df_state.drop_duplicates(keep=False)
    # writer=csv.writer(DF_RM_DUP.head(n=1))

    # pahilaaaa koooooooooooooooo display
#    .............. # [[  data = DF_RM_DUP.head(n=1)
    # #    ((((((Pahilaaa koooo yo)))))) # data.to_csv('teamkyzen1.csv',encoding='utf-8', index=True)
    #     with open("test.csv", "wt") as fp:
    #         writer = csv.writer(fp)
    # # writer.writerow(["your", "header", "foo"])  # write header
    #         writer.writerow(data)
    
        # DF_RM_DUP.to_csv('test.csv', index=False) 
        DF_RM_DUP.to_csv('test1.csv', index=False) 


       


        



        



        
    #     df_state=pd.read_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teamkyzen2.csv")
    
    #     # Dup_Rows = df_state[df_state.duplicated()]

    #     DF_RM_DUP = df_state.drop_duplicates(keep=False) 

    #     # print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

    #     # DF_RM_DUP = df_state.drop_duplicates(keep=False)
    # # writer=csv.writer(DF_RM_DUP.head(n=1))


    # # print('\n\nResult DataFrame after duplicate removal :\n', DF_RM_DUP.head(n=1))
    #     data = str(DF_RM_DUP.head(n=1))

    #     with open('teamkyzen1.csv', 'w', encoding='UTF8') as data:
    #       writer = csv.writer(data)
                
        

                    
                      




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()

# from ntpath import join
# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np
# from time import strftime
# from datetime import datetime




# class Face_Recognition:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")
        
#         title_lbl=Label(self.root,text="FACE RECONGNITION",font=("times new roman",20,"bold"),bg="lightblue",fg="darkgreen")
#         title_lbl.place(x=0,y=0,width=1366,height=35)
        
#         #first image
#         img_top=Image.open(r"Images\n.jpg")
#         img_top=img_top.resize((630, 650),Image.ANTIALIAS)
#         self.photoimg_top=ImageTk.PhotoImage(img_top)

#         f_lbl=Label(self.root,image=self.photoimg_top)
#         f_lbl.place(x=0,y=45,width=630,height=650)
        
#         # second image
#         img_bottom=Image.open(r"Images\face_re.jpg")
#         img_bottom=img_bottom.resize((712, 650),Image.ANTIALIAS)
#         self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

#         f_lbl=Label(self.root,image=self.photoimg_bottom)
#         f_lbl.place(x=640,y=45,width=712,height=650)
        
#         # Button
#         b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="darkgreen",fg="white")
#         b1_1.place(x=300,y=605,width=190,height=35)
        
#     # attendance
#     # def mark_attendance(self,i,r,n,d):
#     #     with open("Bamma.csv","r+",newline="\n") as f:
#     #         myDataList=f.readlines()
#     #         name_list=[]
#     #         for line in myDataList:
#     #             entry=line.split((","))
#     #             name_list.append(entry[0])
#     #         if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ) : 
#     #             now=datetime.now()
#     #             d1=now.strftime("%d/%m/%Y")
#     #             dtString=now.strftime("%H:%M:%S")
#     #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



        

        
#     # face recognition
#     def face_recog(self):
#         def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

#             coord=[]
        
#             for (x,y,w,h) in features:
#                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#                 id,predict=clf.predict(gray_image[y:y+h,x:x+w])
#                 confidence=int((100*(1-predict/300)))
                
#                 conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
#                 my_cursor=conn.cursor()
                
#                 my_cursor.execute("select Name from student where id="+str(id))
#                 n=my_cursor.fetchone()
#                 n="+".join(n)
                
#                 my_cursor.execute("select Roll from student where id="+str(id))
#                 r=my_cursor.fetchone()
#                 r="+".join(r)
                
#                 my_cursor.execute("select Dep from student where id="+str(id))
#                 d=my_cursor.fetchone()
#                 d="+".join(d)
                
#                 # my_cursor.execute("select id from student where id="+str(id))
#                 # i=my_cursor.fetchone()
#                 # i="+".join(i)
                
#                 if confidence>77:
#                     # cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     # self.mark_attendance(i,r,n,d)
#                 else:
#                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                     cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 coord=[x,y,w,h]

#             return coord        

#         def recognize(img,clf,faceCascade):
#             coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)   
#             return img
        
#         faceCascade=cv2.CascadeClassifier(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\classifier.xml")
        
#         video_cap=cv2.VideoCapture(0)
        
#         while True:
#             ret,img=video_cap.read()
#             img=recognize(img,clf,faceCascade)
#             cv2.imshow("Welcome to face Recognition",img)

#             if cv2.waitKey(1)==13:
#                 break
#         video_cap.release()
#         cv2.destroyAllWindows()
        
#         # repeat
#         # captureDevice = cv2.VideoCapture(0) #captureDevice = camera

#         # while True:
#         #     ret, frame = captureDevice.read() 

#         #     cv2.imshow('my frame', frame)
#         #     if cv2.waitKey(1) & 0xFF == ord('q'):
#         #         break

#         # captureDevice.release()
#         # cv2.destroyAllWindows()
            

        
                        
                    
        
        
# if __name__ == "__main__":
#     root=Tk()
#     obj=Face_Recognition(root)
#     root.mainloop()