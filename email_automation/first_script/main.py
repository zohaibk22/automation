import yagmail
from dotenv import load_dotenv
import os
import time
from datetime import datetime as dt


load_dotenv()

sender = os.getenv("SENDER_EMAIL")
receiver = os.getenv("RECEIVER_EMAIL")
subject = "Test Email"
contents = """"
Here is the content of the email.
This is a test email sent using yagmail.

"""

yag = yagmail.SMTP(user=sender, password=os.getenv("SENDER_EMAIL_PASSWORD"))

print("Email sent successfully!") 


while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 15:
        yag.send(to=receiver, subject=subject, contents=contents)
        print(f"Email sent at {now.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(60)