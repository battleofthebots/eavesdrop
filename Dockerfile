FROM ghcr.io/battleofthebots/botb-base-image:ubuntu

RUN apt-get update && apt-get install -y telnetd
RUN echo "user:telnet" | chpasswd

ENTRYPOINT inetd -i
