from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(pipe, response):
    while True:
        msg = pipe.recv()
        print(f"{getpid()} receiving: {msg}")
        sleep(1)
        pipe.send(response)


if __name__ == '__main__':
    ping_conn, pong_conn = Pipe()

    Process(target=ponger, args=(ping_conn, 'ping')).start()
    Process(target=ponger, args=(pong_conn, 'pong')).start()

    ping_conn.send('ping')
