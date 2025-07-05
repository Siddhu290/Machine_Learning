from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('gesture-recognition/', views.gesture_recognition, name='gesture_recognition'),
    path('process-gesture/', views.process_gesture, name='process_gesture'),
    path('generate-audio/', views.generate_audio, name='generate_audio'),
    path('session-history/', views.session_history, name='session_history'),
    path('session/<int:session_id>/', views.session_detail, name='session_detail'),
]