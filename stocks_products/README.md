# Склады и товары

## Техническая задача: Контейнизировать Django Rest Framework, используя Dockerfile.


Пример запроса:

```
# Просмотр продуктов
curl.exe --ssl-reqd localhost:8000/api/v1/products/

```

## Документация по проекту

Для запуска проекта необходимо

Собрать:

```bash
docker build . --tag=f1:v1
```

Запустить:

```base
docker run -d --name=lake -p 8000:8000 f1:v1 
```

Выполнить команду для отображения продуктов:

```bash
curl.exe --ssl-reqd localhost:8000/api/v1/products/

```