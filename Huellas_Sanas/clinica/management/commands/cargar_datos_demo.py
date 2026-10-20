import json
from datetime import date, time, timedelta
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError, transaction

from clinica.models import Cita, Mascota


class Command(BaseCommand):
    help = 'Carga mascotas y citas ficticias desde clinica/data/mascotas_demo.json.'

    @transaction.atomic
    def handle(self, *args, **options):
        archivo_datos = Path(__file__).resolve().parents[2] / 'data' / 'mascotas_demo.json'
        try:
            pacientes = json.loads(archivo_datos.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError) as error:
            raise CommandError(f'No se pudo leer {archivo_datos}: {error}') from error

        if not isinstance(pacientes, list):
            raise CommandError('El JSON debe contener una lista de mascotas.')

        citas_nuevas = 0
        for numero, paciente in enumerate(pacientes, start=1):
            try:
                nombre = paciente['nombre'].strip()
                especie = paciente['especie'].strip()
                raza = paciente.get('raza', '').strip()
                dueno = paciente['nombre_dueno'].strip()
                motivo = paciente['motivo_consulta'].strip()
                estado = paciente['estado']
                fecha = date.today() + timedelta(days=int(paciente['dias_desde_hoy']))
                hora = time.fromisoformat(paciente['hora'])
            except (KeyError, AttributeError, TypeError, ValueError) as error:
                raise CommandError(f'Revisa el objeto {numero} de {archivo_datos.name}: {error}') from error

            if not all((nombre, especie, dueno, motivo)):
                raise CommandError(f'El objeto {numero} debe incluir nombre, especie, dueño y motivo.')
            if estado not in Cita.Estado.values:
                opciones = ', '.join(Cita.Estado.values)
                raise CommandError(f'Estado inválido en objeto {numero}: usa {opciones}.')

            mascota, _ = Mascota.objects.get_or_create(
                nombre=nombre,
                nombre_dueno=dueno,
                defaults={'especie': especie, 'raza': raza},
            )
            if Cita.objects.filter(fecha=fecha, hora=hora).exclude(mascota=mascota).exists():
                raise CommandError(
                    f'El horario {fecha} {hora:%H:%M} del objeto {numero} ya está ocupado.'
                )

            try:
                _, creada = Cita.objects.get_or_create(
                    mascota=mascota,
                    fecha=fecha,
                    hora=hora,
                    defaults={'motivo_consulta': motivo, 'estado': estado},
                )
            except IntegrityError as error:
                raise CommandError(
                    f'No se pudo crear la cita del objeto {numero}; revisa que el horario sea único.'
                ) from error
            citas_nuevas += int(creada)

        self.stdout.write(self.style.SUCCESS(
            f'Datos demo listos: {Mascota.objects.count()} mascotas en total; '
            f'{citas_nuevas} citas nuevas en esta ejecución.'
        ))
