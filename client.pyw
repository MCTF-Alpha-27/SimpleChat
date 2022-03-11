"""
这里是客户端文件，负责创建聊天室窗口
"""
from threading import Thread
from address import *
from plugins.lib.root import *

os.system("taskkill /im cmd.exe")  # 关闭cmd

s.connect((host, port))  # 与服务器建立连接

root.title("SimpleChat")  # 标题

message_frame.grid(row=0, column=0, padx=3, pady=6)  # 消息窗口，第1行，第0列
text_frame.grid(row=1, column=0, padx=3, pady=6)  # 输入窗口，第2行，第0列
sent_frame.grid(row=2, column=0)  # 发送按钮，第3行，第0列
config.grid(row=0, column=1)  # 管理按钮，第4行，第1列

message_frame.grid_propagate(0)  # 固定消息窗口大小
text_frame.grid_propagate(0)  # 固定输入窗口大小
sent_frame.grid_propagate(0)  # 固定发送按钮大小
config.grid_propagate(0)  # 固定管理窗口大小

text_message.grid()  # 将消息窗口添加到容器中
text_text.grid()  # 将输入窗口添加到容器中
button_sent.grid()  # 将发送按钮添加到容器中
config.grid()  # 将管理按钮添加到容器中

receive_thread = Thread(target=get_msg)  # 建立多线程
receive_thread.start()  # 启动线程

root.mainloop()  # 启动Tk循环
