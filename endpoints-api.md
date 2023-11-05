# API Endpoints

*Nota: Falta añadir los métodos DELETE a las vistas de detalle de producto y categoría.*

## Products

### Product List

`/api/products`

Métodos: GET, POST.
  
### Product Detail

`/api/products/<product_slug>`

Métodos: GET, PATCH.
  
### Product Search

`/api/products/search/<search_term>`

Métodos: GET

## Categories

### Category List

`/api/categories`

Métodos: GET, POST.

### Category detail

`/api/categories/<int:category_id>`

Métodos: GET, PATCH.

### Category product list

`/api/categories/<int:category_id>/products`
Métodos: GET
  
------------------

## Django Admin

- `/admin/`

Mediante esta url se puede acceder al administrador de Django, no es un endpoint. Aquí se pueden añadir, borrar y editar objetos con base en los modelos creados para la API.

## Configuración de la API de Django

Para dejar funcionando la API de Django se debe hacer lo siguiente:

1. Crear un archivo con nombre `.env` dentro de la carpeta `api`. Dentro de ese archivo colocar el `SECRET_KEY` de la app de Django.
2. Instalar pip (Gestor de paquetes de Python)
3. Instalar virtualenv, pip-env, venv o paquetes similares para crear entornos virtuales de Python
4. Usando virtualenv:
   `pip install virtualenv`
5. Crear el entorno virtual:
   `virtualenv venv`
6. Activar el entorno virtual en Windows:
    `. .\venv\Scripts\activate`
    Activar el entorno virtual en Linux o Mac:
    `. venv/bin/activate`
    Para desactivar el entorno virtual:
    `deactivate`
7. Con el entorno virtual activado, instalar los paquetes requeridos por el proyecto de Django:
   `pip install -r requirements.txt`
8. Hacer las migraciones de la base de datos:
   `python manage.py makemigrations`
   `python manage.py migrate`
9. Crear un super usuario:
   `python manage.py createsuperuser`
10. Activar el servidor de Django cuando se vaya a usar la API:
    `python manage.py runserver 127.0.0.1:8000`
11. Ahora se puede acceder al administrador de Django con las credenciales del super usuario en `127.0.0.1:8000/admin/` y crear productos y categorías para probar la API.

*Los comandos se anteriores se deben ejecutar desde el directorio raíz del proyecto, donde se encuentra el archivo manage.py.*
