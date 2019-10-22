import matplotlib.pyplot as plt
import pymysql
# 连接database
def connect(messsage):
    conn = pymysql.connect(host="mysql1.cxn970h1xyso.us-east-1.rds.amazonaws.com", user="A123456", password="12345678", database="mysql1", charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句
    try:
       data="select day from text"
       cursor.execute(data)
       data = cursor.fetchall()
       number="select number from text"
       cursor.execute(number)
       number = cursor.fetchall()
       achievemoney = "select achievemoney from text"
       cursor.execute(achievemoney)
       achievemoney = cursor.fetchall()
       changes = "select changes from text"
       cursor.execute(changes)
       changes= cursor.fetchall()
       i=0
       j=0
       floatData = []
       for rowData in data:
           temp = rowData[0].strftime('%Y-%m-%d')
           temp = temp[0:4] + temp[5:7] + temp[8:10]
           floatData.append(float(temp))
           if floatData[i]==float(messsage):
             j=i
             break
           else:
             i=1
      # print('-->',data)
      #k=data[j]+number[j]+achievemoney[j]+changes[j]
        #print (number[i])
      # print (achievemoney[i])
      # mesge=cursor.fetchone()#一次取一条
    except:
       print('SQL执行失败，执行语句为:%s' % str(data))
    print(number[j])
    print(achievemoney[i])
    print(changes[j])
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()
def  put(messsage):
    n=connect(messsage)
    print(n)
def  hua():
    # 建立数据库连接
    conn = pymysql.connect("mysql1.cxn970h1xyso.us-east-1.rds.amazonaws.com", user="A123456", password="12345678", database="mysql1",charset="utf8")
    print("连接成功")
    # 读取数据库表数据
    cursor=conn.cursor()
    try:
        sql = "select * from text where day>'2018/10/20' and day<'2018/10/30'"
        # 执行sql语句
        cursor.execute(sql)  # 取20条数据
        data = cursor.fetchall()
        # 数据转化为列表
        x = list(data.day)  # 日期
        y = list(data.number)  # 数量
        z = list(data.achievemoney)  # 成交额
        # 设置折线样式
        plt.plot(x, y, "g--")
        plt.plot(x, z, "r--")

        # 设置x坐标轴的范围
        plt.xlim(1, 10)
        # 设置y坐标轴的范围
        plt.ylim(100000,1000000 )

        # 设置X轴文字的标题
        plt.xlabel("date")
        # 设置Y轴文字的标题
        plt.ylabel("元")

        # 设置图表的标题
        plt.title("数量和成交额变化情况")
        plt.show()
        print(type(x))
    except:
         print(('SQL执行失败，执行语句为:%s' % str(sql)))
        # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()



































def hua1():
       y1 = [8138700,8138700,8138700,8138700,8138700,8138700,8138700,8138700,8138700,9693500]
       x1 = range(0, 10)
       x2 = range(0, 10)
       y2 = [197523215,222404435,191183031,67037918,154926927,307633593,628039000,693158484,579973766,237689141]
       plt.plot(x1, y1, label='number', linewidth=3, color='r', marker='o',
                markerfacecolor='blue', markersize=12)
       plt.plot(x2, y2, label='achievemoney')
       plt.xlabel('day')
       plt.ylabel('sell')
       plt.title('2018/10/20-30sell analyze')
       plt.legend()
       plt.show()