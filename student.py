from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
 
class Student:
   def __init__(self,root):
     self.root=root
     self.root.geometry("1530x790")
     self.root.title("my window")
      #variables
     
     self.var_dep=StringVar()  
     self.var_course=StringVar()  
     self.var_year=StringVar()
     self.var_semester=StringVar()  
     self.var_student_id=IntVar()  
     self.var_std_name=StringVar()
     self.var_div=StringVar()  
     self.var_roll=StringVar()
     self.var_gender=StringVar()
     self.var_dob=StringVar()
     self.var_phone=StringVar()  
     self.var_address=StringVar()  
     self.var_teacher=StringVar()  
     self.var_email=StringVar()
     self.var_photo=StringVar()
     



     img1=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\student3.jpg")
     img1=img1.resize((500,130))
     self.PhotoImage1=ImageTk.PhotoImage(img1)
     label1=Label(self.root,image=self.PhotoImage1)
     label1.place(x=0,y=0,width=500,height=130)
     

     
     img2=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\student2page.jpg")
     img2=img2.resize((500,130))
     self.PhotoImage2=ImageTk.PhotoImage(img2)
     label2=Label(self.root,image=self.PhotoImage2)
     label2.place(x=500,y=0,width=500,height=130)


     img3=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\student4.jpg")
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
     title_lbl=Label(bg_image,text="STUDENT  MANAGEMENT  SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="dark green")
     title_lbl.place(x=0,y=0,width=1530,height=30)


     main_frame=Frame(bg_image,bd=2)
     main_frame.place(x=5,y=55,width=1530,height=900)



       
 #left frame
     
     left_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student Details information",font=("times new roman",12,"bold"),fg="blue")
     left_frame.place(x=10,y=0,width=770,height=800)

#left image

     img_left=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\frameimage1.jpg")
     img_left=img_left.resize((760,50))
     self.photoimg_left=ImageTk.PhotoImage(img_left)
     f_lb3=Label(left_frame,image=self.photoimg_left)
     f_lb3.place(x=5,y=0,width=760,height=50)
#current course
     current_couse_frame=LabelFrame(left_frame,bd=2,bg="black",relief=RIDGE,text="Current Course information",font=("times new roman",12,"bold"),fg="blue")
     current_couse_frame.place(x=5,y=50,width=760,height=100)
       
#department combo box
     dep_label=Label(current_couse_frame,bg="black",text="Department",font=("times new roman",15,"bold"),fg="blue")
     dep_label.grid(row=0,column=0,padx=10)
     dep_combo=ttk.Combobox(current_couse_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=15,state="read only")
     dep_combo["values"]=("Select Department","AIML","Computer science","Information technology","ECE","Civil","Mechanical","Automobile")
     dep_combo.current(0)
     dep_combo.grid(row=0,column=1,padx=2,pady=7)

#course and combo box
     course_label=Label(current_couse_frame,bg="black",text="Courses",font=("times new roman",15,"bold"),fg="blue")
     course_label.grid(row=0,column=2,padx=10,sticky=W)
     course_combo=ttk.Combobox(current_couse_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=15,state="read only")
     course_combo["values"]=("Select course","B.tech","M.tech","B.voc","M.voc","B.B.A.","M.B.A","Diploma")
     course_combo.current(0)
     course_combo.grid(row=0,column=3)


     #year

     year_label=Label(current_couse_frame,bg="black",text="Year",font=("times new roman",15,"bold"),fg="blue")
     year_label.grid(row=1,column=0,padx=10,sticky=W)
     year_combo=ttk.Combobox(current_couse_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=15,state="read only")
     year_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24")
     year_combo.current(0)
     year_combo.grid(row=1,column=1)

     #semester

     semester_label=Label(current_couse_frame,bg="black",text="Semester",font=("times new roman",15,"bold"),fg="blue")
     semester_label.grid(row=1,column=2,padx=10,sticky=W)
     semester_combo=ttk.Combobox(current_couse_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=15,state="read only")
     semester_combo["values"]=("Select semester","sem-1","sem-2","sem-3","sem-4")
     semester_combo.current(0)
     semester_combo.grid(row=1,column=3)


     #class student frame
     class_student_frame=LabelFrame(left_frame,bd=2,bg="black",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"),fg="blue")
     class_student_frame.place(x=5,y=150,width=760,height=250)
      #student id
     studentId_label=Label(class_student_frame,bg="black",text="StudentId:",font=("times new roman",15,"bold"),fg="blue")
     studentId_label.grid(row=0,column=0,padx=10,sticky=W)

     studentId_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_student_id,font=("times new roman",15,"bold"))
     studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


     #student name
     studentName_label=Label(class_student_frame,bg="black",text="Student Name:",font=("times new roman",15,"bold"),fg="blue")
     studentName_label.grid(row=0,column=2,padx=10,sticky=W)

     studentName_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_std_name,font=("times new roman",15,"bold"))
     studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
     #classdivision
     class_div_label=Label(class_student_frame,bg="black",text="Class Division:",font=("times new roman",15,"bold"),fg="blue")
     class_div_label.grid(row=1,column=0,padx=10,sticky=W)

     #class_div_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_div,font=("times new roman",15,"bold"))
     #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

     class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",14,"bold"),width=14,state="read only")
     class_div_combo["values"]=("A","B","C")
     class_div_combo.current(0)
     class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

     #roll no
     roll_no_label=Label(class_student_frame,bg="black",text="Roll No:",font=("times new roman",15,"bold"),fg="blue")
     roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

     roll_no_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_roll,font=("times new roman",15,"bold"))
     roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
     #GENDER
     gender_label=Label(class_student_frame,bg="black",text="Gender:",font=("times new roman",15,"bold"),fg="blue")
     gender_label.grid(row=2,column=0,padx=10,sticky=W)

     #gender_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_gender,font=("times new roman",15,"bold"))
     #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

     gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",14,"bold"),width=14,state="read only")
     gender_combo["values"]=("male","female","other")
     gender_combo.current(0)
     gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

     #dob
     dob_label=Label(class_student_frame,bg="black",text="D.O.B:",font=("times new roman",15,"bold"),fg="blue")
     dob_label.grid(row=2,column=2,padx=10,sticky=W)

     dob_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_dob,font=("times new roman",15,"bold"))
     dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
     #EMAIL
     EMAIL_label=Label(class_student_frame,bg="black",text="Email Id:",font=("times new roman",15,"bold"),fg="blue")
     EMAIL_label.grid(row=3,column=0,padx=10,sticky=W)

     EMAIL_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_email,font=("times new roman",15,"bold"))
     EMAIL_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
     #phone no
     phone_label=Label(class_student_frame,bg="black",text="Phone No:",font=("times new roman",15,"bold"),fg="blue")
     phone_label.grid(row=3,column=2,padx=10,sticky=W)

     phone_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_phone,font=("times new roman",15,"bold"))
     phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
     #address
     adress_label=Label(class_student_frame,bg="black",text="Address:",font=("times new roman",15,"bold"),fg="blue")
     adress_label.grid(row=4,column=0,padx=10,sticky=W)

     adress_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_address,font=("times new roman",15,"bold"))
     adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
     #teacher name
     teacher_label=Label(class_student_frame,bg="black",text="Teacher Name:",font=("times new roman",15,"bold"),fg="blue")
     teacher_label.grid(row=4,column=2,padx=10,sticky=W)

     teacher_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_teacher,font=("times new roman",15,"bold"))
     teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
     #radio button
     self.var_radio1=StringVar()
     Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="YES")
     Radiobutton1.grid(row=6,column=0)
     
     
     Radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
     Radiobutton2.grid(row=6,column=1)

     #buton frame
     button_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="black")
     button_frame.place(x=0,y=405,width=770,height=90)

     save_button=Button(button_frame,text="Save",command=self.add_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="green")
     save_button.grid(row=0,column=0)

     update_button=Button(button_frame,text="Update",command=self.update_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="green")
     update_button.grid(row=0,column=1)

     delete_button=Button(button_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="green")
     delete_button.grid(row=0,column=2)

     reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",15,"bold"),bg="blue",fg="green")
     reset_button.grid(row=0,column=3)
                       
      #take photo smaple                  
     take_photo_button=Button(button_frame,text="Take Photo Sample",command=self.generate_dataset,width=15,font=("times new roman",12,"bold"),bg="blue",fg="green")
     take_photo_button.grid(row=1,column=0)
       #upload photo smaple                                    
     upload_photosample_button=Button(button_frame,text="Upload Photo Sample",width=15,font=("times new roman",12,"bold"),bg="blue",fg="green")
     upload_photosample_button.grid(row=1,column=1)
     #right frame
     right_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student Details information",font=("times new roman",12,"bold"),fg="blue")
     right_frame.place(x=780,y=0,width=660,height=580)
      #right img
     img_right=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\student and teacher pic right frame.jpg")
     img_right=img_right.resize((660,100))
     self.photoimg_right=ImageTk.PhotoImage(img_right)
     f_lb3=Label(right_frame,image=self.photoimg_right)
     f_lb3.place(x=5,y=0,width=660,height=100)
                                         
     #search system
     search_frame=LabelFrame(right_frame,bd=2,bg="black",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),fg="blue")
     search_frame.place(x=0,y=105,width=600,height=400)

     search_label=Label(search_frame,bd=2,bg="black",relief=RIDGE,text="Search By:",font=("times new roman",15,"bold"),fg="red")
     search_label.grid(row=0,column=0,padx=8,pady=5,sticky=W)

     #new combo for serach
     
     search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),width=12,state="read only")
     search_combo["values"]=("Select ","roll no:","Phone no:")
     search_combo.current(0)
     search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

     search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",12,"bold"))
     search_entry.grid(row=0,column=2,padx=8,pady=5,sticky=W)

     search_button=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="green")
     search_button.grid(row=0,column=3,padx=3)

     show_all_button=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="green")
     show_all_button.grid(row=0,column=4,padx=3)
      #table frame
     table_frame=Frame(right_frame,bd=2,bg="black",relief=RIDGE)
     table_frame.place(x=5,y=170,width=550,height=300)

     #scroll bar right frame
     scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
     scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

     self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","dob","name","email","div","roll","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
     scroll_x.pack(side=BOTTOM,fill=X)
     scroll_y.pack(side=RIGHT,fill=Y)
     scroll_x.config(command=self.student_table.xview)
     scroll_y.config(command=self.student_table.yview)

