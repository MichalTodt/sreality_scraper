FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev \
    && pip3 install -r requirements.txt
CMD scrapy crawl sreality
