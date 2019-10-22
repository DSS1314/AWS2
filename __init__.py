import boto3
import tkinter
from tkinter import messagebox
import connect_mysql
def ui1():
    root = tkinter.Tk()
    # 给主窗口设置标题内容
    root.title("信息查询系统")
    root.geometry('400x400')
    inputUrl = tkinter.Variable()
    # 创建一个消息接收文本框,并设置尺寸
    input_receive = tkinter.Entry(root, width=40,textvariable=inputUrl)  # 输入框
    inputUrl.set("   ")  # 设置默认值
    def ui():  # 发送按钮响应事件
        m = inputUrl.get()
        n=connect_mysql.connect(m)               #编写send1函数将消息发送到后台做相应处理
        print(n)
    def u2():
        connect_mysql.hua1()
    def u3():
        m = inputUrl.get()
        j = connect_mysql.put(m)  # 消息接收函数，将返回的结果打印出来，需要编写receive函数
        get.insert("1.0", j)
        print(j)
        print("           ")
    get = tkinter.Text(root, height=20, width=50)  # 查询相关消息的返回结果，对应显示到该文本框中
    sigin1Up_button = tkinter.Button(root, text="查询", width=10, command=ui)  # 连接到数据库并查询到其中的数据
    sigin2button = tkinter.Button(root, text="折线图", width=10,command= u2)  # command=ui1()#需要连接调用画图函数，返回折线图结果
    sigin1Up_button.place(x=250, y=60)  # 输入键的位置
    input_receive.place(x=50, y=30)  # 输入窗口的显示位置
    sigin2button.place(x=60, y=60)  # 换手率折线图键的位置
    get.place(x=20,y=100)        #接收到的消息的显示位置
    root.mainloop()
ui1()