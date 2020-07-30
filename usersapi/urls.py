from django.urls import path, include
from knox import views as knox_views
from .views import RegisterAPIView, LoginAPIView, UserAPIView


urlpatterns = [
    path('', include('knox.urls')),
    path('register', RegisterAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]
