"""
主体文件，负责许多重要工作，如安装前置、为其它文件提供参数等
"""
import os
import random

__version__ = "2.4.14"  # 版本
__author__ = "Jerry"  # 作者

with open("name.ini", "w") as f:
    f.write("User" + str(random.randint(1, 10000)))

with open("msg_type.ini", "w") as f:
    f.write("normal")

if __name__ == "__main__":
    try:  # 安装前置
        import easy_functions as ef
    except ModuleNotFoundError:
        print('Installing lib file "easy_functions"')
        while True:
            if os.system("pip install easy_functions") == 0:
                import easy_functions as ef

                break
            print("Installation failed. Trying again")

    ef.start("server.pyw")  # 启动服务器
    ef.start("client.pyw")  # 启动客户端
