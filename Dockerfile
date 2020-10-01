FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gcc \
    git \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    python-dev

RUN mkdir /app
WORKDIR /app

COPY requirements/ requirements/
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY scripts/ scripts/
RUN chmod +x scripts/command-dev.sh
COPY djangoplicity/ djangoplicity/
COPY test_project/ test_project/
COPY tests/ tests/
COPY setup.py .
COPY tox.ini .
COPY .coveragerc .
COPY manage.py .
