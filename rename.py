"""
此插件可以更改显示的ID
"""
from .lib.root import *

__name__ = "多姿多彩的ID"
__version__ = "1.4"
__author__ = "Jerry"

def rename():
    rename = tk.Tk()
    rename.title("更改ID")
    rename.minsize(300, 100)

    rename_text = ttk.Label(rename, text = "输入你的ID❤~")

    rename_input = ttk.Entry(rename)

    empty1 = ttk.Label(rename, text = "")
    empty2 = ttk.Label(rename, text = "")
    
    def _rename():
        nonlocal rename_input
        with open("name.ini", "r") as f:
            last_ID = f.read()
        with open("name.ini", "w") as f:
            f.write(rename_input.get())
            
        msg.showinfo("更改ID","成功更改ID为%s"%(' "' + rename_input.get() + '"'))
        send_to_server('"%s" 将自己的ID更改为 "%s"\n'%(last_ID, rename_input.get()))

    rename_button = ttk.Button(rename, text = "更改ID", command = _rename)
    quit_ = ttk.Button(rename, text = "完成", command = rename.destroy)

    rename_text.grid(row=0, column=0)

    rename_input.grid(row=0, column=1)

    empty1.grid(row=1, column=0)
    empty2.grid(row=2, column=0)

    rename_button.grid(row=3, column=0)
    quit_.grid(row=3, column=2)
    
    rename.mainloop()

config_menu.add_command(label = "更改ID", command = rename)