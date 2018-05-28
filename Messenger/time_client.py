# Программа клиента, запрашивающего текущее время
'''
функции клиента:
 - сформировать presense-сообщение;
 - отправить сообщенгие среверу;
 - получить ответ сервера;
 - разобрать сообщение сервера;
 - параметры командной строки скрипта client.py <addr> [<port>]:
 - addr - ip-адрес сервера;
 - port - tcp-порт на сервере, по умолчанию 7777.
'''
from socket import *
import json
import time
import argparse

# ADDR='localhost' //HOST
# PORT=8888
BUFFSIZ=1024

s = socket (AF_INET,SOCK_STREAM)

def create():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a','--address')
    parser.add_argument ('-p','--port',type=int)

    return parser

if __name__ == '__main__':
    parser = create()
    name= parser.parse_args()

addr,port=None,None

if name.address:
    addr=name.address
else:
    addr='localhost'
if name.port:
    port=name.port
else:
    port=8888
s.connect((addr,port))

presense_message={
    'action':'presense',
    'time':time.ctime(time.time()),
    "user": {
        "user_name": "user_name",
        "status": "online"
        }
    }
presense_message=json.dumps(presense_message)
presense_message=presense_message.encode('utf-8')
s.send(presense_message)
response=s.recv(BUFFSIZ)
response=response.decode('utf-8')
response=json.loads(response)
s.close()
print(response['response'],response['time'])

def create_presence(account_name="Guest"):
    '''
    :param account_name: Имя пользователя
    :return:  Словарь сообщения
    tests:
    Из-за времени трудно написать doctest
    '''
    #Если имя не строка
    if not isinstance(account_name,str):
    # Генерируем ошибку передан неверный тип
        raise TypeError
    # Если ддлина имени пользователя больше 25 символов
    if len(account_name)>25:
        # Генерируем ошибку длины имени пользователя, слишком длинное
        raise UsernameToLongError(account_name)
    #формируем словарь сообщения
    message = {
        Action: presence,
        Time: time.time(),
        User: {
            Account_name: account_name
        }
    }
    #возвращаем
    return message

# удалить наработки 
# s = socket(
#     AF_INET, SOCK_STREAM)  # Создать сокет TCP
# s.connect((HOST, PORT))   # Соединиться с сервером
# tm = s.recv(1024)                
# Принять не более 1024 байтов данных
# s.close()
#print("Текущее время: %s" % tm.decode('ascii'))
# print("Текущее время: %s" % tm)