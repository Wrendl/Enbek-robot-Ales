import datetime
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename


def send_mail():
    sender = 'Hrrobot@ales.kz'
    receivers = ['rshoibec@ales.kz']

    msg = MIMEMultipart()
    msg['Subject'] = 'Отчет от робота Enbek.kz'
    msg['From'] = 'Hrrobot@ales.kz'
    # msg['To'] = '77_15_01_p02@ales.kz'
    msg['To'] = 'rshoibec@ales.kz'
    # msg['To'] = 'nganiyev@pythonrpa.org'

    filename = "..\\Tools\\logs\\" + str(datetime.datetime.now().strftime("%d.%m.%Y")) + ".xlsx"
    msg.attach(MIMEText(f'Отчет от робота на дату - {str(datetime.datetime.now().strftime("%d.%m.%Y"))}'))

    with open(filename, "rb") as fil:
       part = MIMEApplication(
           fil.read(),
           Name=basename(filename)
       )
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
    msg.attach(part)

    try:
       smtpObj = smtplib.SMTP('10.107.0.10')
       smtpObj.sendmail(sender, receivers, msg.as_string())
       print("Successfully sent email")
    except smtplib.SMTPException:
       print("Error: unable to send email")


send_mail()
