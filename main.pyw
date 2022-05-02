"""
主体文件，负责许多重要工作，如安装前置、为其它文件提供参数等
"""
import random
import os
from threading import Thread

__version__ = "2.0.0"  # 版本
__author__ = "Jerry"  # 作者

try:
    import easy_functions as ef
except ModuleNotFoundError:
    while True:
        if os.system("pip install easy_functions") == 0:
            import easy_functions as ef
            break

with open("name.ini", "w") as f:
    f.write("User" + str(random.randint(1, 10000)))

with open("msg_type.ini", "w") as f:
    f.write("normal")

server = Thread(target=ef.start, args=("server.pyw",)) # 服务端线程
client = Thread(target=ef.start, args=("client.pyw",)) # 客户端线程
t = [server, client]

if __name__ == "__main__":
    for i in t:
        i.start()
