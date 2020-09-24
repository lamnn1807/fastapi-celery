FROM python:3.7

ENV DOCKER=true

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000