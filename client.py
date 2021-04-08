import socket

HOST = '127.0.0.1'
PORT = 61001
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print('Message from server: ', repr(data))
    u_input = input('Enter your nickname: ')
    nick = bytes(u_input, 'utf-8')
    s.sendall(nick)
    while True:
        u_input = input('Enter your message or \'q\' to exit: ')
        if u_input == 'q':
            quit()
        msg = bytes(u_input, 'utf-8')
        s.sendall(msg)