import email
import smtplib
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fill in credentials here
# Make sure you have enabled access to less secure apps in your google profile. You can do it from here
# myaccount.google.com/lesssecureapps
credentials = {'username': 'demo.mail.pb@gmail.com',
               'password': '11223344Aa!'}

# Start connection
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Log in to the server
server.login(credentials['username'], credentials['password'])

# Build message
message = MIMEMultipart()
message['Subject'] = 'Demo Mail'
message['From'] = 'demo.mail.pb@gmail.com'
message['To'] = 'nikola.dunchev@abv.bg'
message_text = f'Hello! This email is sent from demo! {datetime.now()}'
body = MIMEText(message_text)
message.attach(body)

# Send the mail
server.send_message(message)
print('Mail sent!')