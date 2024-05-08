from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
from cv2 import *
 
class Train:
   def __init__(self,root):
     self.root=root
     self.root.geometry("1530x790")
     self.root.title("train process")

     title_lbl=Label(self.root,text="TARIN DATA SET",font=("times new roman",25,"bold"),bg="black",fg="RED")
     title_lbl.place(x=0,y=0,width=1530,height=30)
     # top image 
     img_top=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\training_photo.jpg")
     img_top=img_top.resize((1530,325))
     self.photoimg_top=ImageTk.PhotoImage(img_top)
     f_lb3=Label(self.root,image=self.photoimg_top)
     f_lb3.place(x=0,y=35,width=1530,height=325)

     #botton image
     b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
     b1_1.place(x=0,y=365,width=1530,height=70)
     img_botton=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\training_photo2.jpg")
     img_botton=img_botton.resize((1530,325))
     self.photoimg_botton=ImageTk.PhotoImage(img_botton)
     f_lb3=Label(self.root,image=self.photoimg_botton)
     f_lb3.place(x=0,y=440,width=1530,height=325)

   def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root) 
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()