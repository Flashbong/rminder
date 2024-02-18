import argparse

class Rmdcli():
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description='Process some integers.',prog='[-h][--help]\t\t Open help')
        parser.add_argument('-h', '--help', type=int, help='Print manpage for the reminder')
        parser.add_argument('-a', '--add', help='Add new note')
        args = parser.parse_args()