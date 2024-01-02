from django.urls import path

from user.views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path('auth/register/', register_view),
    path('auth/login/', login_view),
    path('auth/logout', logout_view),
    path('auth/profile/', profile_view)
]