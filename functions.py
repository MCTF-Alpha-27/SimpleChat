"""
这里是函数文件，存放所有需要用到的函数
"""
import easy_functions as ef
import os
import sys
import json
from .root import *
from main import t

def restart(): # 重启
    if msg.askokcancel("重启","你确定要重启吗？") == False:
        return
    try:
        sys.exit(1)
    except SystemExit:
        ef.start("run.bat")
        os.system("taskkill /f /im pythonw.exe /t")

def eof(): # 退出
    if msg.askokcancel("退出","你确定要退出吗？") == False:
        return
    try:
        sys.exit(1)
    except SystemExit:
        os.system("taskkill /f /im pythonw.exe /t")

def open_plugin_dir(): #打开插件文件夹
    ef.start("%s\\plugins"%os.getcwd())

def show_plugin_info(): # 显示插件信息
    plugin_list = []
    with open(".\\plugins\\plugin_info.json","r") as f: # 读取插件信息json
        for i in f.readlines():
            plugin_list.append(json.loads(i))

    for i in plugin_list: # 遍历插件信息字典
        for l in i:
            name = i[l]["name"]
            version = i[l]["version"] # 版本
            author = i[l]["author"] # 作者
            description = i[l]["description"] # 介绍

            display("\n插件ID: %s\n插件名称: %s\n版本: %s\n作者: %s\n%s"%(l, name, version, author, description))