"""
菜单主文件，实现tkinter窗口的菜单功能并为插件提供前置参数、函数等
为插件提供了参数、函数、模块等，因此所有的插件都必须导入此文件
"""
import tkinter as tk
import socket
import os
import easy_functions as ef
from tkinter import messagebox as msg
from tkinter import ttk
from tkinter.constants import END
from address import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建socket

def display(text, end = "\n"): # 显示消息
    text_message.insert(END, text)
    text_message.insert(END, end)

def send_to_server(text): # 向服务器发送信息
    ef.wait(0.1)
    s.send(bytes(text, "utf-8"))
    ef.wait(0.1)

def send(): # 发送消息
    send_msg = text_text.get("0.0", END)
    s.send(bytes(send_msg, "utf-8"))
    text_text.delete("0.0", END)

def get_msg(): # 将服务器获取到的消息展示到消息面板中
    while True:
        try:
            msg = s.recv(1024).decode("utf-8")
            text_message.insert(END, msg)
        except:
            break

root = tk.Tk() # 根

accept_num = 10 # 最大连接数

message_frame = tk.Frame(root, width=480, height=300, bg="white") # 显示消息的窗口
text_message = tk.Text(message_frame) # 显示消息的Text

sent_frame = tk.Frame(root, width=480, height=30) # 发送消息的面板
text_frame = tk.Frame(root, width=480, height=100)
button_sent = ttk.Button(sent_frame, text = "发送", command = send) # 发送按钮
text_text = tk.Text(text_frame)

config = ttk.Menubutton(root, text = "管理") # 管理按钮
config_menu = tk.Menu(config, tearoff = False) # 下拉菜单

find_plugin_menu = tk.Menu(config_menu, tearoff = False) # 插件显示主菜单
find_plugin_menu_enabled = tk.Menu(find_plugin_menu, tearoff = False) # 启用的插件的主菜单
find_plugin_menu_disabled = tk.Menu(find_plugin_menu, tearoff = False) # 禁用的插件的主菜单

for i in os.listdir(".\\plugins"):
    if i[-3:] == ".py" or i[-9:] == ".disabled":
        config_menu.add_cascade(label = "插件管理", menu = find_plugin_menu) # 将插件显示主菜单绑定至管理菜单主菜单
        break
        
for i in os.listdir(".\\plugins"):
    if i[-3:] == ".py":
        find_plugin_menu.add_cascade(label = "启用的插件", menu = find_plugin_menu_enabled) # 将启用的插件的主菜单绑定至管理菜单主菜单
        break

for i in os.listdir(".\\plugins"):
    if i[-9:] == ".disabled":
        find_plugin_menu.add_cascade(label = "禁用的插件", menu = find_plugin_menu_disabled) # 将禁用的插件的主菜单绑定至管理菜单主菜单
        break
