FROM python:3.7.4 as builder

COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.7-slim

COPY --from=builder /root/.local /root/.local

COPY ToDo app

RUN apt-get update && apt-get install -y default-libmysqlclient-dev

WORKDIR /app

ENV PATH /root/.local:$PATH

EXPOSE 8000

CMD ["python", "-m", "gunicorn", "--bind", ":8000", "--workers", "3", "ToDo.wsgi"]