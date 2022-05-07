"""
下拉菜单文件，负责向主菜单文件添加子菜单
"""
from .functions import *
from .root import *

class Manage:
    config_menu.add_command(label = "打开插件文件夹", command = open_plugin_dir) # 打开插件文件夹
    # config_menu.add_command(label = "载入的插件", command = show_plugin_info)
    config_menu.add_separator() # 增加分割线
    config_menu.add_command(label = "重启", command = restart) # 重启SimpleChat
    config_menu.add_command(label = "退出", command = eof) # 退出
    config_menu.add_separator() # 增加分割线
    
    config.config(menu = config_menu)