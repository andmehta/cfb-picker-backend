"""These views will render a template to choose a game and choose the winner and score"""
from django.urls import path
from accounts.views import login_view, logout_view

urlpatterns = [
    path("account_login/", login_view, name="login_view"),
    path("account_logout/", logout_view, name="logout_view"),
]
