import smtplib
import ssl
import shutil
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


smtp_server = 'smtp.gmail.com'
smtp_port = 587

gmail = 'YOUR_GMAIL_HERE' #Enter sender email address
password = 'YOUR_GMAIL_PASSWORD_HERE' #Enter sender email password

message = MIMEMultipart('mixed')
message['From'] = 'Contact <{sender}>'.format(sender = gmail)
message['To'] = 'DESTINATION_EMAIL_ADDRESS_HERE'  #Enter destination email
message['Subject'] = 'Home Security Alert'

msg_content = '<h4>The following image was picked up by your security system: </h4>\n'
body = MIMEText(msg_content, 'html')
message.attach(body)



def establishAttachment(attachment_path):

    try:
        with open(attachment_path, "rb") as attachment:
            p = MIMEApplication(attachment.read(), _subtype="jpg")
            p.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path)
            message.attach(p)

    except Exception as e:
        print(str(e))

    msg_full = message.as_string()
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(gmail, password)
        server.sendmail(gmail, 'DESTINATION_EMAIL_ADDRESS_HERE', msg_full) #Enter destination email
        server.quit()
        print("email sent out successfully")

def fromFlaggedToSent(saveDir, videoFile, issueID):
    print("Moving Files from ./Flagged to ./Sent ...")
    os.mkdir(f'./Sent/{saveDir}')
    os.replace(f'./Flagged/{saveDir}/{videoFile}', f'./Sent/{saveDir}/{videoFile}')
    os.replace(f'./Flagged/{saveDir}/frame_{issueID}-Detected.jpg', f'./Sent/{saveDir}/frame_{issueID}-Detected.jpg')
    shutil.rmtree(f'./Flagged/{saveDir}')

