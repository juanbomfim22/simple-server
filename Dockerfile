FROM python:3-slim
RUN apt-get update && apt-get install -y bash curl nano wget python3-dev gcc libc-dev libffi-dev

RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /var/www/server

ADD . /var/www/server

ENV PATH="${PATH}:/root/.local/bin"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev --no-interaction --no-ansi

COPY . .

CMD ["flask", "run", "-h", "0.0.0.0"]

EXPOSE 5000
