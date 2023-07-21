import smtplib
#import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_text():
    # Set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    
    # Login to your email account
    s.login('mikestromme@gmail.com', '')

    msg = MIMEMultipart()

    message = """
    Here are the reasons why drumming is important:
    1. Personal Fulfillment: ...
    2. Physical and Mental Health Benefits: ...
    3. Creativity: ...
    4. Social Benefits: ...
    5. Life-long Learning: ...
    6. Inspiration to Others: ...
    7. Brain Training: ...
    Remember, the most important thing is that you enjoy what you're doing...
    """

    # setup the parameters of the message
    msg['From']='mikestromme@gmail.com'
    msg['To']='9207169265@vtext.com'  # replace with the correct SMS gateway
    msg['Subject']="Test"

    # add the message content
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server.
    s.send_message(msg)
    
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == "__main__":
   
   send_text()

