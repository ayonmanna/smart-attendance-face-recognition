from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance_page:

    def __init__(self,root):

        self.root=root

        self.root.geometry("1530x790+0+0")

        self.root.title("face Recogniton System")

        #********variables*********
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()
        
        
         #first image
        img=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\checkimage.jpg")

        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f__lbl=Label(self.root,image=self.photoimg)
        f__lbl.place(x=0,y=0,width=800,height=200)

        #second image
        img1=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\studentsdetailsimage.jpg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f__lbl=Label(self.root,image=self.photoimg1)
        f__lbl.place(x=800,y=0,width=800,height=200)


        #bg image
        img3=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\bgimage.jpg")
        img3=img3.resize((1530,710))
        self.PhotoImage3=ImageTk.PhotoImage(img3)
        bg_image=Label(self.root,image=self.PhotoImage3)
        bg_image.place(x=0,y=200,width=1530,height=710)


        #tittle
        title_lbl=Label(bg_image,text="ATTENDANCE  MANAGEMENT  SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
                        
                        
        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=0,y=55,width=1530,height=900)


        #left label frame
     
        left_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student Attendance Details information",font=("times new roman",12,"bold"),fg="blue")
        left_frame.place(x=0,y=10,width=770,height=800)

        img_left=Image.open(r"C:\Users\abc\Desktop\minor_project\project image\student4.jpg")
        img_left=img_left.resize((760,150))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb3=Label(left_frame,image=self.photoimg_left)
        f_lb3.place(x=5,y=0,width=770,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="black")
        left_inside_frame.place(x=0,y=135,width=760,height=450)

        #label and entry
        #attendance id
        attendanceId_label=Label(left_inside_frame,bg="black",text="AttendanceId:",font=("times new roman",15,"bold"),fg="blue")
        attendanceId_label.grid(row=0,column=0,padx=10,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_id,font=("times new roman",15,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        studentName_label=Label(left_inside_frame,bg="black",text="Roll:",font=("times new roman",15,"bold"),fg="blue")
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("times new roman",15,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        name_label=Label(left_inside_frame,text="Name:",bg="black",font=("times new roman",15,"bold"),fg="blue")
        name_label.grid(row=1,column=0,padx=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font=("times new roman",15,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)



        #Department
        department_label=Label(left_inside_frame,text="Department:",bg="black",font=("times new roman",15,"bold"),fg="blue")
        department_label.grid(row=1,column=2,padx=10,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_dep,font=("times new roman",15,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time
        time_label=Label(left_inside_frame,text="Time:",bg="black",font=("times new roman",15,"bold"),fg="blue")
        time_label.grid(row=2,column=0,padx=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_time,font=("times new roman",15,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        date_label=Label(left_inside_frame,text="Date:",bg="black",font=("times new roman",15,"bold"),fg="blue")
        date_label.grid(row=2,column=2,padx=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("times new roman",15,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status:",bg="black",font=("times new roman",15,"bold"),fg="blue")
        attendance_label.grid(row=3,column=0,padx=10,sticky=W)

        atten_combo=ttk.Combobox(left_inside_frame,font=("times new roman",10,"bold"),width=15,state="read only")
        atten_combo["values"]=("Status","Present","Absent")
        atten_combo.current(0)
        atten_combo.grid(row=3,column=1,pady=5)
        #button frame
        button_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="black")
        button_frame.place(x=0,y=400,width=715,height=35)
        
        #button_frame.place(x=0,y=200,width=715,height=10)

        save_button=Button(left_inside_frame,text="Import csv",width=18,command=self.importcsv,font=("times new roman",13,"bold"),bg="blue",fg="black")
        save_button.grid(row=20,column=0)

        update_button=Button(left_inside_frame,text="Export csv",width=18,command=self.exportcsv,font=("times new roman",13,"bold"),bg="blue",fg="black")
        update_button.grid(row=20,column=1)

        delete_button=Button(left_inside_frame,text="Update",width=18,font=("times new roman",13,"bold"),bg="blue",fg="black")
        delete_button.grid(row=20,column=2)

        reset_button=Button(left_inside_frame,text="Reset",width=18,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="black")
        reset_button.grid(row=20,column=3)
                       





        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Attendance Details information",font=("times new roman",12,"bold"),fg="blue")
        right_frame.place(x=755,y=10,width=760,height=580)

        #table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="black")
        table_frame.place(x=5,y=5,width=600,height=350)

        #==========scroll bar table===========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("department","roll","name","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("department",width=80)
        self.AttendanceReportTable.column("roll",width=80)
        self.AttendanceReportTable.column("name",width=80)
        self.AttendanceReportTable.column("time",width=80)
        self.AttendanceReportTable.column("date",width=80)
        self.AttendanceReportTable.column("attendance",width=80)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #***********fetch data***********

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
          self.AttendanceReportTable.insert("",END,values=i)
     #********import csv**********
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

   #********export csv**********
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("no data","no data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
             exp_write=csv.writer(myfile,delimiter=",")
             for i in mydata:
                exp_write.writerow(i)
             messagebox.showinfo("data export","your data exported"+os.path.basename(fln)+"successfully")
        except Exception as es:
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_dep.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_time.set(row[3])
        self.var_atten_date.set(row[4])
        self.var_atten_attendence.set(row[5])

        #**********reset data************
    def reset_data(self):
        self.var_atten_dep.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")

if __name__ == "__main__":
    root=Tk()
    obj=Attendance_page(root)
    root.mainloop()