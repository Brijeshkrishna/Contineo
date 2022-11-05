FROM python:3.9-bullseye

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

WORKDIR /app/src

CMD "uvicorn app:app --host $SERVER_NAME --port 10000"