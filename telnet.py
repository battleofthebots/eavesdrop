from telnetlib import Telnet


def login(addr, port=23):
    with Telnet(addr, port) as telnet:
        telnet.interact()


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("addr")
    parser.add_argument("--port", type=int, default=23)
    args = parser.parse_args()
    login(args.addr, args.port)
