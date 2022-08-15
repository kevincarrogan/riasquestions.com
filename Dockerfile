FROM tiangolo/uvicorn-gunicorn-starlette:python3.9-alpine3.14

COPY . /app

RUN pip install -r /app/requirements-prod.txt
