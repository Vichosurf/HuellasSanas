# Huellas Sanas

Aplicación Django para registrar mascotas, agendar consultas y mantener una agenda diaria de recepción.

## Iniciar la aplicación

Desde esta carpeta, en PowerShell:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py cargar_datos_demo
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

La agenda de recepción queda en `http://127.0.0.1:8000/`. Django Admin está en `http://127.0.0.1:8000/admin/` y requiere iniciar sesión con el superusuario creado localmente. El comando de datos demo se puede volver a ejecutar sin duplicar las mascotas y citas de ejemplo.

## Funcionalidad

- Registro de mascota y cita en un solo formulario.
- Agenda diaria ordenada por hora, con filtro por fecha y conteo de citas pendientes.
- Bloqueo de dos citas en la misma fecha y hora.
- Gestión CRUD de mascotas y citas mediante Django Admin; las citas tienen filtros por fecha y estado, búsqueda y navegación por fecha.
- Modelos relacionados mediante ORM y base SQLite para el ejercicio.
- Prompts estructurados de apoyo en [PROMPTS_IA.md](PROMPTS_IA.md).

Los registros de demostración son ficticios. Para regenerarlos en una base vacía, ejecutar `python manage.py cargar_datos_demo`.
