from django.forms import ModelForm
from .models import *

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile

        fields = ['user', 'nombre_completo', 'apellidos', 'fecha_nacimiento', 'email']

        labels = {
            'nombre_completo': 'Nombre completo',
            'apellidos': 'Apellidos',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'email': 'Correo electrónico',
        }


class DiarioMikiForm(ModelForm):
    class Meta:
        model = DiarioMiki

        fields = ['user', 'titulo', 'contenido']

        labels = {
            'user': 'Usuario',
            'titulo': 'Título',
            'contenido': 'Contenido',
        }