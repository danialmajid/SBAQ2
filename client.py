import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.56.102', 8888))
num = float(input("Please insert temperature in Fahrenheit: "))
message = str(num)

s.send(message.encode())

print (s.recv(1024).decode())

s.close()
