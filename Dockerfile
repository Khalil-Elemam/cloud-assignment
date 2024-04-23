FROM python:3.12.2-slim
WORKDIR /app
COPY . .
CMD ["python", "main.py"]
