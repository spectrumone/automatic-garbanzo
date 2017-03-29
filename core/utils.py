from django.conf import settings
import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail
import environ


def email_send(email, to_email, subject, content):
    env = environ.Env()
    env.read_env()

    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email(email)
    to_email = Email(to_email)
    subject = subject
    content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    return response.status_code
