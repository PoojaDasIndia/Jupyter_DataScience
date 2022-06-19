import socket

hostname = socket.gethostname()  # get-hostname give host name
IPAddress = socket.gethostbyname(hostname)  # gethostbyname give host according to hostname
print(IPAddress)
