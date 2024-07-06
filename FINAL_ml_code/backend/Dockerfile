FROM python:3.8-slim

WORKDIR /app

COPY pyproject.toml /app/
RUN pip install poetry
RUN poetry install

COPY . /app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
