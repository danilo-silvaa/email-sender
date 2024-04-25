import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class EmailSender:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password

    def send(self, subject, body, recipients, filename=None, attachment=None):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(recipients)
        
        msg.attach(MIMEText(body, 'plain'))

        if filename and attachment:
            with open(attachment, 'rb') as file:
                part = MIMEApplication(file.read(), Name=filename)
            part['Content-Disposition'] = f'attachment; filename="{filename}"'
            msg.attach(part)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, recipients, msg.as_string())