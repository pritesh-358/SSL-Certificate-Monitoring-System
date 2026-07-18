"""
====================================================================
SSL Certificate Monitoring System
====================================================================

Email Sender Module

Author  : Pritesh Thamke
Version : 4.0

Description
-----------
Professional Email Sender Module

Supports

✔ HTML Email
✔ CSV Attachment
✔ Multiple TO
✔ Multiple CC
✔ Multiple BCC
✔ Gmail SMTP
✔ .env Support

====================================================================
"""

# ==============================================================
# IMPORT MODULES
# ==============================================================

import os

import smtplib

from email.mime.text import MIMEText

from email.mime.base import MIMEBase

from email.mime.multipart import MIMEMultipart

from email import encoders

from dotenv import load_dotenv

from config_reader import load_config


# ==============================================================
# LOAD CONFIGURATION
# ==============================================================

load_dotenv()

print("Current Working Directory:", os.getcwd())
print("SMTP_SERVER:", os.getenv("SMTP_SERVER"))
print("SMTP_PORT:", os.getenv("SMTP_PORT"))
print("ENV file exists:", os.path.exists(".env"))

config = load_config()


# ==============================================================
# SMTP CONFIGURATION
# ==============================================================

SMTP_SERVER = os.getenv("SMTP_SERVER")

SMTP_PORT = int(os.getenv("SMTP_PORT"))

SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")

SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")

# ==============================================================
# SEND EMAIL
# ==============================================================

def send_email(
    to_emails,
    cc_emails,
    bcc_emails,
    subject,
    body,
    attachment_path
):
    """
    Send HTML Email with CSV Attachment
    """

    try:

        # ==========================================================
        # CREATE EMAIL
        # ==========================================================

        message = MIMEMultipart()

        message["From"] = SENDER_EMAIL

        message["To"] = ", ".join(to_emails)

        message["Cc"] = ", ".join(cc_emails)

        message["Subject"] = subject

        # ==========================================================
        # HTML BODY
        # ==========================================================

        message.attach(
            MIMEText(body, "html")
        )

        # ==========================================================
        # ATTACH REPORT
        # ==========================================================

        if os.path.exists(attachment_path):

            with open(
                attachment_path,
                "rb"
            ) as attachment:

                part = MIMEBase(
                    "application",
                    "octet-stream"
                )

                part.set_payload(
                    attachment.read()
                )

            encoders.encode_base64(part)

            filename = os.path.basename(
                attachment_path
            )

            part.add_header(

                "Content-Disposition",

                f'attachment; filename="{filename}"'

            )

            message.attach(part)

        else:

            print("Attachment file not found.")

        # ==========================================================
        # SMTP CONNECTION
        # ==========================================================

        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        )

        server.starttls()

        server.login(
            SENDER_EMAIL,
            SENDER_PASSWORD
        )

        # ==========================================================
        # ALL RECEIVERS
        # ==============================================================

        all_receivers = (
            to_emails +
            cc_emails +
            bcc_emails
        )

        # ==========================================================
        # SEND EMAIL
        # ==============================================================

        server.sendmail(
            SENDER_EMAIL,
            all_receivers,
            message.as_string()
        )

        server.quit()

        print("=" * 70)
        print("Email Sent Successfully")
        print("=" * 70)

        print("TO")

        for email in to_emails:
            print(f"   {email}")

        if cc_emails:

            print("\nCC")

            for email in cc_emails:

                print(f"   {email}")

        if bcc_emails:

            print("\nBCC")

            for email in bcc_emails:

                print(f"   {email}")

        print("=" * 70)

        return True

    # ==============================================================
    # ERROR HANDLING
    # ==============================================================

    except FileNotFoundError:

        print("=" * 70)
        print("Attachment file not found.")
        print("=" * 70)

        return False

    except smtplib.SMTPAuthenticationError:

        print("=" * 70)
        print("SMTP Authentication Failed.")
        print("Check EMAIL_ADDRESS and EMAIL_PASSWORD.")
        print("=" * 70)

        return False

    except smtplib.SMTPException as error:

        print("=" * 70)
        print("SMTP Error")
        print(error)
        print("=" * 70)

        return False

    except Exception as error:

        print("=" * 70)
        print("Unexpected Error")
        print(error)
        print("=" * 70)

        return False