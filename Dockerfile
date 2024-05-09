FROM python:3.12.3-alpine3.19
LABEL mantainer="contato@henriquesebastiao.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY bot /bot
COPY requirements.txt .

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r requirements.txt

CMD ["/venv/bin/python", "./bot/main.py"]