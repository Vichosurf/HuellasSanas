# Huellas Sanas

Aplicación Django para registrar mascotas, agendar consultas y mantener una agenda diaria de recepción.

## Iniciar la aplicación

Desde esta carpeta, en PowerShell, ejecuta:

```powershell
.\iniciar.ps1
```

El script aplica migraciones pendientes, carga los registros ficticios de demostración y levanta el servidor con Python del entorno `.venv`. Para elegir otro puerto puedes usar `.\iniciar.ps1 -Direccion 127.0.0.1:8001`.

La agenda queda en `http://127.0.0.1:8000/` y Django Admin en `http://127.0.0.1:8000/admin/`. Admin requiere un superusuario local, que se crea con:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

## Agregar mascotas de demostración con JSON

Los datos están en [clinica/data/mascotas_demo.json](clinica/data/mascotas_demo.json). Cada objeto crea una mascota y su primera cita. Agrega un objeto a la lista con esta estructura:

```json
{
  "nombre": "Nube",
  "especie": "Perro",
  "raza": "Mestizo",
  "nombre_dueno": "Alex Rivera",
  "motivo_consulta": "Control general",
  "estado": "pendiente",
  "dias_desde_hoy": 0,
  "hora": "14:00"
}
```

Usa un horario libre para la fecha indicada y uno de estos estados: `pendiente`, `atendida` o `cancelada`. Guarda el JSON y ejecuta:

```powershell
.\.venv\Scripts\python.exe manage.py cargar_datos_demo
```

El comando no duplica las mascotas ni sus citas si se ejecuta otra vez. Para agregar una mascota sin cita todavía, usa Django Admin en **Mascotas → Añadir mascota**.

## Si aparece “no such table: clinica_cita”

La base SQLite no tiene aplicadas las migraciones. Detén el servidor y vuelve a iniciarlo con `.\iniciar.ps1`, o ejecuta desde esta carpeta:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py cargar_datos_demo
```

## Funcionalidad

- Registro de mascota y cita en un formulario.
- Agenda diaria por hora, filtro por fecha y conteo de citas pendientes.
- Validación para impedir dos citas en la misma fecha y hora.
- Gestión CRUD de mascotas y citas en Django Admin, con filtros por fecha y estado.
- Modelos ORM relacionados y base SQLite local.
