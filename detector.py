import cv2
import numpy as np
import mysql.connector
event=''
import datetime
d3=''
flag=1
def setevent(eventname):
    global d3
    global event
    event=str(eventname)
    print(event)
    conn=mysql.connector.connect(user='root',password='',host='localhost',database='deepblue_attendance',port=3306)
    mycursor=conn.cursor()
    result=mycursor.execute("SELECT event_date FROM event WHERE heading = '%s'"%event)
    row=mycursor.fetchone()
    now=datetime.datetime.now()   
    d1=datetime.datetime.strptime(str(row[0]),"%Y-%m-%d")
    d2=datetime.datetime.strptime(now.strftime("%Y-%m-%d"),"%Y-%m-%d")
    d3=str(abs((d2 - d1).days))
    d3=int(d3)+1

def attendance(ID):
    global d3
    global event
    global flag
    print(ID)
    print("doing")
    conn=mysql.connector.connect(user='root',password='',host='localhost',database='deepblue_attendance',port=3306)
    mycursor=conn.cursor()
    if(flag==1):
        mycursor.execute("UPDATE attendence_demo SET attendance='PRESENT' WHERE student_id=%s AND day=%s",(ID,d3))
        conn.commit()
        flag=2
        print("done")
    print("function done")
	
def finalrecognition():
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0);
    rec=cv2.createLBPHFaceRecognizer();
    rec.load(event+"\\tranningData.yml",)
    idc='unknown'
    font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
        faces = faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])		
            if(conf<50):
                cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
                cv2.cv.PutText(cv2.cv.fromarray(img),str(conf),(x+y,y+w),font,255);
                attendance(id)
            else:
                cv2.cv.PutText(cv2.cv.fromarray(img),str(idc),(x,y+h),font,255);								
        cv2.imshow("Face",img); 
        		
        if(cv2.waitKey(1)==ord('q')):
            print("exit")
            break;
    cam.release()
    cv2.destroyAllWindows()