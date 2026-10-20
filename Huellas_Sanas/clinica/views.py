from datetime import date

from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegistroForm
from .models import Cita


def agenda(request):
    filtro_fecha = forms.DateField(required=False)
    fecha_seleccionada = date.today()
    fecha_recibida = request.GET.get('fecha')
    if fecha_recibida:
        try:
            fecha_seleccionada = filtro_fecha.clean(fecha_recibida)
        except forms.ValidationError:
            messages.error(request, 'La fecha indicada no es válida. Se muestra la agenda de hoy.')
    citas = Cita.objects.select_related('mascota').filter(fecha=fecha_seleccionada)
    form = RegistroForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La mascota y su cita quedaron registradas.')
        return redirect(f"{reverse('agenda')}?fecha={form.cleaned_data['fecha'].isoformat()}")
    return render(request, 'clinica/agenda.html', {
        'form': form, 'citas': citas, 'fecha_seleccionada': fecha_seleccionada.isoformat(),
        'pendientes': citas.filter(estado=Cita.Estado.PENDIENTE).count(),
    })
