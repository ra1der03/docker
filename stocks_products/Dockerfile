FROM python:3.11
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
ENV MY_ENV=venv
EXPOSE 8000
COPY . .
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]