#("dep","course","year","sem","id","dob","name","email","div","roll","gender","phone","address","teacher","photo")
     #scroll show
     self.student_table.heading("dep",text="Department")
     self.student_table.heading("course",text="course")
     self.student_table.heading("year",text="year")
     self.student_table.heading("sem",text="semester")
     self.student_table.heading("id",text="studentid")
     self.student_table.heading("dob",text="DOB")
     self.student_table.heading("name",text="Name")
     self.student_table.heading("email",text="Email id")
     self.student_table.heading("div",text="Division")
     self.student_table.heading("roll",text="Roll")
     self.student_table.heading("gender",text="Gender")
     self.student_table.heading("phone",text="Phone")
     self.student_table.heading("address",text="Address")
     self.student_table.heading("teacher",text="Teacher")
     self.student_table.heading("photo",text="Photo")
     
     self.student_table["show"]="headings"

     self.student_table.column("dep",width="150")
     self.student_table.column("course",width="150")
     self.student_table.column("year",width="150")
     self.student_table.column("sem",width="150")
     self.student_table.column("id",width="150")
     self.student_table.column("dob",width="150")
     self.student_table.column("name",width="150")
     self.student_table.column("email",width="150")
     self.student_table.column("div",width="150")
     self.student_table.column("roll",width="150")
     self.student_table.column("gender",width="150")
     self.student_table.column("phone",width="150")
     self.student_table.column("address",width="150")
     self.student_table.column("teacher",width="150")
     self.student_table.column("photo",width="150")

     self.student_table.pack(fill=BOTH,expand=1)
     self.student_table.bind("<ButtonRelease>",self.get_cursor)
     self.fetch_data()

  #function declaration
   def add_data(self):
          if self.var_dep.get()=="select Department" or self.var_std_name.get()==" " or self.var_student_id.get()==" ":
              messagebox.showerror("Error","All Fields Are Required",parent=self.root)
          else:
              #messagebox.showinfo("success bocachodagon ","Welcome our system ")
              try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="W2002@gopal#",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                         
                                                       self.var_dep.get(),  
                                                       self.var_course.get(),  
                                                       self.var_year.get(),
                                                       self.var_semester.get(),  
                                                       self.var_student_id.get(),
                                                       self.var_dob.get(),
                                                       self.var_std_name.get(),
                                                       self.var_email.get(),
                                                       self.var_div.get(),  
                                                       self.var_roll.get(),
                                                       self.var_gender.get(),
                                                       self.var_phone.get(),  
                                                       self.var_address.get(),  
                                                       self.var_teacher.get(),
                                                       
                                                       self.var_radio1.get()
                                                       
                                                                                                             
                                              ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("success","student details has been added successfully",parent=self.root)
              except Exception as es:
                  messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)
     

     #fetch data
   def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="W2002@gopal#",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student1")
        data=my_cursor.fetchall()
     
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

     #**********get cursor***********
   def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]


       self.var_dep.set(data[0]),  
       self.var_course.set(data[1]),  
       self.var_year.set(data[2]),
       self.var_semester.set(data[3]),
       self.var_student_id.set(data[4]),
       self.var_dob.set(data[5]), 
       self.var_std_name.set(data[6]),
       self.var_email.set(data[7]),
       self.var_div.set(data[8]),  
       self.var_roll.set(data[9]),
       self.var_gender.set(data[10]),
       
       self.var_phone.set(data[11]),  
       self.var_address.set(data[12]),  
       self.var_teacher.set(data[13]),  
       
       
       self.var_radio1.set(data[14])

   #UPDATE FUNCTION
   def update_data(self):
        if self.var_dep.get() == "select Department" or self.var_std_name.get() == " " or self.var_student_id.get() == " ":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                print("hellow")
                conn = mysql.connector.connect(host="localhost", username="root", password="W2002@gopal#",
                                               database="face_recognition")
                my_cursor = conn.cursor()

                update_query = """
                    UPDATE student1 
                    SET Department=%s, course=%s, year=%s, sem=%s, dob=%s, name=%s, email=%s, 
                    division=%s, roll=%s, gender=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                    WHERE studentid=%s
                """

                values = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_dob.get(),
                    self.var_std_name.get(),
                    self.var_email.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_photo.get(),
                    self.var_student_id.get()
                )

                my_cursor.execute(update_query, values)
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
            
                  
            #try problem
           

       #**********delete function********
   def delete_data(self):
       if self.var_student_id.get()=="":
           messagebox.showerror("Error","student id must be recuired",parent=self.root)
       else:
           try:
               delete=messagebox.askyesno("student delete page","do you want to delete this student",parent=self.root)
               if delete>0:
                   conn=mysql.connector.connect(host="localhost",username="root",password="W2002@gopal#",database="face_recognition")
                   my_cursor=conn.cursor()
                   sql="delete from student1 where studentid=%s"
                   val=(self.var_student_id.get(),)
                   my_cursor.execute(sql,val)
               else:
                   if not delete:
                       return
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("delete","successfully deleted student details",parent=self.root)
           except Exception as es:
               messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                             
   #******reset*****
   def reset_data(self):
       self.var_dep.set("select Department"),  
       self.var_course.set("select course"),  
       self.var_year.set("select year"),
       self.var_semester.set("select semester"),
       self.var_student_id.set(""),  
       self.var_std_name.set(""),
       self.var_div.set("select division"),  
       self.var_roll.set(""),
       self.var_gender.set("Male"),
       self.var_dob.set(""),
       self.var_phone.set(""),  
       self.var_address.set(""),  
       self.var_teacher.set(""),  
       self.var_email.set(""),
       self.var_photo.set(""),
       self.var_radio1.set(""),
     # generate data set and take photo samples
   def generate_dataset(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()==" " or self.var_student_id.get()==" ":
              messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            #try problem
            try:
                print("hi bal")
                conn=mysql.connector.connect(host="localhost",username="root",password="W2002@gopal#",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student1")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor = conn.cursor()

                update_query = """
                    UPDATE student1 
                    SET Department=%s, course=%s, year=%s, sem=%s, dob=%s, name=%s, email=%s, 
                    division=%s, roll=%s, gender=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                    WHERE studentid=%s
                """

                values = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_dob.get(),
                    self.var_std_name.get(),
                    self.var_email.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_photo.get(),
                    self.var_student_id.get()==id+1
                )

                my_cursor.execute(update_query, values)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # load redefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                cap=cv2.VideoCapture(0)
                img_id=0
                print("sala")
                def face_cropped(img):
                    #print("gar matra")
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #print("bal cher")
                    #scaling factor = 1.3
                    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        print("hel")
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                while True:
                   
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(300,300))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)
                        print("gandu")

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed !!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
   
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()