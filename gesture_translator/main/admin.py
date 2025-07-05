from django.contrib import admin
from .models import UserProfile, GestureSession, GestureTranslation, PredefinedGesture


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'last_activity')
    list_filter = ('created_at', 'last_activity')
    search_fields = ('user__username', 'user__email')


@admin.register(GestureSession)
class GestureSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_name', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active')
    search_fields = ('user__username', 'session_name')


@admin.register(GestureTranslation)
class GestureTranslationAdmin(admin.ModelAdmin):
    list_display = ('session', 'translated_text', 'timestamp', 'confidence_score')
    list_filter = ('timestamp', 'confidence_score')
    search_fields = ('session__user__username', 'translated_text')


@admin.register(PredefinedGesture)
class PredefinedGestureAdmin(admin.ModelAdmin):
    list_display = ('gesture_name', 'default_translation', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('gesture_name', 'default_translation')
