# Huellas Sanas

Sistema web para centralizar el registro de pacientes veterinarios y la agenda de consultas de la clínica **Huellas Sanas**.

## Problema que resuelve

La recepción administraba las atenciones con una combinación de agendas de papel y mensajes de WhatsApp. Al crecer la cantidad de pacientes, esa información dispersa empezó a provocar problemas concretos:

- Dos pacientes podían quedar citados para la misma fecha y hora.
- Una cita podía no llegar a la agenda que revisaba el equipo veterinario.
- El motivo de consulta podía perderse entre mensajes.
- Al llegar a la clínica, los dueños podían descubrir que su cita no estaba registrada.
- Era difícil consultar rápidamente qué pacientes debían atenderse durante el día.

Huellas Sanas guarda estos datos en una base centralizada. Recepción puede registrar la mascota junto con su primera cita y revisar la agenda por fecha. El sistema ordena las citas por hora y bloquea la duplicación de una fecha y hora. La administración puede consultar y modificar los registros desde Django Admin.

## Funcionalidades principales

- Formulario web para registrar una mascota y su cita: nombre, especie, raza, dueño, fecha, hora y motivo.
- Agenda diaria que se puede consultar para otras fechas.
- Visualización del paciente, dueño, motivo y estado de cada cita.
- Estados disponibles: `pendiente`, `atendida` y `cancelada`.
- Validación para evitar dos citas en el mismo bloque horario.
- Gestión de mascotas y citas con operaciones CRUD en Django Admin.
- Filtros administrativos por fecha y estado de la cita, además de búsqueda de pacientes y motivos.
- Carga de pacientes ficticios desde un archivo JSON para demostrar el sistema.
- Diseño adaptable a pantallas de escritorio y teléfonos.

## Tecnologías utilizadas

| Tecnología | Uso en el proyecto |
| --- | --- |
| **Python** | Lenguaje de programación de las vistas, formularios, modelos y comandos de gestión. |
| **Django 6.1** | Framework web: maneja las rutas, solicitudes, validación de formularios, plantillas, sesiones y administración. |
| **Django ORM** | Define los modelos y consulta la base de datos usando objetos Python. |
| **SQLite** | Base de datos local del ejercicio. Django la crea y actualiza al aplicar las migraciones. |
| **HTML** | Estructura de la página de recepción y la agenda. |
| **CSS** | Presentación visual y adaptación a distintos tamaños de pantalla. |
| **JSON** | Archivo de datos ficticios que consume el comando `cargar_datos_demo`. |
| **PowerShell** | Consola usada para ejecutar los comandos de Django en Windows. |

La interfaz no requiere un framework JavaScript ni una base de datos externa para funcionar en este ejercicio.

## Modelos de datos

### Mascota

Cada registro guarda el nombre de la mascota, especie, raza y nombre del dueño.

### Cita

Cada cita se relaciona con una mascota y guarda fecha, hora, motivo de consulta y estado. La base de datos impone que no se repita la combinación de fecha y hora.

La relación es de **una mascota a muchas citas**: una mascota puede volver a la clínica y tener más de una consulta a lo largo del tiempo.

## Recorrido de uso

1. Recepción abre la agenda y registra al paciente y su primera consulta.
2. Django valida los campos y comprueba que el horario esté libre.
3. La información se guarda en SQLite mediante los modelos ORM.
4. La cita queda visible en la agenda de su fecha.
5. El director inicia sesión en Django Admin para revisar, buscar, editar o eliminar mascotas y citas, y cambiar el estado de una cita.

## Tecnologías y estructura del proyecto

- `config/settings.py`: aplicaciones, idioma español, zona horaria de Santiago y base de datos.
- `config/urls.py`: rutas del proyecto y acceso al panel administrativo.
- `clinica/models.py`: modelos `Mascota` y `Cita`.
- `clinica/forms.py`: validación y guardado del registro de mascota y cita.
- `clinica/views.py` y `clinica/urls.py`: lógica y rutas de la agenda.
- `clinica/templates/clinica/agenda.html`: plantilla de recepción.
- `clinica/static/clinica/estilos.css`: estilos responsive.
- `clinica/admin.py`: configuración de los modelos en Django Admin.
- `clinica/data/mascotas_demo.json`: pacientes y citas ficticias de demostración.
- `clinica/management/commands/cargar_datos_demo.py`: comando que lee el JSON y crea los registros en la base.
- `clinica/migrations/`: historial de cambios de esquema aplicado por Django.

## Requisitos

- Python instalado.
- El entorno virtual del proyecto en `.venv` con Django instalado.
- PowerShell en Windows, o una consola equivalente que permita ejecutar Python.

## Preparar y ejecutar en Windows

Abre PowerShell en la carpeta `Huellas_Sanas` y ejecuta:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py cargar_datos_demo
.\.venv\Scripts\python.exe manage.py runserver
```

El primer comando crea las tablas que necesita la aplicación. El segundo carga las mascotas ficticias. El tercero inicia el servidor local. Después abre:

- Agenda de recepción: <http://127.0.0.1:8000/>
- Django Admin: <http://127.0.0.1:8000/admin/>

Para entrar en Django Admin, crea una cuenta administrativa una vez:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

Django pedirá el nombre de usuario y la contraseña; el proyecto no incluye credenciales predeterminadas.

### Si aparece `no such table: clinica_cita`

La base SQLite todavía no tiene aplicadas las migraciones. Detén el servidor, ejecuta `migrate` con el comando de arriba y vuelve a iniciar `runserver`.

## Agregar mascotas de demostración con JSON

Edita `clinica/data/mascotas_demo.json`. Cada objeto describe una mascota y la cita que se creará para ella. Ejemplo:

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

Agrega el objeto dentro de la lista JSON, separándolo del anterior con una coma. Usa un horario que esté libre en la fecha elegida y uno de los estados válidos (`pendiente`, `atendida` o `cancelada`). Luego carga los datos con:

```powershell
.\.venv\Scripts\python.exe manage.py cargar_datos_demo
```

`dias_desde_hoy` es un desplazamiento respecto de la fecha en que se ejecuta el comando. Por ello, al cargar el mismo JSON otro día, la fecha calculada de las citas de demostración cambia. Para registrar pacientes reales, utiliza el formulario web o Django Admin. Para guardar una mascota sin cita todavía, usa **Mascotas → Añadir mascota** en Django Admin.

## Alcance

Este proyecto es una aplicación local de demostración para el ejercicio. Usa SQLite y no requiere conexión a servicios externos. El panel administrativo está protegido por el inicio de sesión de Django; el formulario público de recepción no requiere autenticación en esta versión.
