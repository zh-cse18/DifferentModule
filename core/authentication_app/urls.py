from django.urls import path
from .views import user_login, register, user_logout, change_password, activate_account
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
urlpatterns = [
    path('login/', user_login, name="login"),
    path('register/', register, name="registration"),
    path('logout/', user_logout, name="logout"),
    path('change_pass/', change_password, name="changepass"),

    #pass reset related
    path('reset/password/', PasswordResetView.as_view(template_name='authentication/reset_pass.html'), name="password_reset"),
    path('reset/password/done/', PasswordResetDoneView.as_view(template_name='authentication/reset_pass_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', PasswordResetView.as_view(template_name='authentication/password_reset_complete.html'), name="password_reset_complete"),
    path('activate/<uidb64>/<token>/', activate_account, name="activate_account"),
]
