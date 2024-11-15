FROM python:3.11.2-slim

WORKDIR /app

# Copy only the necessary files into the container
COPY requirements.txt .
COPY hack.py .
COPY .env .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Command to run the application
CMD ["python", "hack.py"]