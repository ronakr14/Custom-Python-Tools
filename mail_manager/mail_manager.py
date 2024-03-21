# mail_manager/mail_manager.py

"""This module allows the user to make mail operations.

Examples:
    >>> from mail_manager.mail_manager import MailManager
    >>> mail_manager = MailManager(subject='abc', receiver ='abc@xyz.com', body='abc', log_file='abc.log')

    >>> receiver = ['abc@xyx.com', 'mnp@xyx.com']
    >>> attachment = ['abc.txt', 'mnp.xlsx']
    >>> sender = "abc@mnp.com"
    >>> sender_credentials = "abcd1234"
    >>> result = mail_manager.send_mail(sender=sender, sender_credentials=sender_credentials, copy_receiver=copy_receiver, attachment=attachment)

The module contains the following methods:

- `__init__(subject, receiver, body, log_file)` - creates the instance of the class.
- `send_mail(sender, sender_credentials, copy_receiver, attachment)` - sends the email.
"""

from email import encoders
from email.mime.base import MIMEBase
import inspect
import os
from log_manager import LogManager
from win32com.client import Dispatch
from typing import Union
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailManager:
    """A class for managing email operations.

    Attributes:
        log (LogManager): A LogManager instance for logging.
        service (str): The service to be used for sending the email.
        receiver (Union[list, str]): A list of email addresses or a single email address.
        subject (str): The subject of the email.
        body (str): The body of the email.
    """

    def __init__(
            self, subject: str, receiver: Union[list, str], body: str,
            service: str = 'windows', log_file: str = './Custom-Python_Tools.log') -> None:
        """
        Args:
            subject: Email Subject
            receiver: Email Receiver
            body: Email Body
            service: Service to use for sending the email.
            log_file: The path to the log file.
        """
        self.log = LogManager(log_name='MailManager', log_file=log_file)
        self.service = service
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.log.info("MailManager initialized.")

    def _copy_receiver_modify(self, copy_receiver: Union[list, str, None]) -> Union[str, None]:
        """This function takes in a list of email addresses as input and returns a string containing all the email addresses separated by a semicolon.
        If the input is not a list, it returns the input unchanged.
        
        Args:
            copy_receiver: A list of email addresses or a single email address.
        
        Returns:
            Union[str, None]: A list of email addresses separated by a semicolon or the input unchanged.
        """
        self.log.info(f"{inspect.stack()[0][3]}:\ncopy_receiver={copy_receiver}.")
        if copy_receiver:
            if isinstance(copy_receiver, list):
                self.log.info(f"copy_receiver modified = {"; ".join(copy_receiver)}.")
                return "; ".join(copy_receiver)
            else:
                self.log.info("No modification needed.")
                return copy_receiver
        else:
            self.log.info("None received in copy_receiver.")
            return None

    def _attachment_modify(self, attachment: Union[list, str, None]) -> Union[list, None]:
        """This function takes in a list of email addresses as input and returns a string containing all the email addresses separated by a semicolon.
        If the input is not a list, it returns the input unchanged.
        
        Args:
            attachment: A list of email addresses or a single email address.
        
        Returns:
            Union[list, str]: A list of email addresses separated by a semicolon or the input unchanged.
        """
        self.log.info(f"{inspect.stack()[0][3]}:\nattachment={attachment}.")
        if attachment:
            if isinstance(attachment, list):
                self.log.info("No modification needed.")
                return attachment
            else:
                self.log.info(f"attachments modified = {[attachment]}.")
                return [attachment]
        else:
            self.log.info("None received in attachment.")
            return None

    def _receiver_modify(self, receiver: Union[list, str]) -> str:
        """This function takes in a list of email addresses as input and returns a string containing all the email addresses separated by a semicolon.
        If the input is not a list, it returns the input unchanged.
        
        Args:
            receiver: A list of email addresses or a single email address.
        
        Returns:
            str: A list of email addresses separated by a semicolon or the input unchanged.
        """
        self.log.info(f"{inspect.stack()[0][3]}:\nreceiver={receiver}.")
        if isinstance(receiver, list):
            self.log.info(f"receiver modified = {"; ".join(receiver)}.")
            return "; ".join(receiver)
        else:
            self.log.info("No modification needed.")
            return receiver

    def send_mail(
            self, copy_receiver: Union[list, str, None],
            attachment: Union[list, str, None], sender: str = None,
            sender_credentials: str = None,) -> bool:
        """This function sends an email using the selected service.

        Args:
            copy_receiver: A list of email addresses or a single email address to be added as a carbon copy (CC) of the email.
            attachment: A list of email addresses or a single email address to be attached to the email.
            sender: The email address of the sender. If not specified, the default sender set in the system will be used.
            sender_credentials: The password or API key of the sender. If not specified, the default credentials set in the system will be used.
        
        Returns:
            bool: A boolean value indicating whether the email was sent successfully or not.
        
        Raises:
            ValueError: If the selected service is not supported.
        """
        self.log.info(f"{inspect.stack()[0][3]}:\ncopy_receiver={copy_receiver}, attachment={attachment}, sender={sender}, sender_credentials={sender_credentials}, service={self.service}.")
        if self.service == "windows":
            return self.windows_service(copy_receiver, attachment)
        elif self.service == "smtp":
            return self.smtp_service(sender, sender_credentials, copy_receiver, attachment)

    def _windows_service(
            self, copy_receiver: Union[list, str, None],
            attachment: Union[list, str, None]):
        """This function is used to send an email using the outlook application.

        Args:
            copy_receiver: A list of email addresses to be copied on the email.
            attachment: A list of file paths or email addresses of the attachments to be added to the email.

        Returns:
            bool: A boolean value indicating whether the email was sent successfully or not.

        Raises:
            Exception: An exception is raised if there is an error in sending the email.
        """
        self.log.info(f"{inspect.stack()[0][3]}:\ncopy_receiver={copy_receiver}, attachment={attachment}.")
        receiver = self.receiver_modify(self.receiver)
        copy_receiver = self.copy_receiver_modify(copy_receiver)
        attachment = self.attachment_modify(attachment)

        try:
            outlook = Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            self.log.info("Outlook item created.")
            mail.Subject = self.subject
            mail.To = receiver
            mail.CC = copy_receiver
            mail.HTMLBody = self.body
            for att in attachment:
                mail.Attachments.Add(att)
            mail.Send()
            self.log.info(f"Email sent with following details:\nFrom=Windows User\nTo={receiver}\nCC={copy_receiver}")
            self.log.info(f"Subject={self.subject}\nBody={self.body}\nAttachment={attachment}")
            return True
        except Exception as e:
            self.log.error(f"Undefined Error: {e}.")
            return False

    def _smtp_server(self, sender: str) -> str:
        """This function determines the SMTP server to use based on the email sender's domain.

        Args:
            sender: The email sender's domain.

        Returns:
            str: The SMTP server to use.
        """
        self.log.info(f"{inspect.stack()[0][3]}:\nsender={sender}.")
        if 'gmail.com' in sender:
            self.log.info("smtp_server=smtp.gmail.com")
            return 'smtp.gmail.com'
        else:
            self.log.info("smtp_server=smtp-mail.outlook.com")
            return 'smtp-mail.outlook.com'

    def _smtp_service(
            self, sender: str, sender_credentials: str, copy_receiver: Union[list, str, None],
            attachment: Union[list, str, None]):
        """A function to send an email through SMTP.

        Args:
            sender: The email address of the sender
            sender_credentials: The password of the sender
            copy_receiver: A list of email addresses to be copied, or a single email address
            attachment: A list of file paths to be attached, or a single file path

        Returns:
            bool: A boolean indicating whether the email was sent successfully or not
        """
        self.log.info(f"{inspect.stack()[0][3]}:\nsender={sender}, attachment={attachment}, copy_receiver={copy_receiver}.")

        receiver = self.receiver_modify(self.receiver)
        copy_receiver = self.copy_receiver_modify(copy_receiver)
        attachments = self.attachment_modify(attachment)

        flag = True
        try:
            message = MIMEMultipart()
            self.log.info("MIME item created.")
            message['From'] = sender
            message['To'] = receiver
            message['Bcc'] = copy_receiver
            message['Subject'] = self.subject

            message.attach(MIMEText(self.body, 'plain'))

            for file in attachments:
                file = os.path.basename(file)
                with open(file, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {file}',
                    )
                    message.attach(part)
                self.log.info(f"{file} attached.")

            server = smtplib.SMTP(self.smtp_server(sender), 587)
            server.starttls()
            server.login(sender, sender_credentials)
            text = message.as_string()
            server.sendmail(sender, receiver, text)
            self.log.info(f"Email sent with following details:\nFrom={sender}\nTo={receiver}\nCC={copy_receiver}")
            self.log.info(f"Subject={self.subject}\nBody={self.body}\nAttachment={attachment}")

        except smtplib.SMTPException as e:
            flag = False
            self.log.error("SMTP error occurred:", e)
        except Exception as e:
            flag = False
            self.log.error("An error occurred:", e)

        finally:
            server.quit()
            self.log.info("SMTP server closed successfully.")
            return flag
