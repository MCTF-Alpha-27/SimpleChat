"""
服务器文件，负责创建服务器的连接
"""
from threading import Thread
from plugins.lib.root import *

def brodcast(msg, ID="", msg_type="normal"):  # 广播
    ID = "[" + ID + "] "  # 增加中括号

    if msg_type == "normal":  # 判断消息类型
        for conn in client:
            conn.send(bytes(ID, "utf-8") + msg)  # 发送

    elif msg_type == "system":
        for conn in client:
            conn.send(msg)


def handle_client_in(conn, addr):  # 通知谁进入了聊天室
    with open("name.ini", "r") as f:
        ID = f.read()
    welcome = "欢迎 %s 加入聊天室\n" % ID
    client[conn] = ID
    brodcast(bytes(welcome, "utf-8"), msg_type="system")

    while True:
        try:
            with open("name.ini", "r") as f:
                ID = f.read()
            with open("msg_type.ini", "r") as f:
                msg_type = f.read()
            msg = conn.recv(1024)
            brodcast(msg, ID, msg_type=msg_type)
        except Exception as e:
            conn.close()
            del client[conn]
            brodcast(bytes("%s 离开聊天室\n" % ID, "utf-8"), msg_type="system")


client = {}  # 用户信息
addresses = {}  # 地址

s.bind((host, port))  # 绑定地址和端口号

if __name__ == "__main__":
    s.listen(accept_num)

    while True:
        conn, address = s.accept()
        addresses[conn] = address  # 记录地址
        Thread(target=handle_client_in, args=(conn, address)).start()  # 开启多线程
