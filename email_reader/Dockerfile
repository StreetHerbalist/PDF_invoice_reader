FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir imapclient

CMD ["python", "main.py"]