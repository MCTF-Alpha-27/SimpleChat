"""
不会说话？这个插件可以帮到你！
"""
from .lib.root import *

__name__ = "悦耳之语"
__version__ = "1.0"
__author__ = "Jerry"

nicewords = tk.Menu(config_menu, tearoff = False)
config_menu.add_cascade(label = __name__, menu = nicewords)

# 表示感谢
thanks_talk = tk.Menu(nicewords, tearoff = False)
nicewords.add_cascade(label = "表示感谢", menu = thanks_talk)
thanks_talk.add_command(label = "真的很感谢你帮我！有空请你吃饭~", command = lambda: send_to_server("真的很感谢你帮我！有空请你吃饭~\n"))
thanks_talk.add_command(label = "谢谢你！如果这次没有你我就糟了", command = lambda: send_to_server("谢谢你！如果这次没有你我就糟了\n"))

# 表示抱歉
sorry_talk = tk.Menu(nicewords, tearoff = False)
nicewords.add_cascade(label = "表示抱歉", menu = sorry_talk)
sorry_talk.add_command(label = "真的非常抱歉，我会很快改正的！", command = lambda: send_to_server("真的非常抱歉，我会很快改正的！\n"))
sorry_talk.add_command(label = "对不起，我再也不会这样了！", command = lambda: send_to_server("对不起，我再也不会这样了！\n"))
sorry_talk.add_command(label = "真的很抱歉，由于我的失误造成了这么大的影响，请再给我一次机会！", command = lambda: send_to_server("真的很抱歉，由于我的失误造成了这么大的影响\n请再给我一次机会！\n"))

# 哲学句子
philosophy_talk = tk.Menu(nicewords, tearoff = False)
nicewords.add_cascade(label = "哲学句子", menu = philosophy_talk)
philosophy_talk.add_command(label = "人们平白消失，又无故再现，他们各奔东西，直到失去了对方", command = lambda: send_to_server("人们平白消失，又无故再现，他们各奔东西，直到失去了对方\n"))
philosophy_talk.add_command(label = "日升东方，却落于西；人海相识，却散于席", command = lambda: send_to_server("日升东方，却落于西；人海相识，却散于席\n"))