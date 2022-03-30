#echoclient.py
import socket
port = 1235
address = '127.0.0.1'
BUF_SIZE = 1024

# create a socket object name 'con'
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))

message1 = "Hello!"
message2 = f"address is {address}"
con.send(bytes(message1,"utf-8"))
con.send(bytes(message2,"utf-8"))

data = con.recv(BUF_SIZE)
con.close()
print(data.decode("utf-8"))

