from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("signup", views.signup_view, name="signup_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("dashboard", views.dashboard_view, name="dashboard_view"),
]

