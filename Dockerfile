FROM python:3.13-alpine

WORKDIR /test_task

COPY Pipfile Pipfile.lock ./
RUN pip install --no-cache-dir pipenv && pipenv install --system

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
