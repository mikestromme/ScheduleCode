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
receiver_email = '9207169265@vtext.com'



def send_text():
        

   
    message = """
    This is your message
    """

    # setup the parameters of the message
    # msg['From']='mikestromme@gmail.com'
    # msg['To']='9207169265@vtext.com'  # replace with the correct SMS gateway
    # msg['Subject']=message

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative') # use multipart in-case you want to send html and text in the body see https://docs.python.org/2/library/email-examples.html
    msg['Subject'] = message
    msg['To'] = receiver_email

    # Create the body of the message (a plain-text and an HTML version).
    email_body = ''
    part1 = MIMEText(email_body, 'plain')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)   

    # add the message content
    msg.attach(MIMEText(message, 'plain'))

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls(context=context)
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email.split(','), msg.as_string())
    
    del message

    # Terminate the SMTP session and close the connection
    server.quit()

if __name__ == "__main__":
   
   send_text()

