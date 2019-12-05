import socket
PORT = 7105

sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

sd.bind(('', PORT))

sd.listen(5)

print("socket is listening")

while True:
    try:
        # Establish connection with client.
        conn, addr = sd.accept()
        print('Got connection from', addr)

        # send a thank you message to the client.
        conn.send('Thank you for connecting'.encode())
    except Exception as e:
        print("Value of e: {} and its type is: {}".format(e, str(type(e))))
    finally:
        # Close the connection with the client
        conn.close()
