"""
主体文件，负责许多重要工作，如安装前置、为其它文件提供参数等
"""
import random
import os
from threading import Thread

__version__ = "2.0.0-Alpha"  # 版本
__author__ = "Jerry"  # 作者

with open("name.ini", "w") as f:
    f.write("User" + str(random.randint(1, 10000)))

with open("msg_type.ini", "w") as f:
    f.write("normal")

def run(file):
    os.system("python %s"%file)

server = Thread(target=run, args=("server.pyw",)) # 服务端线程
client = Thread(target=run, args=("client.pyw",)) # 客户端线程
t = [server, client]

if __name__ == "__main__":
    for i in t:
        i.start()
