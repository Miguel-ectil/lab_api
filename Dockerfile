# Usar uma imagem base oficial do Python
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 1313

CMD ["python", "app.py"]