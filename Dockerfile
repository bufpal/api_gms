FROM python:3.6-alpine

RUN apk update && \
    apk add python3 python3-dev \
            gcc musl-dev linux-headers zlib zlib-dev \
            freetype freetype-dev jpeg jpeg-dev \
            postgresql-dev

WORKDIR /code
COPY . /code/

ENV LANG c.UTF-8
ENV DJANGO_SETTINGS_MODULE askdjango.settings.prod
ENV PYTHONUNBUFFERED 1

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["uwsgi", "--plugins", "http,python", \
              "--http", "0.0.0.0:80", \
              "--wsgi-file", "/code/api_gms/wsgi.py", \
              "--master", \
              "--die-on-term", \
              "--single-interpreter", \
              "--harakiri", "30", \
              "--reload-on-rss", "512", \
              "--post-buffering-bufsize", "8192"]