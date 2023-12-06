from django.urls import path
from .views import CreateUserView

urlpatterns = [
    path('sign-up/', CreateUserView.as_view()),
]
