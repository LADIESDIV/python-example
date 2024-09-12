FROM python:3.12 AS requirement
ENV PYTHONUNBUFFERED=1
USER root
RUN mkdir -p /code
COPY app.py /code
COPY requirements.txt /code
WORKDIR /code

RUN apt-get update && apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED=1
USER root
RUN mkdir /code

COPY --from=requirement /code /code
COPY --from=requirement /opt/venv /opt/venv

RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip setuptools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

WORKDIR /code

USER 1001

EXPOSE 8080

ENV FLASK_APP app.py
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV ENV="prod"

CMD ["python", "app.py", "-h", "0.0.0.0"]
