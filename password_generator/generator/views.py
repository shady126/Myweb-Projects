from django.shortcuts import render
from .models import GeneratedPassword
import random
import string

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def calculate_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Define strength criteria
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "strong", "Strong"
    elif length >= 8 and (has_upper or has_lower) and (has_digit or has_special):
        return "medium", "Medium"
    else:
        return "weak", "Weak"

def password(request):
    length = int(request.GET.get('length', 12))
    characters = string.ascii_lowercase
    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase
    if request.GET.get('numbers'):
        characters += string.digits
    if request.GET.get('special'):
        characters += string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    strength_class, strength_label = calculate_strength(generated_password)
    
    # Save password
    GeneratedPassword.objects.create(password=generated_password)

    return render(request, 'generator/password.html', {
        'password': generated_password,
        'strength': strength_class,
        'strength_label': strength_label
    })

def history(request):
    passwords = GeneratedPassword.objects.all().order_by('-created_at')[:10]
    return render(request, 'generator/history.html', {'passwords': passwords})