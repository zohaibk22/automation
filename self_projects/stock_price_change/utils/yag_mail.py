import yagmail
class YagMail:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.yag = yagmail.SMTP(user=self.sender_email, password=self.sender_password)

    def send_email(self, receiver_email, subject, body):
        try:
            self.yag.send(to=receiver_email, subject=subject, contents=body)
            print("Email sent successfully")
        except Exception as e:
            print("Failed to send email:", e)

    def close(self):
        self.yag.close()


    @classmethod
    def from_env(cls):
        """
        Create a YagMail instance using environment variables:
        SENDER_EMAIL and SENDER_EMAIL_PASSWORD.
        """
        import os
        sender_email = os.getenv('SENDER_EMAIL')
        sender_password = os.getenv('SENDER_EMAIL_PASSWORD')
        if not sender_email or not sender_password:
            raise ValueError("Environment variables SENDER_EMAIL and SENDER_EMAIL_PASSWORD must be set.")
        return cls(sender_email, sender_password)
