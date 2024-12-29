from django.urls import path
from .views import RegisterViews,LoginView

urlpatterns = [
    path('register/', RegisterViews.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

]

