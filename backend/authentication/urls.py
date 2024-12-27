from django.urls import path
from .views import RegisterViews

urlpatterns = [
    path('register/', RegisterViews.as_view(), name='register'),

]

