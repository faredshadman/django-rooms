from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields= '__all__'