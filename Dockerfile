FROM python:3.10
MAINTAINER trond
WORKDIR /app
RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY . .
RUN mv /app/config-prod.yml /app/config.yml
ENV PYTHONUNBUFFERED=1
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["web.py"]
