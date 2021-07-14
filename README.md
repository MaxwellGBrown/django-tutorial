# django-example

This repo is built from the [Django: Getting Started Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)

## quickstart

```
docker build -t django-example
docker run -it -v $(pwd):/usr/src/app --name django-migration --rm django-example migrate
docker run -d -p 8000:80 -v $(pwd):/usr/src/app --name django-example --rm django-example
```

### create a migration

```
docker run -it -v $(pwd):/usr/src/app --name django-migration --rm django-example migrate
docker run -it -v $(pwd):/usr/src/app --name django-migration --rm django-example makemigrations polls
```
