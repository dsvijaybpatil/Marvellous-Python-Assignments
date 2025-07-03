import os
import sys
import psutil # type: ignore
import time
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def SendEmail(FolderName,filename,Emailid):
    msg=MIMEMultipart()
    msg['From']="patilvijay.95@gmail.com"
    msg['To']=Emailid
    msg['Subject']='Log file using python script'
    body='please find the attached log file'
    msg.attach(MIMEText(body,'plain'))
    filepath=os.path.join(FolderName,filename)
    with open(filepath,"rb") as f:
    attached_file=MIMEApplication(f.read(),_subtype="log")
    attached_file.add_header("Content-Disposition",'attachment',filename=filepath)
    msg.attach(attached_file)
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login('patilvijay.95@gmail.com','bnfkelrcgpknunsd')
    msg="this is the testing mail sent by python script. How r u"
    server.sendmail('patilvijay.95@gmail.com',Emailid,msg)

def CreateLog(FolderName,Emailid):
    flag=os.path.isabs(FolderName)
    if flag==False:
        FolderName=os.path.abspath(FolderName)
        
    flag=os.path.exists(FolderName)
    
    if flag==False:
        print("The given directory does not exists.")
        exit()
    flag=os.path.isdir(FolderName)
    if flag==False:
        print("The given path is correct but it is not a directory.")
    
    timestamp=time.ctime()
    filename="Marvellous%s.log"%timestamp
    filename=filename.replace(" ","_")
    filename=filename.replace(":","_")
    logfileName=os.path.join(FolderName,filename)
    flag2=os.path.exists(logfileName)
    if flag2==False:
        logfile=open(logfileName,"w")
        logfile.close()
    logfile=open(logfileName,"a")
    logfile.write("Marvellous Infosystem Process Log\n")
    logfile.write("Log File is created at:"+str(timestamp)+"\n")
    Data=ProcessScan()
    for content in Data:
        logfile.write("%s \n"%content)
    logfile.close()
    SendEmail(FolderName,filename,Emailid)

    
def ProcessScan():

    for proc in psutil.process_iter():       
        
            Data=proc.as_dict(attrs=['name',"pid","username"])
    return Data       
       
        

    
    
def main():
   Border="-"*80
   print(Border)
   print("-----------------------Marvellous Automation--------------------")
   print(Border)
   if (len(sys.argv)==2):
        if((sys.argv[1]=="--h") or sys.argv[1]=="--H"):
            print("This application is used to stored Processess in log file.")
            
        elif((sys.argv[1]=="--u") or sys.argv[1]=="--U"):
            print("Use the given script as")
            print("ScriptName.py ProcessName")
            
   elif(len(sys.argv)==3):
     CreateLog(sys.argv[1],sys.argv[2])
       
            
   
   else:
        print("Invalid Number of Command line arguments.")         
        print("Use the given flag as:")
        print("--h: Use to Display the help.")
        print("--u: Use to Display the usage.")
       

if __name__=="__main__":
    main()