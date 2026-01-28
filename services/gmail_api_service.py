import base64 #gmail api msg
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

from services.gmail_auth import Create_Service

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]


def send_email_gmail_api(
    to_email: str,
    subject: str,
    text_body: str,
    attachments: list[str] | None = None,
):
    service = Create_Service(
        CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES
    )

    message = MIMEMultipart()
    message["to"] = to_email
    message["subject"] = subject

    message.attach(MIMEText(text_body, "plain"))

    # Attach files (xlsx / pdf etc.)
    if attachments:
        for file_path in attachments:
            part = MIMEBase("application", "octet-stream")
            with open(file_path, "rb") as f: #rb = read binary
                part.set_payload(f.read())

            encoders.encode_base64(part) #attachment encode
            part.add_header(
                "Content-Disposition",
                f'attachment; filename="{os.path.basename(file_path)}"',
            )
            message.attach(part)

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={"raw": raw_message}
    ).execute() # email send

    print(f"Gmail API email sent to {to_email}")
