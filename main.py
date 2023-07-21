import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Set up the SMTP server
    s = smtplib.SMTP(host='your-smtp-server.com', port=your-port)
    s.starttls()
    
    # Login to your email account
    s.login('your-email@example.com', 'your-password')

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
    msg['From']='your-email@example.com'
    msg['To']='your-email@example.com'
    msg['Subject']="Weekly Drumming Motivation"

    # add the message content
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server.
    s.send_message(msg)
    
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()

# Schedule the job every week
schedule.every(7).days.at("10:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
