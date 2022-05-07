"""
进行一些网页操作
"""
from .lib.root import *

__name__ = "通用网页扩展"
__version__ = "1.0"
__author__ = "Jerry"

def open_url():
    url = tk.Tk()
    
    url.minsize(300, 100)
    url.title("打开网页")

    url_text = ttk.Label(url, text = "网页链接")
    url_input = ttk.Entry(url)
    empty1 = ttk.Label(url, text = "")
    empty2 = ttk.Label(url, text = "")
    url_button = ttk.Button(url, text = "打开", command = lambda: showurl(url_input.get()))
    quit_ = ttk.Button(url, text = "完成", command = url.destroy)

    url_text.grid(row=0, column=0)
    url_input.grid(row=0, column=1)
    empty1.grid(row=1, column=0)
    empty2.grid(row=2, column=0)
    url_button.grid(row=3, column=0)
    quit_.grid(row=3, column=2)

    url.mainloop()

url_menu = tk.Menu(config_menu, tearoff = False)
config_menu.add_cascade(label = "通用网页扩展", menu = url_menu)

url_menu.add_command(label = "打开网页", command = open_url)