# Aplicacion de cursos
Aplicaci�n de cursos con carrito de compras en django
## Ejecutar

Para ejecutar el proyecto debe de tener instalado VirtualWrapper, Python3 y pip3, y sigas las instrucciones:
Nota: si esta trabajando con Virtualenv, puede ejecutar por ejemplo: virtualenv -p python3 env_django1.11.7

```
$ mkvirtualenv -p python3 env_django1.11.7
```

```
$ git clone https://herostartup@bitbucket.org/herostartup/reto-curso.git
```

```
$ cd carrito_compra/
```

```
$ pip install -r requirements.txt
```

```
$ ./manage.py makemigrations
```


```
$ ./manage.py migrate
```

```
$ ./manage.py createsuperuser
```

```
$ ./manage.py runserver
```

resultado
![a](https://www.dropbox.com/s/e231vy2n8c4zb7f/resultado_carrito.png)
[Enlace a image](https://www.dropbox.com/s/e231vy2n8c4zb7f/resultado_carrito.png)


# migrar a postgresql
https://devcode.la/tutoriales/como-conectar-django-con-postgres-en-ubuntu/

pipenv install  psycopg2 = "==2.7.4"
pipenv install  psycopg2-binary = "*"# RETO-DJANGO
# RETO-DJANGO
