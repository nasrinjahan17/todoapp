from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = "todoapp"

urlpatterns = [
    path("", index, name="index"),
    path("login/", user_login, name="login"),
    path("signup/", signup, name="signup"),
    path("profile/", profile, name="profile"),
    path("logout/", user_logout, name="logout"),
    path("add_todo/", add_todo),
    path("delete_todo/<int:id>", delete_todo, name="delete_todo"),
    path("change_status/<int:id>/<str:status>", change_todo),
    path("my_todos/", my_todos, name="my_todos"),
    # ? Password Reset with email
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="auth/forgot-password.html"),
        name="password_reset",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
]
