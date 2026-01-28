import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#Read configuration from environment
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))

class EmailService:
    def __init__(self):
        logger.info("Intializing EmailService")
        logger.debug(f"SMTP Configuration - Server: {SMTP_SERVER}, Port: {SMTP_PORT}")

        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            raise ValueError(
                "EMAIL_ADDRESS or EMAIL_PASSWORD is missing. "
                "Please configure them in your .env file."
            )
        
    def send(self, #je gmail aama hase ema email jase
             subject: str, #send Email
             to_email: str,
             text_body: str,
             html_body: str | None = None, 
             attachments:list[str] | None = None,
    ):
        logger.info(f"Preparing to send email - Subject: '{subject}', To: {to_email}")
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = to_email
            msg.set_content(text_body)

            if html_body:
                msg.add_alternative(html_body, subtype="html")

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
                logger.debug("Starting SSL encryption")
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                logger.debug("Authentication successful")
                smtp.send_message(msg)
                logger.info(f"Email send successfully to {to_email}")
                
        except Exception as e:
            print(f"Failed to send email: {e}")
            raise
