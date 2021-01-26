import socket
import tkinter as tk
from tkinter import ttk

#global constant
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
BYTESIZE=64
MAXCONN=10
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'

#global connection variable
Client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect(ADDR)


#mainwindow 
main_window=tk.Tk()
main_window.geometry('500x500')
main_window.title('Message Box')

#message box
message_box=tk.LabelFrame(main_window,text='Type Message',width=300,bd=0)
message_box.pack(side=tk.BOTTOM)
message_box.config(pady=20)

#button functionality
def msg_send():
    message=text_editor.get(1.0,'end-1c')
    # print(f"message {message}")
    if message !=None:
        msg=message.encode(FORMAT)
        msg_length=len(msg)
        send_length=str(msg_length).encode(FORMAT)
        send_length+=b' '*(BYTESIZE-len(send_length))
        Client.send(send_length)
        Client.send(msg)
        text_editor.delete(1.0,'end')
    else:
        return

#button for sending message
send_button=tk.Button(message_box,text='SEND',command=msg_send)
send_button.pack(side=tk.RIGHT)

#text_editor inside message box frame
text_editor =tk.Text(message_box,width=50,height=10)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(message_box)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#shortcut key binding


main_window.mainloop()

#for disconnecting user
def final_msg_send(message):
    msg=message.encode(FORMAT)
    msg_length=len(msg)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' '*(BYTESIZE-len(send_length))
    Client.send(send_length)
    Client.send(msg)
final_msg_send(DISCONNECT_MESSAGE)
