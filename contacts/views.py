from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from ToDo_settings.settings import NOREPLY_TODO_EMAIL
from contacts.forms import ContactForm


class ContactView(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = 'contacts/contact_us.html'
    success_url = reverse_lazy('email_sent')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            mail_subject = form.cleaned_data['subject']
            message = form.cleaned_data['text']
            send_mail(mail_subject,
                      message,
                      request.user.email,
                      [NOREPLY_TODO_EMAIL]
                      )
            return self.form_valid(form)
        return self.form_invalid(form)


class EmailSent(TemplateView):
    template_name = 'contacts/email_sent_confirm.html'
