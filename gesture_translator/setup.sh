#!/bin/bash

# Gesture Translator Setup Script
echo "🤟 Gesture Translator Setup Script"
echo "=================================="

# Check Python version
python_version=$(python3 --version 2>&1)
echo "✓ Found Python: $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "⬇️  Installing dependencies..."
pip install -r requirements.txt

# Set up database
echo "🗄️  Setting up database..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "👤 Creating superuser..."
echo "Please enter details for the admin user:"
python manage.py createsuperuser

# Load sample gestures
echo "🤲 Loading sample gestures..."
python manage.py shell -c "
from main.models import PredefinedGesture
gestures = [
    {'name': 'hello', 'description': 'Waving hand gesture', 'translation': 'Hello, how are you?'},
    {'name': 'thanks', 'description': 'Putting hands together', 'translation': 'Thank you very much!'},
    {'name': 'help', 'description': 'Raising hand up', 'translation': 'I need help, please.'},
    {'name': 'water', 'description': 'Cup-like hand gesture', 'translation': 'I would like some water.'},
    {'name': 'food', 'description': 'Hand to mouth gesture', 'translation': 'I am hungry.'},
    {'name': 'yes', 'description': 'Thumbs up gesture', 'translation': 'Yes, I agree.'},
    {'name': 'no', 'description': 'Shaking head with hands', 'translation': 'No, I disagree.'},
    {'name': 'please', 'description': 'Open palm gesture', 'translation': 'Please help me.'},
    {'name': 'sorry', 'description': 'Hand on chest', 'translation': 'I am sorry.'},
    {'name': 'goodbye', 'description': 'Waving goodbye', 'translation': 'Goodbye, see you later.'}
]
for gesture in gestures:
    PredefinedGesture.objects.get_or_create(
        gesture_name=gesture['name'],
        defaults={
            'gesture_description': gesture['description'],
            'default_translation': gesture['translation']
        }
    )
print('Sample gestures loaded successfully!')
"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the development server:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit http://127.0.0.1:8000 in your browser"
echo ""
echo "Admin interface: http://127.0.0.1:8000/admin/"
echo ""
echo "Have fun with gesture translation! 🤟"