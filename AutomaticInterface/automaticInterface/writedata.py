import openpyxl
import xlrd
import time

from openpyxl.styles import Font, colors, Alignment


def writeExcel(excledata_sheel,exclerows):
    createdcase = openpyxl.Workbook()
    sheetform = createdcase.active#创建一个活动
    sheetformOnestyle = Font(name='等线', size=12, color=colors.RED,)
    sheetform.title = 'Result'
    sheetform['A1'] = "用例编号"
    sheetform['B1'] = "接口地址"
    sheetform['C1'] = "请求参数"
    sheetform['D1'] = '请求方式'
    sheetform['E1'] = '返回参数'
    sheetform['F1'] = '是否执行'  # 写入对应的数值
    sheetform['G1'] = '备注'#写入对应的数值
    sheetform['A1'].font = sheetformOnestyle
    sheetform['B1'].font = sheetformOnestyle
    sheetform['C1'].font = sheetformOnestyle
    sheetform['D1'].font = sheetformOnestyle
    sheetform['E1'].font = sheetformOnestyle
    sheetform['F1'].font = sheetformOnestyle
    sheetform['G1'].font = sheetformOnestyle
    # row = [1,2,3,5]
    # sheetform.append(row)
    # sheetform = createdcase.create_sheet('Result', index=1)
    #print(createdcase.get_sheet_names())

    for i in range(1,exclerows):
        print(excledata_sheel.row_values(i))
        #把读取Excel的数据存放到0-4的表格中（0开始不包含4）
        sheetform.append(excledata_sheel.row_values(i)[0:4])
        # 把读取Excel的数据存放到4的表格中(1开始数，post列)
        poststr = ("F%s"%(int(excledata_sheel.row_values(i)[0])+1))
        sheetform[poststr]=excledata_sheel.row_values(i)[4]
        # 把读取Excel的数据存放到5的表格中(1开始数，备注列)
        tfstr = ("G%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
        sheetform[tfstr] = excledata_sheel.row_values(i)[5]


    # excelname = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    excelname = 'A'
    createdcase.save('%s.xlsx' % (excelname))

