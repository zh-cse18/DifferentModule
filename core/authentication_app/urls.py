from django.urls import path
from .views import user_login, register, user_logout, change_password
from django.contrib.auth.views import PasswordResetView,PasswordChangeDoneView, PasswordResetCompleteView,\
    PasswordResetConfirmView
urlpatterns = [
    path('login/', user_login, name="login"),
    path('register/', register, name="registration"),
    path('logout/', user_logout, name="logout"),
    path('change_pass/', change_password, name="changepass"),
    path('reset/password/', PasswordResetView.as_view(template_name='password_reset.html'), name="pass_reset "),
    path('reset/password/done/', PasswordChangeDoneView.as_view(template_name='password_reset_done.html'), name="reset_pass_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirmation.html'), name="reset_pass_confirmation"),
    path('reset/done/', PasswordChangeDoneView.as_view(template_name='password_reset_done.html'), name="reset_pass_done"),

]
