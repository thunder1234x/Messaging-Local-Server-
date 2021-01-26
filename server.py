import socket
import threading

#global constant
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
BYTESIZE=64
MAXCONN=10
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'

#global variables
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn,addr):
    """
    this function handle multiple clients simultaneously
    args:
    conn:object of client connection
    addr:object of client port, ip address information
    return:None
    """
    print(f"[CONNECTED] {addr} is connected to server")
    connected=True
    
    while connected:
        new_msg_len=conn.recv(BYTESIZE).decode(FORMAT)
        if new_msg_len:
            new_msg_len=int(new_msg_len)
            msg=conn.recv(new_msg_len).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr}] :: {msg}")
    conn.close()



def start():
   """"
   Here all the client will connect to that server for sending messages through different threads
    args:None
    return:None
   """
   server.listen()
   print(f"    [LISTENING] Server is listening on {SERVER}")
   while True:
       conn,addr=server.accept()
       thread=threading.Thread(target=handle_client,args=(conn,addr))
       thread.start()
       print("[ACTIVE CONNECTION] is {}".format(threading.activeCount()-1))



print("[STARTING] Server is starting......")
start()