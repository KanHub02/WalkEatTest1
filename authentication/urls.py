from django.urls import path

from .views import RegistrationAPIview

app_name = 'authentication'
urlpatterns = [
    path("api/users/", RegistrationAPIview.as_view()),
]