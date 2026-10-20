from datetime import date, time, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction

from clinica.models import Cita, Mascota


class Command(BaseCommand):
    help = 'Crea 20 pacientes ficticios y sus citas de demostración.'

    @transaction.atomic
    def handle(self, *args, **options):
        pacientes = [
            ('Luna', 'Perro', 'Golden Retriever', 'Camila Rojas', 'Control anual'),
            ('Michi', 'Gato', 'Doméstico de pelo corto', 'Diego Pérez', 'Vacunación triple felina'),
            ('Toby', 'Perro', 'Poodle', 'Valentina Soto', 'Picazón en la piel'),
            ('Nala', 'Gato', 'Siamés', 'Francisca Díaz', 'Control de peso'),
            ('Rocky', 'Perro', 'Labrador', 'Tomás Muñoz', 'Dolor en una pata'),
            ('Mora', 'Perro', 'Mestiza', 'Javiera Silva', 'Examen preventivo'),
            ('Simba', 'Gato', 'Naranja', 'Matías Torres', 'Refuerzo de vacuna'),
            ('Kira', 'Perro', 'Pastor alemán', 'Daniela Flores', 'Consulta digestiva'),
            ('Coco', 'Ave', 'Cacatúa ninfa', 'Andrés Herrera', 'Revisión de plumaje'),
            ('Doki', 'Perro', 'Beagle', 'Paula Castro', 'Limpieza dental'),
            ('Pelusa', 'Conejo', 'Cabeza de león', 'Nicolás Vargas', 'Control de uñas'),
            ('Max', 'Perro', 'Bulldog francés', 'Carolina Fuentes', 'Tos persistente'),
            ('Lola', 'Gato', 'Mestiza', 'Sebastián Reyes', 'Esterilización: evaluación'),
            ('Bobby', 'Perro', 'Cocker spaniel', 'Antonia Espinoza', 'Otitis'),
            ('Chispa', 'Hamster', 'Sirio', 'Felipe Navarro', 'Control general'),
            ('Milo', 'Gato', 'British shorthair', 'Constanza Vidal', 'Pérdida de apetito'),
            ('Canela', 'Perro', 'Dachshund', 'Ignacio Campos', 'Vacunación antirrábica'),
            ('Pipa', 'Perro', 'Chihuahua', 'Belén Morales', 'Revisión postoperatoria'),
            ('Oreo', 'Gato', 'Bicolor', 'Gabriel Castillo', 'Lagrimeo en un ojo'),
            ('Flor', 'Cobaya', 'Americana', 'Josefina León', 'Evaluación preventiva'),
        ]
        estados = [Cita.Estado.PENDIENTE, Cita.Estado.ATENDIDA, Cita.Estado.PENDIENTE,
                   Cita.Estado.CANCELADA, Cita.Estado.PENDIENTE]
        creadas = 0
        for index, (nombre, especie, raza, dueno, motivo) in enumerate(pacientes):
            mascota, creada = Mascota.objects.get_or_create(
                nombre=nombre, nombre_dueno=dueno,
                defaults={'especie': especie, 'raza': raza},
            )
            fecha = date.today() + timedelta(days=index % 7 - 3)
            hora = time(9 + index // 4, (index % 4) * 15)
            _, cita_creada = Cita.objects.get_or_create(
                mascota=mascota, fecha=fecha, hora=hora,
                defaults={'motivo_consulta': motivo, 'estado': estados[index % len(estados)]},
            )
            creadas += int(cita_creada)
        self.stdout.write(self.style.SUCCESS(
            f'Datos demo listos: {Mascota.objects.count()} mascotas en total; {creadas} citas nuevas en esta ejecución.'
        ))
