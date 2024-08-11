FROM python:3.11-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /srcc

COPY ./requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
ENV MY_ENV=base_env
EXPOSE 5050

COPY . .
CMD ["python3", "-u", "main.py", "--host", "0.0.0.0", "--port", "[host]"]