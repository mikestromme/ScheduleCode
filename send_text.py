import smtplib, ssl
#import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
email_password = os.getenv("email_password")
smtp_server = os.getenv("smtp_server")
sender_email = os.getenv("sender_email")



def send_text():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls(context=context)
        server.login(sender_email, email_password)
    

    msg = MIMEMultipart()

    message = """
    This is your message
    """

    # setup the parameters of the message
    msg['From']='mikestromme@gmail.com'
    msg['To']='9207169265@vtext.com'  # replace with the correct SMS gateway
    msg['Subject']=message

    # add the message content
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server.
    server.send_message(msg)
    
    del msg

    # Terminate the SMTP session and close the connection
    server.quit()

if __name__ == "__main__":
   
   send_text()

