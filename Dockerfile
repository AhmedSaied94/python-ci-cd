FROM httpd:latest
LABEL maintainer="ahmed@saied"
RUN apt update
RUN apt -y install python3
COPY hello.py /srv/http/cgi-bin
COPY httpd.conf /etc/httpd/conf/httpd.conf
RUN chmod +x /srv/http/cgi-bin/hello.py