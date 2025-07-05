# Gesture Translator - Django Application

A Django web application that uses computer vision and natural language processing to translate hand gestures into text and speech. This application is specifically designed for users who cannot speak, providing them with an alternative communication method.

## Features

### 🎯 Core Features
- **Hand Gesture Recognition**: Real-time gesture detection using computer vision
- **Text Translation**: Convert recognized gestures into meaningful sentences
- **Text-to-Speech**: Audio output for translated text
- **User Authentication**: Secure login and registration system
- **Session Management**: Track and manage gesture recognition sessions
- **History Tracking**: View past sessions and translations

### 🎨 User Interface
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Clean, accessible interface using Bootstrap
- **Real-time Feedback**: Live camera feed with gesture recognition overlay
- **Quick Gestures**: Pre-defined gesture buttons for common phrases
- **Customizable Settings**: Adjust recognition sensitivity and preferences

### 🔧 Technical Features
- **Django Framework**: Robust backend with PostgreSQL/SQLite support
- **REST API**: AJAX endpoints for real-time gesture processing
- **Admin Interface**: Manage users, gestures, and sessions
- **Extensible Architecture**: Easy to add new gesture types and ML models

## Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/04a96402-abf9-4f75-a4fe-da304017988f)

### User Registration
![Registration](https://github.com/user-attachments/assets/a0bb7bc7-c5fc-4d6b-80d1-b292d09d325f)

### Gesture Recognition Interface
![Gesture Recognition](https://github.com/user-attachments/assets/142928e9-d479-47f7-b2e9-b0e21ad9370b)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser with camera access

### Step 1: Clone the Repository
```bash
git clone https://github.com/Siddhu290/Machine_Learning.git
cd Machine_Learning/gesture_translator
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Load Sample Data
```bash
python manage.py shell
>>> from main.models import PredefinedGesture
>>> gestures = [
...     {"name": "hello", "description": "Waving hand gesture", "translation": "Hello, how are you?"},
...     {"name": "thanks", "description": "Putting hands together", "translation": "Thank you very much!"},
...     {"name": "help", "description": "Raising hand up", "translation": "I need help, please."},
... ]
>>> for gesture in gestures:
...     PredefinedGesture.objects.create(
...         gesture_name=gesture["name"],
...         gesture_description=gesture["description"],
...         default_translation=gesture["translation"]
...     )
>>> exit()
```

### Step 7: Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.

## Usage

### For Users

1. **Register/Login**: Create an account or log in to access gesture recognition features
2. **Dashboard**: View your session history and statistics
3. **Gesture Recognition**: 
   - Click "Start Recognition" to begin camera capture
   - Perform hand gestures in front of the camera
   - View translated text in real-time
   - Use "Speak Text" to hear the audio output
4. **Quick Gestures**: Use predefined gesture buttons for common phrases
5. **Settings**: Adjust recognition sensitivity and preferences

### For Administrators

1. **Admin Interface**: Access `/admin/` to manage users and gestures
2. **Add Gestures**: Create new predefined gestures and translations
3. **User Management**: View user activity and session history
4. **System Monitoring**: Monitor application usage and performance

## Architecture

### Models
- **UserProfile**: Extended user information and preferences
- **GestureSession**: Individual gesture recognition sessions
- **GestureTranslation**: Recorded gesture-to-text translations
- **PredefinedGesture**: Common gestures with default translations

### Views
- **Authentication**: Login, registration, user management
- **Dashboard**: User overview and statistics
- **Gesture Recognition**: Real-time gesture processing
- **History**: Session and translation history

### Templates
- **Responsive Layout**: Mobile-first design with Bootstrap
- **Real-time Updates**: JavaScript for live gesture recognition
- **Accessibility**: Screen reader compatible and keyboard navigable

## API Endpoints

### Gesture Processing
```
POST /process-gesture/
Content-Type: application/json
{
    "gesture_data": "hello"
}

Response:
{
    "success": true,
    "translated_text": "Hello, how are you?",
    "confidence": 0.85,
    "timestamp": "2024-01-15T10:30:00Z"
}
```

### Audio Generation
```
POST /generate-audio/
Content-Type: application/json
{
    "text": "Hello, how are you?"
}

Response:
{
    "success": true,
    "audio_url": "/media/audio/generated_audio.mp3",
    "message": "Audio generated successfully"
}
```

## Extending the Application

### Adding New Gesture Types
1. Create new `PredefinedGesture` objects in the admin interface
2. Update the gesture recognition algorithm to detect new patterns
3. Test the new gestures in the recognition interface

### Integrating Machine Learning Models
1. Install additional dependencies:
   ```bash
   pip install opencv-python mediapipe numpy
   ```
2. Replace the mock gesture recognition in `views.py` with actual ML models
3. Update the frontend JavaScript to handle real-time video processing

### Custom Text-to-Speech
1. Install gTTS for server-side speech generation:
   ```bash
   pip install gTTS
   ```
2. Update the `generate_audio` view to create actual audio files
3. Configure media file serving for audio playback

## Technology Stack

- **Backend**: Django 5.2.4, Python 3.8+
- **Frontend**: Bootstrap 5.1.3, JavaScript ES6, HTML5
- **Database**: SQLite (development), PostgreSQL (production)
- **Computer Vision**: OpenCV, MediaPipe (ready for integration)
- **Text-to-Speech**: Web Speech API, gTTS (ready for integration)
- **Authentication**: Django's built-in authentication system

## Browser Support

- Chrome 60+ (recommended for camera access)
- Firefox 55+
- Safari 11+
- Edge 79+

## Security

- CSRF protection enabled
- Secure authentication with session management
- Input validation and sanitization
- SQL injection protection via Django ORM

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -m 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support, questions, or feature requests:
- Open an issue on GitHub
- Contact: siddharth29m@gmail.com

## Acknowledgments

- Built with Django framework
- UI components from Bootstrap
- Icons from Font Awesome
- Inspired by accessibility and inclusive design principles

---

**Made with ❤️ for accessibility and inclusive communication**