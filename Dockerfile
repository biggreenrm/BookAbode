FROM python:3.10.6

LABEL maintainer="Sergey Gurkov <biggreen.rm@gmail.com>"

ENV FLASK_APP=${FLASK_APP:-run} \
    POETRY_VERSION=1.1.13

RUN set -ex; pip install --no-cache-dir poetry==$POETRY_VERSION; \
    poetry config virtualenvs.create false

WORKDIR /app/

COPY . .

RUN poetry install

EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0"]
