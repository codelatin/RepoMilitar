from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'autor', 'tutor', 'programa', 'descripcion', 'palabras_clave', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-input militar-input',
                'placeholder': 'TÍTULO DEL PROYECTO',
                'autofocus': True,
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-input militar-input',
                'placeholder': 'AUTOR',
            }),
            'tutor': forms.TextInput(attrs={
                'class': 'form-input militar-input',
                'placeholder': 'TUTOR',
            }),
            'programa': forms.TextInput(attrs={
                'class': 'form-input militar-input',
                'placeholder': 'PROGRAMA ACADÉMICO',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-input militar-textarea',
                'rows': 6,
                'placeholder': 'DESCRIPCIÓN DETALLADA DEL PROYECTO... (máx. 500 palabras)',
            }),
            'palabras_clave': forms.TextInput(attrs={
                'class': 'form-input militar-input',
                'placeholder': 'EJ: IA, CIBERSEGURIDAD, PYTHON, DASHBOARD — separadas por comas',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select militar-select',
            }),
        }