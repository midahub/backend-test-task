FROM python:3.12

WORKDIR /app/src

# TODO: setup application

CMD ["uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "8000"]
