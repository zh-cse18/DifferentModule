from django.urls import path
from .views import user_login, register, user_logout, change_password

urlpatterns = [
    path('login/', user_login, name="login"),
    path('register/', register, name="registration"),
    path('logout/', user_logout, name="logout"),
    path('change_pass/', change_password, name="changepass"),
]
