FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev \
    && pip3 install -r flask/requirements.txt \
    && pip3 install .
WORKDIR ./flask
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app"]