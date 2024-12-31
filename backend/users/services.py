import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from backend.config.common import Common  # Assuming Common is imported correctly
import random

# Initialize logger
logger = logging.getLogger('smtp')

class EmailVerificationService:
    def __init__(self):
        # Use the SMTP settings from Common
        self.smtp_host = Common.EMAIL_HOST
        self.smtp_port = Common.EMAIL_PORT
        self.smtp_user = Common.EMAIL_HOST_USER
        self.smtp_password = Common.EMAIL_HOST_PASSWORD
        self.smtp_use_tls = Common.EMAIL_USE_TLS
        self.default_from_email = Common.DEFAULT_FROM_EMAIL
        self.verification_code = None

    def generate_verification_code(self):
        self.verification_code = str(random.randint(100000, 999999)) # Generate a 6-digit random code
        return self.verification_code

    def send_email_verification_code(self, email_address, verification_code=None):
        # Use the provided verification code if available, else use the instance one
        code = verification_code if verification_code else self.verification_code
        subject = "Your Email Verification Code"
        message = f"Your verification code is: {code}"
    
        # Email details
        sender_email = self.default_from_email
        receiver_email = email_address
    
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
    
        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                if self.smtp_use_tls:
                    server.starttls()  # Upgrade to a secure connection
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
    
            logger.info(f"Sent email verification code '{code}' to {email_address}.")
            return True
        except Exception as e:
            logger.error(f"Failed to send email verification code to {email_address}. Error: {str(e)}")
            return False


    def verify_code(self, input_code):
        is_valid = input_code == self.verification_code
        logger.info(f"Verification {'succeeded' if is_valid else 'failed'} for code: {input_code}")
        return is_valid
