"""
此插件可以更改聊天窗口的标题
"""
from .lib.root import *

__name__ = "标题更改"
__version__ = "1.1"
__author__ = "Jerry"

def title():
    title = tk.Tk()
    title.title("更改聊天窗口标题")
    title.minsize(300, 100)

    title_text = ttk.Label(title, text = "标题")

    title_input = ttk.Entry(title)

    empty1 = ttk.Label(title, text = "")
    empty2 = ttk.Label(title, text = "")

    def _title():
        nonlocal title_input
        root.title(title_input.get())

    title_button = ttk.Button(title, text = "更改", command = _title)
    quit_ = ttk.Button(title, text = "完成", command = title.destroy)

    title_text.grid(row=0, column=0)
    
    title_input.grid(row=0, column=1)

    empty1.grid(row=1, column=0)
    empty2.grid(row=2, column=0)

    title_button.grid(row=3, column=0)
    quit_.grid(row=3, column=2)

config_menu.add_command(label = "更改聊天窗口标题", command = title)