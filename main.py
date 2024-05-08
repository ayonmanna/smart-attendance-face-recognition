from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train 
from face_recognition import Face_Recognition
from attendance import Attendance_page
import os

class Face_Recognitation_system:
  def __init__(self,root):
     self.root=root
     self.root.geometry("1530x790+0+0")
     self.root.title("my window")

     img1=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\face image.jpg")
     img1=img1.resize((500,130))
     self.PhotoImage1=ImageTk.PhotoImage(img1)
     label1=Label(self.root,image=self.PhotoImage1)
     label1.place(x=0,y=0,width=500,height=130)
     

     
     img2=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\checkimage.jpg")
     img2=img2.resize((500,130))
     self.PhotoImage2=ImageTk.PhotoImage(img2)
     label2=Label(self.root,image=self.PhotoImage2)
     label2.place(x=500,y=0,width=500,height=130)


     img3=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\image3.jpg")
     img3=img3.resize((500,130))
     self.PhotoImage3=ImageTk.PhotoImage(img3)
     label3=Label(self.root,image=self.PhotoImage3)
     label3.place(x=1000,y=0,width=500,height=130)

      #bg image
     img4=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\bgimage.jpg")
     img4=img4.resize((1530,710))
     self.PhotoImage4=ImageTk.PhotoImage(img4)
     bg_image=Label(self.root,image=self.PhotoImage4)
     bg_image.place(x=0,y=130,width=1530,height=710)
      #tittle
     title_lbl=Label(bg_image,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM  SOFTWARE",font=("times new roman",20,"bold"),bg="black",fg="red")
     title_lbl.place(x=0,y=0,width=1530,height=30)
     
      
      #student button
     img5=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\studentbutton.jpg")
     img5=img5.resize((220,220))
     self.PhotoImage5=ImageTk.PhotoImage(img5) 

     b1=Button(bg_image,command=self.Student_details,image=self.PhotoImage5,cursor="hand2")
     b1.place(x=150,y=55,width=220,height=220)
     
     b1_1=Button(bg_image,command=self.Student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
     b1_1.place(x=150,y=275,width=220,height=40)

     #face recognition
     img6=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\facebutton.jpg")
     img6=img6.resize((220,220))
     self.PhotoImage6=ImageTk.PhotoImage(img6) 
     b2=Button(bg_image,image=self.PhotoImage6,command=self.data_recognition,cursor="hand2")
     b2.place(x=450,y=55,width=220,height=220)
     
     b2_2=Button(bg_image,text="Face Recognition" ,command=self.data_recognition,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
     b2_2.place(x=450,y=275,width=220,height=40)
     
     #attendence
     img7=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\attendencebutton.jpg")
     img7=img7.resize((220,220))
     self.PhotoImage7=ImageTk.PhotoImage(img7) 
     b3=Button(bg_image,image=self.PhotoImage7,cursor="hand2")
     b3.place(x=750,y=55,width=220,height=220)
     
     b3_3=Button(bg_image,text="Attendence" ,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
     b3_3.place(x=750,y=275,width=220,height=40)
     

     #help
     img8=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\helpbutton.jpg")
     img8=img8.resize((220,220))
     self.PhotoImage8=ImageTk.PhotoImage(img8) 
     b4=Button(bg_image,image=self.PhotoImage8,cursor="hand2")
     b4.place(x=1050,y=55,width=220,height=220)
     
     b4_4=Button(bg_image,text="Help Desk" ,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
     b4_4.place(x=1050,y=275,width=220,height=40)
     
     #train 
     img9=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\trainbutton.jpg")
     img9=img9.resize((220,220))
     self.PhotoImage9=ImageTk.PhotoImage(img9) 
     b5=Button(bg_image,image=self.PhotoImage9,command=self.data_train,cursor="hand2")
     b5.place(x=150,y=335,width=220,height=220)
     
     b5_5=Button(bg_image,text="Train Data" ,cursor="hand2",command=self.data_train,font=("times new roman",15,"bold"),bg="blue",fg="white")
     b5_5.place(x=150,y=525,width=220,height=40)

     #photo
     img10=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\photobutton.jpg")
     img10=img10.resize((220,220))
     self.PhotoImage10=ImageTk.PhotoImage(img10) 
     b6=Button(bg_image,image=self.PhotoImage10,cursor="hand2",command=self.open_img)
     b6.place(x=450,y=335,width=220,height=220)
     
     b6_6=Button(bg_image,text="Photos" ,cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
     b6_6.place(x=450,y=525,width=220,height=40)

     #developer
    
     img11=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\developarbutton.jpg")
     img11=img11.resize((220,220))
     self.PhotoImage11=ImageTk.PhotoImage(img11) 
     b7=Button(bg_image,image=self.PhotoImage11,cursor="hand2")
     b7.place(x=750,y=335,width=220,height=220)
     
     b7_7=Button(bg_image,text="Developer" ,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
     b7_7.place(x=750,y=525,width=220,height=40)

     #exit

     img12=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\exitbutton.jpg")
     img12=img12.resize((220,220))
     self.PhotoImage12=ImageTk.PhotoImage(img12) 
     b8=Button(bg_image,image=self.PhotoImage12,cursor="hand2")
     b8.place(x=1050,y=335,width=220,height=220)
     
     b8_8=Button(bg_image,text="Exit" ,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
     b8_8.place(x=1050,y=525,width=220,height=40)
  #function for open dataset file open photos button
         

     #FUNCTION BUTTON
  def open_img(self):
     os.startfile("data")
  def Student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)
  def data_train(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)     
  def data_recognition(self):
       self.new_window=Toplevel(self.root)
       self.app=Face_Recognition(self.new_window)     



if __name__ == "__main__":
   root=Tk()
   obj=Face_Recognitation_system(root)
   root.mainloop()
