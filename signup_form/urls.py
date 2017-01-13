from django.conf.urls import url, include
from signup_form.views import SignUpVolunteer


urlpatterns = [
            url(r'^$', SignUpVolunteer.as_view(), name="signup_form"),
            ]
