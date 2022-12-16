FROM python:3.10-slim
ENV PYTHONBUFFERED 1
WORKDIR /app

RUN pip install "poetry==1.2.2"

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi --no-root
COPY . .
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
