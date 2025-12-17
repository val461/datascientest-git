FROM ubuntu:18.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
ADD authorization.py /my_server/code/authorization.py
WORKDIR /my_server/
CMD ["python3", "code/authorization.py"]
