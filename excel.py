import xlrd
import xlwt

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\Lenovo\Desktop\工作簿1.xlsx')
    # 获取所有sheet
    print(workbook.sheet_names()) # [u'sheet1', u'sheet2']
    #获取sheet2
    sheet2_name= workbook.sheet_names()[1]
    print(sheet2_name)
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_name('Sheet1')
    # sheet的名称，行数，列数
    print (sheet2.name,sheet2.nrows,sheet2.ncols)
    rows = sheet2.row_values(3) # 获取第四行内容
    cols = sheet2.col_values(2) # 获取第三列内容
    print(rows)
    print(cols)
    #获取单元格内容的三种方法
    print(sheet2.cell(1,0).value.encode('utf-8'))
    print(sheet2.cell_value(1,0).encode('utf-8'))
    print(sheet2.row(1)[0].value.encode('utf-8'))
    # 获取单元格内容的数据类型
    print(sheet2.cell(1,0).ctype)
if __name__ == '__main__':
    read_excel()





