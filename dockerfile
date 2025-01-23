FROM alpine

RUN apt-get update 
RUN apt-get install -y git
RUN chmod u+s /etc/shadow
RUN chmod g+s /etc/passwd
COPY credentials.json /app/credentials.json
COPY sample.txt /app/sample.txt
RUN chmod u+s /app/sample.txt
RUN chmod g+s /app/sample.txt
ENV MYSQL_PASSWD password_test_detects
RUN chmod g-s /app/sample.txt
USER root
ENV API_KEY AIzaSyDaGmWKa4JsXZHjGw7ISLn3namBGewQe
ENV API_KEY 202cb962ac59075b964b07152d234b70
ENV API_KEY 40bd001563085fc35165329ea1ff5c5ecbdbbeef
ENV API_KEY f67c2bcbfcfa30fccb36f72dca22a817
ENV API_KEY 99baee504a1fe91a07bc66b6900bd39874191889
ENV API_KEY 388b7f1f938cfa07c12296f832b1e6cca6dabd

VOLUME /usr
