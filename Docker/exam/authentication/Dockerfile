FROM ubuntu:18.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
ADD authentication.py /my_server/authentication.py
WORKDIR /my_server/
EXPOSE 5000
CMD python3 authentication.py
