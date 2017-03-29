from django.views.generic import FormView

from .mixins import AjaxableResponseMixin
from .forms import EmailSendForm
from .utils import email_send


# Create your views here.
class EmailSendView(AjaxableResponseMixin, FormView):
    form_class = EmailSendForm
    http_method_names = [u'post']

    def form_valid(self, form):
        data = form.cleaned_data
        email_send(
            email=data['email'],
            to_email='inquire@spectrumone.co',
            subject=data['subject'],
            content=data['message']
        )

        return super(EmailSendView, self).form_valid(form)
