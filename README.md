# Eavesdrop

This container runs a telnet server and changes the base image user to have the password `telnet`.
Competitors are given a pcap file from which they need to extract the telnet login session containing the username `user` and the password `telnet`.


## Building
```sh
docker build . -t eavesdrop
```

## Running
```sh
docker run --cpus=1 -p 21:21 -p 6200:6200 eavesdrop
```

## Exploiting
```sh
telnet -l user <container addr>
# enter password telnet
```

If you insist on having a script, a python script is included
```sh
python3 telnet.py <container addr>
```

*note: inetd doesn't like it when you use localhost with docker containers, but it's fine if you are in the docker network or use the container's IP*
