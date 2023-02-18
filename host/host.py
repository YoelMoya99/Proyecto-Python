import socket

HOST = "10.0.2.16"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        
        data = conn.recv(1024)
        while not data:                
            data = conn.recv(1024)
            
        print(data)
            
        s.sendall(bytes(input('Digite un mensage: '), 'utf-8'))
        
            # if not data:
            #     break
            # conn.sendall(data)