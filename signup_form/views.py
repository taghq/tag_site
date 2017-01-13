from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.mail import send_mail

from signup_form.models import Volunteer

class SignUpVolunteer(CreateView):
    model=Volunteer
    template_name='signup_form/signup.html'
    success_url='/'
    fields = ["name", "email", "interests"]
    def form_valid(self, form):
        send_mail(
            'New Signup from %s' % (form.cleaned_data['email']) ,
            'Here is the message.',
            'bjageman@gmail.com',
            ['neurobomber@gmail.com'],
            fail_silently=False,
        )
        return super(SignUpVolunteer, self).form_valid(form)
