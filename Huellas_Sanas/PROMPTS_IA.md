# Prompts estructurados para la actividad

Estos prompts describen las tareas de IA solicitadas y sirven como registro reproducible del apoyo utilizado en la construcción.

## 1. Interfaz HTML/CSS responsive

> Actúa como diseñador frontend para una clínica veterinaria llamada “Huellas Sanas”. Genera una plantilla Django HTML accesible, en español, para una página de recepción que combine un formulario para registrar mascota (nombre, especie, raza, nombre del dueño) y cita (fecha, hora, motivo) con una tabla de citas del día (hora, mascota, dueño, motivo, estado). Incluye `{% csrf_token %}`, errores por campo, estado vacío, mensajes de éxito, filtro de fecha por GET y enlaces al Django Admin. Crea CSS responsive para móvil y escritorio, con estética cálida, limpia y profesional; no uses JavaScript ni dependencias de CSS externas. Devuelve archivos separados `agenda.html` y `estilos.css`, usando nombres de campos compatibles con modelos Django.

## 2. Datos ficticios para validar el sistema

> Genera un comando de administración Django idempotente llamado `cargar_datos_demo` que cree 20 mascotas ficticias de distintas especies y sus citas. Usa los modelos `Mascota(nombre, especie, raza, nombre_dueno)` y `Cita(mascota, fecha, hora, motivo_consulta, estado)`. Reparte las citas en fechas cercanas a la fecha actual y horas válidas sin duplicar el mismo bloque de fecha y hora. Usa `get_or_create` para que ejecutar el comando repetidamente no duplique datos. Incluye una mezcla de estados permitidos (`pendiente`, `atendida`, `cancelada`) y muestra un resumen al finalizar. No uses información personal real.

## 3. Administración de las citas generadas

> En una aplicación Django existente, registra los modelos `Mascota` y `Cita` en `admin.py`. Configura para Cita una lista con fecha, hora, mascota, motivo y estado; filtros por fecha y estado; búsqueda por nombre de mascota, dueño y motivo; jerarquía de fechas; y orden cronológico. Explica y ejecuta el flujo de Django para generar/aplicar migraciones, cargar los 20 registros de demostración con `python manage.py cargar_datos_demo` y administrarlos en `/admin/`. No inventes credenciales de superusuario: indica que se crean con `python manage.py createsuperuser`.

## Uso del framework para administrar

Desde la carpeta `Huellas_Sanas`, ejecutar:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Luego iniciar sesión en `http://127.0.0.1:8000/admin/`. La tabla de citas permite filtrar por fecha y estado; para sembrar o completar la base demo, usar `.\.venv\Scripts\python.exe manage.py cargar_datos_demo`.
