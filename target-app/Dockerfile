FROM python:3.13-slim
WORKDIR /usr/local/app

RUN useradd app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

USER app
EXPOSE 8080


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]