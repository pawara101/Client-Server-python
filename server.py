import socket
port = 1234
address = "127.0.0.1"

#Create a socket name server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # for IPv4, TCP
server.bind((address,port))
server.listen(5)
print('Listening...')

while True:
    con,addr = server.accept()
    print('Connection address is:', addr)
    con.send(b'Welcome to the server!')
    con.send(bytes("hello Welcome",'utf-8'))