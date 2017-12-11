import xlrd
fname = "one.xlsx"
bk = xlrd.open_workbook(fname)
sh = bk.sheet_by_name("Sheet1")#找到sheet1的工作表
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print ("nrows %d, ncols %d" % (nrows,ncols))
#获取第一行第一列数据
cell_value = sh.cell_value(1,0)
print (cell_value,"cell_value")

row_list = []
ncols_list = []
#获取各行数据
for i in range(1,nrows):
        row_data = sh.row_values(i)
        if "http" in row_data[1]:
            row_list.append(row_data)
        else:
            print("表格中的接口地址错误，请填写正确的接口地址。")
            break


print(row_list)

