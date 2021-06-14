from django.urls import path
from .views import user_login, register, user_logout, change_password
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView,\
    PasswordResetConfirmView
urlpatterns = [
    path('login/', user_login, name="login"),
    path('register/', register, name="registration"),
    path('logout/', user_logout, name="logout"),
    path('change_pass/', change_password, name="changepass"),

    path('reset/password/', PasswordResetView.as_view(template_name='reset_pass.html'), name="password_reset"),
    path('reset/password/done/', PasswordResetDoneView.as_view(template_name='reset_pass_done.html'), name="reset_pass_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', PasswordResetView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),

]
