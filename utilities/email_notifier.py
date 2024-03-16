import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

class EmailNotifier:
    def __init__(self, email, password, smtp_server='smtp.gmail.com', smtp_port=587):
        """
        Initializes the EmailNotifier.

        :param email: The email address from which to send notifications.
        :param password: The password for the email account.
        :param smtp_server: The SMTP server address (default is Gmail).
        :param smtp_port: The SMTP server port (default is 587 for Gmail).
        """
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_notification(self, recipient, subject, message):
        """
        Sends an email notification.

        :param recipient: The recipient's email address.
        :param subject: The subject of the email.
        :param message: The body of the email.
        """
        try:
            # Set up the SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)

            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Send email
            server.sendmail(self.email, recipient, msg.as_string())
            logging.info("Email notification sent successfully")

            # Close connection
            server.quit()
        except Exception as e:
            logging.error(f"Failed to send email notification: {e}")
# Email Notifier 
