import os
import yagmail

receiver = "abhishekghorpade07@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = r"C:\TY\Sem5\Desighn Project 1\it f\it f\Face-Recognition-Attendance-System\FRAS\Attendance\Attendance.csv" # attach the file

# mail information
yag = yagmail.SMTP("senderabhi07@gmail.com", "bejgcsxezqwabajj")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
