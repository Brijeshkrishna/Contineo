FROM python:3.9

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 10000

ENTRYPOINT [ "uvicorn" ]

CMD ["app:app","--host", "0.0.0.0", "--port", "10000"]