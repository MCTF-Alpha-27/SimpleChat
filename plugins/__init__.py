"""
插件前置文件，负责导入文件夹下所有插件并检查插件安全性
"""
import os
import importlib
import json
from .lib.root import *
# TODO: 优化插件管理器UI
# def show_plugin_info(): # 启用的插件信息
    # msg.showinfo("插件信息","插件名: %s\n版本: %s\n作者: %s\n%s"%(enable_name, version, author, description))
    # display("插件列表    版本    作者    简介")
    # display("-------    ----    ----   ----")
    # display("%s          %s      %s     %s"%(name, version, author, description))

with open(".\\plugins\\plugin_info.json","w",encoding="ansi") as f: # 创建插件json
    f.write("")
for i in os.listdir(".\\plugins"): # 插件文件夹下所有文件
    if i[-3:] == ".py": # 判断该文件是否为启用的插件
        if i != "__init__.py": # 筛除__init__.py
            plugin = importlib.import_module("plugins.%s"%i.strip("py").strip(".")) # 导入插件

            if plugin.__doc__ is None: # 如果插件文档不存在，则设定默认值
                plugin.__doc__ = "No description"
            
            i = i.replace(".py","")
            plugin_list = { # 插件信息
                i : { # i为插件ID
                    "name"        : getattr(plugin, "__name__", i).replace("plugin.",""), # 插件名称
                    "version"     : getattr(plugin, "__version__", "1.0"),                # 插件版本
                    "author"      : getattr(plugin, "__author__", "Unknown"),             # 插件作者
                    "description" : plugin.__doc__                                        # 插件介绍
                }
            }
            with open(".\\plugins\\plugin_info.json","a") as f: # 写入插件json
                f.write(json.dumps(plugin_list, sort_keys = True, separators = (", ", ": ")))
                f.write("\n")

            _plugin = tk.Menu(find_plugin_menu_enabled, tearoff = False)

            for i in plugin_list: # 遍历插件信息字典
                name = i
                
                version = plugin_list[name]["version"] # 版本
                author = plugin_list[name]["author"] # 作者
                description = plugin_list[name]["description"] # 介绍

                def disable_plugin(): # 禁用插件
                    global name
                    os.rename(name, name + ".disabled")

                def enable_plugin(): # 启用插件
                    global name
                    os.rename(name + ".py.disabled", name)

                find_plugin_menu_enabled.add_cascade(label = i, menu = _plugin)
                _plugin.add_command(label = "插件信息", command = lambda: msg.showinfo("插件信息", "作者: %s\n版本: %s\n%s"%(author, version, description)))
                _plugin.add_command(label = "禁用", command = disable_plugin)

    elif i[-9:] == ".disabled": # 判断该文件是否为被禁用的插件
        _plugin = tk.Menu(find_plugin_menu_disabled, tearoff = False)
        disable_name = i.replace(".py.disabled", "")

        find_plugin_menu_disabled.add_cascade(label = disable_name, menu = _plugin)
        _plugin.add_command(label = "启用", command = enable_plugin)