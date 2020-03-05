from django.urls import path
from login_django.views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),
]

