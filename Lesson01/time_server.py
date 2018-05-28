# Программа сервера времени

from socket import *
import json
import time
import argparse

# ADDR='localhost' //HOST
# PORT=8888
BUFFSIZ=1024

s= socket(AF_INET,SOCK_STREAM)

def create():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a','--address')
    parser.add_argument ('-p','--port',type=int)

    return parser

if __name__ == '__main__':
    parser = create()
    name= parser.parse_args()

addr,port='127.0.0.1',8888 
# none

if name.address:
    addr=name.address
else:
    addr=' '
if name.port:
    port=name.port
else:
    port=8888

s.bind((addr,port)) # Присваивает порт 8888
s.listen(5) # Переходит в режим ожидания запросов;
# одновременно обслуживает не более 5 запросов.

#бесконечный цикл
while True:
    client, addr_client = s.accept()
    print('Получен запрос на соеднение от' ,str(addr_client))
    message=client.recv(BUFFSIZ)
    if message:
        response_message={
            'response':'Соединение установлено',
            'time':time.ctime(time.time())
            }
    else:
        response_message={
            'response':'Соединение не установлено',
            'time':time.ctime(time.time())
            }
    response_message=json.dumps(response_message)
# Обратите внимание, дальнейшая работа ведётся с сокетом клиента
# client.send(timestr.encode('ascii'))   
# <- По сети должны передаваться байты,
# поэтому выполняется кодирование строки    
    client.send(response_message.encode('utf-8'))
client.close()

# client.close()
# удалить наработки
# while True:
#     conn, addr = sock.accept()
#     print('Connected:', addr)
#     data_b = conn.recv(BUFFSIZ)
#     obj_j=data_b.decode('utf-8')
#     print('Obj:', obj_j)
#     print(type(obj_j))
#     obj=json.loads((obj_j))
#     print('Close')
#     conn.close()
