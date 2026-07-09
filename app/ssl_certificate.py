import ssl
import socket
from datetime import datetime


def get_ssl_certificate(domain):
    """
    Fetch SSL Certificate from a website
    """

    context = ssl.create_default_context()

    with socket.create_connection((domain, 443)) as sock:

        with context.wrap_socket(sock, server_hostname=domain) as secure_socket:

            certificate = secure_socket.getpeercert()

    return certificate

    # ===========================
# NEW FUNCTION STARTS HERE
# ===========================

def get_common_name(certificate):
    """
    Extract Common Name (CN) from SSL Certificate
    """

    subject = certificate.get("subject", ())

    for item in subject:
        for key, value in item:
            if key == "commonName":
                return value

    return "N/A"

def get_issuer_name(certificate):
    """
    Extract Issuer Organization Name
    """

    issuer = certificate.get("issuer", ())

    for item in issuer:
        for key, value in item:
            if key == "organizationName":
                return value

    return "N/A"

def get_expiry_date(certificate):

    expiry_date = certificate["notAfter"]

    expiry = datetime.strptime(
        expiry_date,
        "%b %d %H:%M:%S %Y %Z"
    )

    return expiry.strftime("%d %b %Y")

def calculate_remaining_days(expiry_date):
    """
    Calculate remaining days until SSL certificate expiry.
    """

    expiry = datetime.strptime(
        expiry_date,
        "%d %b %Y"
    )

    today = datetime.now()

    remaining_days = (expiry - today).days

    return remaining_days

def get_ssl_status(remaining_days):
    """
    Determine SSL Certificate Status
    """

    if remaining_days > 30:
        return "✅ SAFE"

    elif remaining_days > 7:
        return "⚠️ WARNING"

    elif remaining_days >= 0:
        return "🔴 CRITICAL"

    else:
        return "❌ EXPIRED"