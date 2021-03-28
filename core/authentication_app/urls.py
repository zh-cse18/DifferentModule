from django.urls import path
from .views import user_login, register, user_logout, index

urlpatterns = [
    path('', index, name="posts"),
    path('login/', user_login, name="login"),
    path('register/', register, name="registration"),
    path('logout/', user_logout, name="logout"),
]
