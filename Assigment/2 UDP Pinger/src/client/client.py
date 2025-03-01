import time
from socket import *
server_name = "localhost"
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)
address_tuple = (server_name, server_port)
for i in range(1, 11):
    send_time = time.time()
    send_message = f"Ping {i} {send_time}"
    try:
        print()
        client_socket.sendto(send_message.encode(), address_tuple)
        client_socket.settimeout(1)
        print(send_message)
        receive_message, received_address = client_socket.recvfrom(2048)
        receive_time = time.time()
        print(int(receive_time - send_time))
    except TimeoutError:
        print("Request timed out")
client_socket.close()