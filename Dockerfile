FROM python:3.9-bullseye

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

WORKDIR /app/src

CMD [ "gunicorn", "app:app" , "-b", "0.0.0.0:8000","--log-level", "debug", "--access-logfile", "-", "--logger-class", "gunicorn_color.Logger"] 
