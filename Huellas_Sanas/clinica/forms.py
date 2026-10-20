from django import forms
from django.db import transaction

from .models import Cita, Mascota


class RegistroForm(forms.Form):
    nombre = forms.CharField(
        max_length=80,
        label='Nombre de la mascota',
        widget=forms.TextInput(attrs={'autocomplete': 'off'}),
    )
    especie = forms.CharField(
        max_length=40,
        label='Especie',
        initial='Perro',
        widget=forms.TextInput(attrs={'placeholder': 'Perro, gato, ave…'}),
    )
    raza = forms.CharField(max_length=80, label='Raza', required=False)
    nombre_dueno = forms.CharField(
        max_length=120,
        label='Nombre del dueño',
        widget=forms.TextInput(attrs={'autocomplete': 'name'}),
    )
    fecha = forms.DateField(label='Fecha', widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(label='Hora', widget=forms.TimeInput(attrs={'type': 'time'}))
    motivo_consulta = forms.CharField(
        max_length=240,
        label='Motivo de consulta',
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Describe brevemente el motivo de la visita',
        }),
    )

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('fecha') and cleaned.get('hora') and Cita.objects.filter(
            fecha=cleaned['fecha'], hora=cleaned['hora']
        ).exists():
            self.add_error('hora', 'Ese bloque horario ya está ocupado. Elige otra hora.')
        return cleaned

    @transaction.atomic
    def save(self):
        mascota = Mascota.objects.create(
            nombre=self.cleaned_data['nombre'], especie=self.cleaned_data['especie'],
            raza=self.cleaned_data['raza'], nombre_dueno=self.cleaned_data['nombre_dueno'],
        )
        return Cita.objects.create(
            mascota=mascota, fecha=self.cleaned_data['fecha'], hora=self.cleaned_data['hora'],
            motivo_consulta=self.cleaned_data['motivo_consulta'],
        )
