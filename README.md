# Mi Portafolio Django

Este es un proyecto de portafolio personal construido con el framework Django (Python).

## Descripción

Este proyecto tiene como objetivo crear un portafolio web similar a [https://kappak.dev/](https://kappak.dev/) utilizando Django. Actualmente, incluye la estructura básica con las siguientes secciones:

* **Inicio:** Una página de presentación.
* **Proyectos:** Una sección para mostrar mis trabajos y proyectos.
* **Sobre Mí:** Información personal y mis habilidades.
* **Contacto:** Una forma de que los visitantes se pongan en contacto conmigo.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

* **Python:** (Versión 3.x recomendada) - [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **Pip:** El gestor de paquetes de Python (generalmente se instala con Python).

## Instalación

Sigue estos pasos para configurar el proyecto localmente:

1.  **Clona el repositorio (si aún no lo has hecho):**
    ```bash
    git clone [https://github.com/javiergiraldo/miportafolio.git](https://github.com/javiergiraldo/miportafolio.git)
    cd mi_portafolio
    ```

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    # Activa el entorno virtual (dependiendo de tu sistema operativo)
    # En macOS/Linux:
    source venv/bin/activate
    # En Windows:
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias de Django:**
    ```bash
    pip install Django
    ```

4.  **Ejecuta las migraciones (inicialmente no habrá ninguna, pero es una buena práctica):**
    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuario (para acceder a la interfaz de administración de Django, si la necesitas en el futuro):**
    ```bash
    python manage.py createsuperuser
    # Sigue las instrucciones en la terminal para crear el usuario.
    ```

6.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

7.  **Abre tu navegador web y ve a `http://127.0.0.1:8000/`.** Deberías ver la página de inicio de mi portafolio.

## Estructura del Proyecto

La estructura básica del proyecto es la siguiente:

mi_portafolio/
├── mi_portafolio/      # Archivos de configuración del proyecto
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py      # Configuración principal del proyecto
│   ├── urls.py          # Definición de las URLs del proyecto
│   └── wsgi.py
├── pagina_principal/   # Aplicación principal del portafolio
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── pagina_principal/
│   │       ├── base.html    # Plantilla base
│   │       ├── contacto.html
│   │       ├── inicio.html
│   │       ├── proyectos.html
│   │       └── sobre_mi.html
│   ├── tests.py
│   ├── urls.py          # Definición de las URLs de la aplicación
│   └── views.py         # Lógica de las vistas
├── manage.py            # Script para administrar el proyecto Django
└── venv/                # (Opcional) Entorno virtual

## Próximos Pasos

Los siguientes pasos para continuar desarrollando este portafolio podrían incluir:

* Integrar Tailwind CSS para aplicar estilos.
* Crear modelos para gestionar la información de los proyectos y otras secciones de forma dinámica.
* Implementar un formulario de contacto.
* Agregar más contenido y personalizar las plantillas.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1.  Haz un fork del repositorio.
2.  Crea una rama para tu contribución (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y haz commit de ellos (`git commit -m 'feat: Añade nueva funcionalidad'`).
4.  Sube tus cambios al fork (`git push origin feature/nueva-funcionalidad`).
5.  Crea un Pull Request.

## Licencia

MIT License

