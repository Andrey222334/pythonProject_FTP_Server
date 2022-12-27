import socket
from Command_lib import *


ChoseDirectory(os.path.join(os.getcwd(), 'docs'))

def process(req):
    req = req.split()
    if req[0] == 'pwd':
        return os.getcwd()[os.getcwd().find('docs'):]
    elif req[0] == 'ls':
        if len(os.listdir(os.getcwd())) != 0:
            return '; '.join(os.listdir(os.getcwd()))
        else:
            return 'Directory is empty'
    elif req[0] == 'mkdir':
        if not os.path.exists(os.path.join(os.getcwd(), req[1])):
            os.makedirs(os.path.join(os.getcwd(), req[1]))
            return os.path.join(os.getcwd(), req[1])[os.getcwd().find('docs'):]
        else:
            return "aleady exists"
    elif req[0] == 'cd':

        if os.path.exists(os.path.join(os.getcwd(), req[1])):
            ChoseDirectory(os.path.join(os.getcwd(), req[1]))
        elif req[1] == 'up':
            ChoseDirectory(req[1])

        if os.getcwd().find('docs') != -1:
            return os.getcwd()[os.getcwd().find('docs'):]
        else:
            ChoseDirectory(os.path.join(os.getcwd(), 'docs'))
            return 'dont exists'

    elif req[0] == 'rm':
        if os.path.exists(os.path.join(os.getcwd(), req[1])):
            RemoveDir(os.path.join(os.getcwd(), req[1]))
            return os.getcwd()[os.getcwd().find('docs'):]
        else:
            return 'dont exists'

    elif req[0] == 'touch':
        if not(os.path.exists(os.path.join(os.getcwd(), req[1]))):
            CreateFile(os.path.join(os.getcwd(), req[1]))
            return os.getcwd()[os.getcwd().find('docs'):]
        else:
            return 'already exists'

    elif req[0] == 'cat':
        if os.path.exists(os.path.join(os.getcwd(), req[1])):
            return ReadFile(os.path.join(os.getcwd(), req[1]))
        else:
            return 'dont exists'
    elif req[0] == 'exit':
        print(f'{addr} disconnect')
        return 'exit'
    else:
        return 'bad request'



PORT = 6666

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', PORT))
sock.listen()
print("Прослушиваем порт", PORT)
while True:
    conn, addr = sock.accept()
    log_list = [str(conn), str(addr), '', '']

    request = conn.recv(1024).decode()
    log_list[2] = request
    print(request)

    response = process(request)
    log_list[3] = response
    conn.send(response.encode())

    with open(r'C:\Users\Пользователь1\PycharmProjects\FTP_server\log.txt', 'a') as file:  # Запись логов
        file.write(f'Connection Info: {log_list[0]}\n')
        file.write(f'Actual Connection: {log_list[1]}\n')
        file.write(f'Command From Client: {log_list[2]}\n')
        file.write(f'Server Response: {log_list[3]}\n')
        file.write('\n')

conn.close()