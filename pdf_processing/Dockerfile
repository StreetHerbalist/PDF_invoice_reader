FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir PyMuPDF

CMD ["python", "main.py"]
