from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView
from .views import *

urlpatterns = [
    path('login', login),
    path('o/token', TokenRefreshView.as_view()),
    path('signup', register),
    path('logout', TokenBlacklistView.as_view()),
    path('signupteacher',signupteacher),
    path('getteachers',get_teachers),
    path('approve',handle_approve),
    path('get-users', get_users)
]
