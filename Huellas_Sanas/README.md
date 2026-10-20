# Huellas Sanas

Aplicación Django para registrar mascotas, agendar consultas y mantener una agenda diaria de recepción.

## Iniciar la aplicación

Desde esta carpeta, en PowerShell, ejecuta:

```powershell
.\iniciar.ps1
```

El script aplica migraciones pendientes, carga los registros ficticios de demostración y levanta el servidor con el Python del entorno `.venv`. Para elegir otro puerto, por ejemplo `8001`, usa `.\iniciar.ps1 -Direccion 127.0.0.1:8001`.

La agenda queda en `http://127.0.0.1:8000/` y Django Admin en `http://127.0.0.1:8000/admin/`. Admin requiere iniciar sesión con un superusuario local, que se crea con:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

## Si aparece “no such table: clinica_cita”

La base SQLite todavía no tiene aplicadas las migraciones. Detén el servidor y vuelve a iniciarlo con `.\iniciar.ps1`, o ejecuta manualmente, desde esta carpeta:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py cargar_datos_demo
```

## Funcionalidad

- Registro de mascota y cita en un solo formulario.
- Agenda diaria ordenada por hora, con filtro por fecha y conteo de citas pendientes.
- Bloqueo de dos citas en la misma fecha y hora.
- Gestión CRUD de mascotas y citas mediante Django Admin; las citas tienen filtros por fecha y estado, búsqueda y navegación por fecha.
- Modelos relacionados mediante ORM y base SQLite para el ejercicio.
- Datos de demostración ficticios, cargables sin duplicados con `python manage.py cargar_datos_demo`.
- Prompts estructurados de apoyo en [PROMPTS_IA.md](PROMPTS_IA.md).
