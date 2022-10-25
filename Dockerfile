FROM python:3.11.0-bullseye

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt
WORKDIR /app/src

EXPOSE 8000

CMD [ "gunicorn", "app:app" , "-b", "0.0.0.0:8000","--log-level", "debug" ]