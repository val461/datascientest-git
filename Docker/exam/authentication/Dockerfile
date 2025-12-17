FROM ubuntu:18.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
ADD authentication.py /my_server/code/authentication.py
WORKDIR /my_server/
CMD python3 code/authentication.py
