FROM tiangolo/uvicorn-gunicorn-starlette:python3.11

COPY . /app

RUN pip install -r /app/requirements-prod.txt
