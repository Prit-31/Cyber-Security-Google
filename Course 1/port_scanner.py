import socket

host = "127.0.0.1"
for port in range(20, 1025):
    sock = socket.socket()
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()
  
