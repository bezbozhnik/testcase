FROM python:3.11

WORKDIR /app

COPY ../../requirements.txt .
RUN pip install -r requirements.txt

COPY ../../main.py .
COPY ../../db.py .
COPY ../../models.py .
COPY ../../create_db.py .