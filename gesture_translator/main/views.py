from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json
import os
from .models import UserProfile, GestureSession, GestureTranslation, PredefinedGesture


def home(request):
    """Home page view"""
    return render(request, 'main/home.html')


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    """User dashboard view"""
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    # Get recent sessions
    recent_sessions = GestureSession.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]
    
    # Get recent translations
    recent_translations = GestureTranslation.objects.filter(
        session__user=request.user
    ).order_by('-timestamp')[:10]
    
    context = {
        'profile': profile,
        'recent_sessions': recent_sessions,
        'recent_translations': recent_translations,
    }
    return render(request, 'main/dashboard.html', context)


def gesture_recognition(request):
    """Gesture recognition page"""
    # For demo purposes, create a temporary session if no user is logged in
    if request.user.is_authenticated:
        # Get or create active session
        session, created = GestureSession.objects.get_or_create(
            user=request.user,
            is_active=True,
            defaults={'session_name': f'Session {GestureSession.objects.filter(user=request.user).count() + 1}'}
        )
    else:
        # Create a demo session
        session = type('DemoSession', (), {
            'session_name': 'Demo Session',
            'user': type('DemoUser', (), {'username': 'Demo User'})()
        })()
    
    # Get predefined gestures
    predefined_gestures = PredefinedGesture.objects.filter(is_active=True)
    
    context = {
        'session': session,
        'predefined_gestures': predefined_gestures,
    }
    return render(request, 'main/gesture_recognition.html', context)


@csrf_exempt
@require_http_methods(["POST"])
@login_required
def process_gesture(request):
    """Process gesture data and return translation"""
    try:
        data = json.loads(request.body)
        gesture_data = data.get('gesture_data', '')
        
        # For now, return a simple mock translation
        # In a real implementation, this would use ML models
        mock_translations = {
            'hello': 'Hello, how are you?',
            'thanks': 'Thank you very much!',
            'help': 'I need help, please.',
            'water': 'I would like some water.',
            'food': 'I am hungry.',
            'yes': 'Yes, I agree.',
            'no': 'No, I disagree.',
            'please': 'Please help me.',
            'sorry': 'I am sorry.',
            'goodbye': 'Goodbye, see you later.'
        }
        
        # Simple gesture recognition (mock)
        gesture_text = gesture_data.lower()
        translated_text = mock_translations.get(gesture_text, "Gesture not recognized. Please try again.")
        
        # Get active session
        session = GestureSession.objects.filter(
            user=request.user,
            is_active=True
        ).first()
        
        if session:
            # Save translation
            translation = GestureTranslation.objects.create(
                session=session,
                gesture_text=gesture_text,
                translated_text=translated_text,
                confidence_score=0.85 if gesture_text in mock_translations else 0.1
            )
            
            return JsonResponse({
                'success': True,
                'translated_text': translated_text,
                'confidence': translation.confidence_score,
                'timestamp': translation.timestamp.isoformat()
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'No active session found'
            })
            
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


@csrf_exempt
@require_http_methods(["POST"])
@login_required
def generate_audio(request):
    """Generate audio for translated text"""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        
        if not text:
            return JsonResponse({
                'success': False,
                'error': 'No text provided'
            })
        
        # Mock audio generation (would use TTS in real implementation)
        # For now, just return success with a placeholder
        return JsonResponse({
            'success': True,
            'audio_url': '/static/audio/placeholder.mp3',
            'message': 'Audio generation feature coming soon!'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


@login_required
def session_history(request):
    """View session history"""
    sessions = GestureSession.objects.filter(
        user=request.user
    ).order_by('-created_at')
    
    context = {'sessions': sessions}
    return render(request, 'main/session_history.html', context)


@login_required
def session_detail(request, session_id):
    """View details of a specific session"""
    try:
        session = GestureSession.objects.get(
            id=session_id,
            user=request.user
        )
        translations = GestureTranslation.objects.filter(
            session=session
        ).order_by('-timestamp')
        
        context = {
            'session': session,
            'translations': translations
        }
        return render(request, 'main/session_detail.html', context)
        
    except GestureSession.DoesNotExist:
        messages.error(request, 'Session not found.')
        return redirect('session_history')
