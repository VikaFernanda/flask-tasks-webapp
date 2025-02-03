FROM python:3.12-slim AS build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV FLASK_DEBUG False

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN apt-get update && apt-get install -y nginx

RUN rm /etc/nginx/sites-enabled/default

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 5000

RUN flask db upgrade

# CMD sh -c "flask db upgrade && nginx -g 'daemon off;' & flask run --host=0.0.0.0"

CMD service nginx start && flask run --host=0.0.0.0