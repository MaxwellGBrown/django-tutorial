# django-example

## quickstart

```
docker build -t django-example
docker run -d -p 8000:80 -v $(pwd):/usr/src/app --name django-example --rm django-example
```
