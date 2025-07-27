import os
from pathlib import Path
import logging
import pandas as pd
import yagmail
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

def send_invoice_email(yag, name, email, amount, attachment_path):
    try:
        yag.send(
            to=email,
            subject=f"Invoice for {name}",
            contents=f"Please find attached your invoice for the amount of ${amount}.",
            attachments=attachment_path
        )
        logging.info(f"Email sent to {email}")
    except Exception as e:
        logging.error(f"Failed to send email to {email}: {e}")

def main():
    load_dotenv()
    sender = os.getenv('SENDER_EMAIL')
    password = os.getenv('SENDER_EMAIL_PASSWORD')
    if not sender or not password:
        logging.error("Missing SENDER_EMAIL or SENDER_EMAIL_PASSWORD in environment.")
        return

    contacts_path = Path(__file__).parent / 'files' / 'contact.csv'
    if not contacts_path.exists():
        logging.error(f"Contacts file not found: {contacts_path}")
        return

    contacts_df = pd.read_csv(contacts_path)
    yag = yagmail.SMTP(sender, password=password)

    for _, row in contacts_df.iterrows():
        name = row.get('name', 'Recipient')
        email = row.get('email')
        amount = row.get('amount')
        if not all([name, email, amount]):
            logging.warning(f"Missing data for row: {row}")
            continue

        bill_path = Path('bills') / f"{email}.txt"
        bill_path.parent.mkdir(parents=True, exist_ok=True)
        with open(bill_path, 'w') as f:
            f.write(f"Dear {name},\n\nYour bill amount is: ${amount}\n\nThank you!")

        send_invoice_email(yag, name, email, amount, bill_path)

if __name__ == "__main__":
    main()