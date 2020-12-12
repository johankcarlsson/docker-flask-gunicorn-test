FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
#RUN mkdir code
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
#COPY app/* /app/code/
#WORKDIR /app/code
EXPOSE 5000
ENTRYPOINT ["gunicorn", "--config", "/app/gunicorn_config.py", "app.wsgi:app", "--reload"]