import matplotlib.pyplot as plt#画图文件
def show1():
       y1 = [8138700,8138700,8138700,8138700,8138700,8138700,8138700,8138700,8138700,9693500]
       x1 = range(0, 10)
       x2 = range(0, 10)
       y2 = [197523215,222404435,191183031,67037918,154926927,307633593,628039000,693158484,579973766,237689141]
       plt.plot(x1, y1, label='Frist line', linewidth=3, color='r', marker='o',
                markerfacecolor='blue', markersize=12)
       plt.plot(x2, y2, label='second line')
       plt.xlabel('时间')
       plt.ylabel('销售情况')
       plt.title('2018/10/20-10/30销售情况')
       plt.legend()
       plt.show()
show1()