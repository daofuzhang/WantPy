import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def sendSMTPMail(strSMTPServer, strFrom, arrayTo, strSubject, strContent, strAttachFilePath, strAttachFileName):
    mimeMessage = MIMEMultipart()
    mimeMessage["Subject"] = strSubject
    mimeMessage["From"] = strFrom
    mimeMessage["To"] = ", ".join(arrayTo)
    mimeMessage.attach(MIMEText(strContent))

    if strAttachFilePath != None and strAttachFileName != None:
        with open(strAttachFilePath, "rb") as fileAttacch:
            objApplication = MIMEApplication(fileAttacch.read(), Name=strAttachFileName)
            objApplication["Content-Disposition"] = "attachment; filename='%s'" % strAttachFileName
            mimeMessage.attach(objApplication)

    smtpServer = smtplib.SMTP(strSMTPServer)
    smtpServer.sendmail(strFrom, arrayTo, mimeMessage.as_string())
    smtpServer.quit()
    return True

def sendSMTPMailWithMultiAttach(strSMTPServer, strFrom, arrayTo, strSubject, strContent, listAttachFilePath, listAttachFileName):
    mimeMessage = MIMEMultipart()
    mimeMessage["Subject"] = strSubject
    mimeMessage["From"] = strFrom
    mimeMessage["To"] = ", ".join(arrayTo)
    mimeMessage.attach(MIMEText(strContent))

    intFileIndex = 0
    for strAttachFilePath in listAttachFilePath:
        with open(strAttachFilePath, "rb") as fileAttacch:
            objApplication = MIMEApplication(fileAttacch.read(), Name=listAttachFileName[intFileIndex])
            objApplication["Content-Disposition"] = "attachment; filename='%s'" % listAttachFileName[intFileIndex]
            mimeMessage.attach(objApplication)
        intFileIndex += 1

    smtpServer = smtplib.SMTP(strSMTPServer)
    smtpServer.sendmail(strFrom, arrayTo, mimeMessage.as_string())
    smtpServer.quit()
    return True
