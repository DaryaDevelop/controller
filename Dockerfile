FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .
COPY .env_docker .env

CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]