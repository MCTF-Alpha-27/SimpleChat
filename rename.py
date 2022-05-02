"""
此插件可以更改显示的ID
"""
from .lib.root import *

__name__ = "多姿多彩的ID"
__version__ = "1.2"
__author__ = "Jerry"

def rename():
    rename = tk.Tk()
    rename.title("更改ID")
    rename.minsize(300, 100)

    rename_input = ttk.Entry(rename)

    empty = ttk.Label(rename, text = "")
    
    def ID_change():
        nonlocal rename_input
        with open("name.ini", "w") as f:
            f.write(rename_input.get())
            
        msg.showinfo("更改ID","成功更改ID为%s"%(' "' + rename_input.get() + '"'))

    rename_ID = ttk.Button(rename, text = "更改ID", command = ID_change)
    quit_ = ttk.Button(rename, text = "完成", command = rename.destroy)

    #rename_text.pack()
    rename_input.pack()
    empty.pack()
    rename_ID.pack(side=tk.LEFT)
    quit_.pack(side=tk.RIGHT)
    
    rename.mainloop()

config_menu.add_command(label = "更改ID", command = rename)