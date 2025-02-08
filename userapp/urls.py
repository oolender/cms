from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


# Define a list of url patterns
urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', LogoutView.as_view(next_page="/login"), name="logout"),
    path('register/', views.register_view, name="register"),
]
