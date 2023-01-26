import socket

# function to convert fahrenheit input to celsius
def fahrenheit_to_celsius(tempF):
    tempC = (tempF - 32) * (5.0/9.0)
    return tempC

def main():

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.bind(("192.168.56.102", 8888))

    serversocket.listen(1)

    print("Waiting for client,please wait")

    while 1:

        clientsocket, addr = serversocket.accept()
        print("Received connection from %s" % str(addr))

        tempF = clientsocket.recv(1024).decode()
        tempC = fahrenheit_to_celsius(float(tempF))
        tempC = round(tempC,2)
        tempC = str(tempC)
        clientsocket.send(tempC.encode())

main()
