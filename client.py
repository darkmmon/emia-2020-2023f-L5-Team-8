# importing the necessary modules.
import tkinter as tk
from tkinter import messagebox
import socket
import sys
import errno
def send_message(client_socket, message, by):
    # defining the header length.
    HEADER_LENGTH = 10
    """
    encode the message into bytes, counted the number of bytes, and then prepared a header of fixed size, that we have encoded to bytes as well.
    """
    message = message.encode('utf-8')
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
    # sending the message.
    client_socket.send(message_header + message)

def get_message(client_socket):
    # defining the header length.
    HEADER_LENGTH = 10

    try:
        # looping over the received messages and printing them.
        while True:
            # getting the header.
            username_header = client_socket.recv(HEADER_LENGTH)

            # If no header is accepted then finish the connection.
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Converting the header to an int value.
            username_length = int(username_header.decode('utf-8').strip())

            # Decoding the received username.
            username = client_socket.recv(username_length).decode('utf-8')

            # Decoding the received message.
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # Printing the message.
            print(f'{username} > {message}')
            return "abc"

    except IOError as e:
    #     # handling the normal error on nonblocking connections.
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
    #         sys.exit()

    # except Exception as e:
    #     print('Reading error: '.format(str(e)))
    #     sys.exit()

def chatroom_main():
 # defining the header length.
    HEADER_LENGTH = 10

        # Getting the name of the client.
        # need to get from data
    my_username = "hello world speaking"

    # defining the IP address and Port Number.
    IP = "127.0.0.1"
    PORT = 1234

    """
    Creating a client socket and providing the address family (socket.AF_INET) and type of connection (socket.SOCK_STREAM), i.e. using TCP connection.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting the socket with the IP address and Port Number.
    client_socket.connect((IP, PORT))

    """
    Setting the connection to a non-blocking state so that the recv() function call will not get blocked. It will return some exceptions only.
    """
    client_socket.setblocking(False)

    # Setting the username and header.
    username = my_username.encode('utf-8')
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
    
    # start of actual function

    signup_window = tk.Tk()
    signup_window.geometry("800x500")
    signup_window.title("Chatroom")

    title = tk.Label(signup_window, text="Create your personal account", font= ('Arial' ,18))
    title.pack(padx= 20, pady=20)

    frame = tk.Frame(signup_window)
    frame.columnconfigure(0,weight=2)
    frame.columnconfigure(1,weight=2)
    frame.columnconfigure(2,weight=2)
    frame.columnconfigure(3,weight=2)

    incoming_message = get_message(client_socket)
    incoming_message = "testing"
    tk.Label(frame, text=incoming_message).grid(column=0, row=0)

    message = tk.Label(frame, text="message:", font= ('Arial' ,18))
    message.grid(row=5, column=0, sticky=tk.E +tk.W)
    new_message = tk.Entry(frame)
    new_message.grid(row=5, column=1)


    frame.pack()

    button_2 = tk.Button(signup_window, text= "Enter", font= ("Arial", 15), command=lambda :send_message(client_socket, new_message.get(), my_username))
    button_2.pack()
    signup_window.mainloop()