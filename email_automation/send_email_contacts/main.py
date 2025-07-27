import os
import yagmail
import pandas as pd
from dotenv import load_dotenv

if __name__ == "__main__":
    # print(os.getcwd(), "currsent working directory")
    load_dotenv()

    df = pd.read_csv('files/contacts.csv')
    sender = os.getenv('SENDER_EMAIL')
    yag = yagmail.SMTP(sender, password=os.getenv('SENDER_EMAIL_PASSWORD'))


    for row in df.itertuples(index=False):
        name = row.name
        email = row.email
        file_name = row.filepath.strip() if hasattr(row, 'filepath') else None
        print(row, "ROW")

        receiver = email
        subject = f"Hello {name}!"
        body = """
        this is a test email to run a automation script
        """.strip()


        try:
            yag.send(to=receiver, subject=subject, contents=body, attachments="bills/" + file_name if file_name else None)
        except Exception as e:
            print(f"Failed to send email to {name} at {email}: {e}")
            continue

        print(f"Email sent to {name} at {email}")

