# Aplicación registro de especies

## Python + Django + Bootstrap + MySql


## Funcionalidad
```
CRUD para proyectos<br>
CRUD para ecorregiones<br>
CRUD para especies <br>
Para el proyecto se usó django templates <br>

```

## Modelo de base de datos
```
Adjunto a este proyecto se encuentra el modelo relacional de bases de datos,
para esto se usarón modelos gracias al ORM de django

```

## Clonar proyecto
```
git clone <url project>
```
## Entrar a la carpeta
```
cd <project folder>
```

## Configuración e instalación del proyecto

### Configuración
```
pip install pipenv (se usa pipenv para registro de dependencias en el proyecto)<br>
pipenv install django (para instalar django y crear entorno virtual)<br>
pipenv shell (Activar el entorno virtual)<br>
pipenv install PyMySQL (instalación de conector a la base de datos de mysql, ajustes en archivo settings.py)<br>

```
### Ejecutar migraciones
```
python manage.py migrate (migración modelos predeterminados django)<br>
python manage.py makemigrations (crea migración de modelos del proyecto)<br>
python manage.py migrate (migración modelos del proyecto)<br>
```
### probar del proyecto
```
python manage.py runserver <br>
http://localhost:8000 (URL pagina principal del proyecto)<br>

```

