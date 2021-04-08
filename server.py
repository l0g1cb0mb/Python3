from datetime import datetime
import threading
import socket


HOST = 'localhost'
PORT = 61001


def new_conn():
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        conn.sendall(b'Enter your nickname, please!')
        nick = conn.recv(1024)
        with open('logs', 'a') as f:
            now = datetime.now()
            tmp = '[' + str(nick) + ']:(' + now.strftime("%d/%m/%Y %H:%M:%S") + ') - ' + 'Connected by (IP address, port) - ' + str(addr) + ';\n'
            f.write(tmp)
        while True:
            data = conn.recv(1024)
            if data == b'':
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                tmp = '[CLIENT]:(' + now + ')[' + str(nick) + '] - disconnected;\n'
                with open('logs', 'a') as f:
                    f.write(tmp)
                print(tmp)    
                break
            print(nick, 'message:', data)
            if not data: break
            conn.sendall(data)
            with open('logs', 'a') as f:
                now = datetime.now()
                tmp = '[' + str(nick) + ']:(' + now.strftime("%d/%m/%Y %H:%M:%S") + ') - ' + str(data) + ';\n'
                f.write(tmp)
            

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    t1 = threading.Thread(group=None, target=new_conn, name=None, args=(), kwargs={}, daemon=None)
    t1.start()
    t2 = threading.Thread(group=None, target=new_conn, name=None, args=(), kwargs={}, daemon=None)
    t2.start()
    
    try:
        t1.run()
    except:
        t1.join()
        
    try:
        t2.run()
    except:
        t2.join()
