FROM python:3.11.2-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY hack.py /app/
COPY .env /app/

EXPOSE 8080

CMD ["python", "hack.py"]