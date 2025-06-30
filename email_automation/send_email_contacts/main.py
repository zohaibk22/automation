import os
import yagmail
import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv('files/contacts.csv')

    for row in df.itertuples(index=False):
        name = row.name
        email = row.email

        sender = os.getenv('SENDER_EMAIL')
        receiver = email
        subject = f"Hello {name}!"
        body = """
        this is a test email to run a automation script
        """.strip()

        yag = yagmail.SMTP(sender, password=os.getenv('SENDER_PASSWORD'))

        yag.send(to=receiver, subject=subject, contents=body, attachments='files/test.doc')

        print(f"Email sent to {name} at {email}")

