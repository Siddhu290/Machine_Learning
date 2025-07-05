from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} Profile"


class GestureSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.session_name}"


class GestureTranslation(models.Model):
    session = models.ForeignKey(GestureSession, on_delete=models.CASCADE)
    gesture_text = models.TextField()
    translated_text = models.TextField()
    audio_file = models.FileField(upload_to='audio/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    confidence_score = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"{self.session.user.username} - {self.translated_text[:50]}"


class PredefinedGesture(models.Model):
    gesture_name = models.CharField(max_length=100)
    gesture_description = models.TextField()
    default_translation = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.gesture_name
