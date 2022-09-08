from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, SignInView

app_name = 'account'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
