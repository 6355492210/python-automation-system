import base64
import os
import logging
from typing import List, Optional, Union
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Assuming this service module exists in your project structure
from services.gmail_auth import Create_Service 

# --- Configuration ---
# specific loggers are better than root loggers in production
logger = logging.getLogger(__name__) 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GmailClient:
    """
    A wrapper class for the Gmail API to handle authentication and email sending.
    """
    def __init__(self, secret_file: str, api_name: str = "gmail", api_version: str = "v1", scopes: List[str] = None):
        if scopes is None:
            scopes = ["https://mail.google.com/"]
        
        self.secret_file = secret_file
        self.scopes = scopes
        
        # Initialize service once during instantiation
        try:
            self.service = Create_Service(secret_file, api_name, api_version, scopes)
            logger.info("Gmail API Service authenticated successfully.")
        except Exception as e:
            logger.critical(f"Failed to authenticate Gmail Service: {e}")
            raise

    def send_email(
        self,
        to_email: str,
        subject: str,
        text_body: str,
        attachments: Optional[List[str]] = None
    ) -> bool:
        """
        Constructs and sends an email with optional attachments.
        
        :param to_email: Recipient email address.
        :param subject: Email subject line.
        :param text_body: Plain text body of the email.
        :param attachments: List of file paths to attach.
        :return: True if sent successfully, False otherwise.
        """
        try:
            message = MIMEMultipart()
            message["to"] = to_email
            message["subject"] = subject
            message.attach(MIMEText(text_body, "plain"))

            # Process Attachments
            if attachments:
                for file_path in attachments:
                    self._attach_file(message, file_path)

            # Encode message
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

            # Send via Gmail API
            self.service.users().messages().send(
                userId="me",
                body={"raw": raw_message}
            ).execute()

            logger.info(f"Email sent successfully to: {to_email}")
            return True

        except Exception as e:
            logger.error(f"Failed to send email to {to_email}. Error: {e}")
            return False

    def _attach_file(self, message: MIMEMultipart, file_path: str):
        """Helper method to validate and attach a file to the message."""
        if not os.path.exists(file_path):
            logger.warning(f"Attachment skipped (File not found): {file_path}")
            return

        try:
            part = MIMEBase("application", "octet-stream")
            with open(file_path, "rb") as f:
                part.set_payload(f.read())
            
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f'attachment; filename="{os.path.basename(file_path)}"',
            )
            message.attach(part)
        except Exception as e:
            logger.error(f"Could not attach file {file_path}: {e}")

# --- Usage Example ---
if __name__ == "__main__":
    CLIENT_SECRET = "client_secret.json"
    
    # Instantiate the client once
    try:
        gmail_client = GmailClient(CLIENT_SECRET)
        
        # Use it to send emails
        gmail_client.send_email(
            to_email="recipient@example.com",
            subject="Project Update",
            text_body="Here is the report.",
            attachments=["report.pdf", "data.xlsx"]
        )
    except Exception as e:
        print(f"Application initialization failed: {e}")