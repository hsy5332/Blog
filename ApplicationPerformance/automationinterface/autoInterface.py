import xlrd
import requests
import json
import openpyxl
import time
import ApplicationPerformance.applicationperformance.launchTime as launchTime

from openpyxl.styles import Font, colors, Alignment, borders


# 读取Excel测试用例，并请求接口
def readExcel():
    # 创建Excel
    createdcase = openpyxl.Workbook()
    sheetform = createdcase.active  # 创建一个活动
    sheetformOnestyle = Font(name='等线', size=12, color=colors.RED, )
    sheetform.title = 'Result'
    sheetform['A1'] = "用例编号"
    sheetform['B1'] = "接口地址"
    sheetform['C1'] = "请求参数"
    sheetform['D1'] = '请求方式'
    sheetform['E1'] = '返回参数'
    sheetform['F1'] = '是否执行'  # 写入对应的数值
    sheetform['G1'] = '备注'  # 写入对应的数值
    sheetform['A1'].font = sheetformOnestyle
    sheetform['B1'].font = sheetformOnestyle
    sheetform['C1'].font = sheetformOnestyle
    sheetform['D1'].font = sheetformOnestyle
    sheetform['E1'].font = sheetformOnestyle
    sheetform['F1'].font = sheetformOnestyle
    sheetform['G1'].font = sheetformOnestyle

    # 读取Excel
    excledata = xlrd.open_workbook("interfacecase.xlsx")
    excledata_sheel = excledata.sheet_by_name('Sheet1')  # 获取Excel表格中的数据，为sheet1的工作间
    exclerows = excledata_sheel.nrows  # 获取Excel的行数
    row_list = []  # 存放用例数据的列表
    datakey = []  # 拆分Excel中参数栏，存放请求参数的key
    datavalues = []  # 拆分Excel中参数栏，存放请求参数的values
    datadict = {}  # 用于存放请求参数字段使用
    returndatalist = []
    print("执行用例的总数量为：%s" % (exclerows - 1))
    starttime = time.time()
    eventid = time.strftime("%Y%m%d%H%M%S", time.localtime())
    for i in range(1, exclerows):
        row_data = excledata_sheel.row_values(i)
        if "http" in row_data[1]:
            # 把读取Excel的数据存放到0-4的表格中（0开始不包含4）
            sheetform.append(excledata_sheel.row_values(i)[0:4])
            # 把读取Excel的数据存放到4的表格中(1开始数，post列)
            poststr = ("F%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
            sheetform[poststr] = excledata_sheel.row_values(i)[4]
            # 把读取Excel的数据存放到5的表格中(1开始数，备注列)
            tfstr = ("G%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
            sheetform[tfstr] = excledata_sheel.row_values(i)[5]
            if 1 == int(row_data[4]):  # 判断Excel中设置的方式是否为执行状态
                row_list.append(row_data)
                datastr = row_data[2].replace(' ', '')
                datastr = datastr.replace(',', '=')  # 格式化row_data[2]参数的字符串
                datastr = datastr.split('=')
                datakey = datastr[::2]  # 把key放入datakey
                datavalues = datastr[1::2]  # 把values放入datavalues
                datadict = dict(zip(datakey, datavalues))  # 生成请求参数字典
                url = row_data[1]
                if 'post' == str(row_data[3]):  # 判断接口请求方式是否为post
                    try:
                        returnparameter = interfaceRequest(url, datadict, 'post')
                        print(int(row_data[0]), "接口返回数据 :", returnparameter)
                        returndatalist.append(returnparameter)
                        # 把读取Excel的数据存放到E2的列表格中
                        returnparm = ("E%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
                        sheetform[returnparm] = str(returndatalist[0])
                        returndatalist = []
                        savedate = "insert into automation_interface  (`interfaceurl`,`requestparameter`,`returnparameter`,`requesttype`,`casestatus`,`caseid`,`remark`,`createdtime`,`updatetime`,`eventid`)VALUES(\"%s\",\"%s\",\"%s\",'%s','%s','%s',\"%s\",'%s','%s','%s')" % (
                            url, datadict, returnparameter, str(row_data[3]), int(row_data[4]), int(row_data[0]),
                            str(row_data[5]),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), eventid)
                        launchTime.MysqlConnect().saveDatatoMysql(savedate)
                    except:
                        print(int(row_data[0]), "请检查用例 %s 的接口地址以及参数是否有问题 ！" % (int(row_data[0])))
                        returndatalist.append("请检查用例的接口地址以及参数是否有问题 ！")
                        # 把读取Excel的数据存放到E2的列表格中
                        returnparm = ("E%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
                        sheetform[returnparm] = str(returndatalist[0])
                        sheetform[returnparm].font = sheetformOnestyle
                        returnparameter = "返回的参数有问题"
                        returndatalist = []
                        savedate = "insert into automation_interface  (`interfaceurl`,`requestparameter`,`returnparameter`,`requesttype`,`casestatus`,`caseid`,`remark`,`createdtime`,`updatetime`,`eventid`)VALUES(\"%s\",\"%s\",\"%s\",'%s','%s','%s',\"%s\",'%s','%s','%s')" % (
                            url, datadict, returnparameter, str(row_data[3]), int(row_data[4]), int(row_data[0]),
                            str(row_data[5]),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), eventid)
                        launchTime.MysqlConnect().saveDatatoMysql(savedate)
                elif 'get' == str(row_data[3]):  # 判断接口请求方式是否为get
                    try:
                        returnparameter = interfaceRequest(url, datadict, 'get')
                        print(int(row_data[0]), "接口返回数据 :", returnparameter)
                        returndatalist.append(returnparameter)
                        # 把读取Excel的数据存放到E2的列表格中
                        returnparm = ("E%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
                        sheetform[returnparm] = str(returndatalist[0])
                        returndatalist = []
                        savedate = "insert into automation_interface  (`interfaceurl`,`requestparameter`,`returnparameter`,`requesttype`,`casestatus`,`caseid`,`remark`,`createdtime`,`updatetime`,`eventid`)VALUES(\"%s\",\"%s\",\"%s\",'%s','%s','%s',\"%s\",'%s','%s','%s')" % (
                            url, datadict, returnparameter, str(row_data[3]), row_data[4], int(row_data[0]),
                            str(row_data[5]),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), eventid)
                        launchTime.MysqlConnect().saveDatatoMysql(savedate)

                    except:
                        print(int(row_data[0]), "请检查用例 %s 的接口地址以及参数是否有问题 ！" % (int(row_data[0])))
                        returndatalist.append("请检查用例的接口地址以及参数是否有问题 ！")
                        # 把读取Excel的数据存放到E2的列表格中
                        returnparm = ("E%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
                        sheetform[returnparm] = str(returndatalist[0])
                        sheetform[returnparm].font = sheetformOnestyle
                        returnparameter = "返回的参数有问题"
                        returndatalist = []
                        savedate = "insert into automation_interface  (`interfaceurl`,`requestparameter`,`returnparameter`,`requesttype`,`casestatus`,`caseid`,`remark`,`createdtime`,`updatetime`,`eventid`)VALUES(\"%s\",\"%s\",\"%s\",'%s','%s','%s',\"%s\",'%s','%s','%s')" % (
                            url, datadict, returnparameter, str(row_data[3]), row_data[4], int(row_data[0]),
                            str(row_data[5]),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), eventid)
                        launchTime.MysqlConnect().saveDatatoMysql(savedate)
                else:  # 接口请求方式不为get也不为post
                    print(int(row_data[0]), "请检查用例 %s 的请求方式是否填写正确 ！" % (int(row_data[0])))
                    returndatalist.append("请检查用例的请求方式是否填写正确 ！")
                    # 把读取Excel的数据存放到E2的列表格中
                    returnparm = ("E%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
                    sheetform[returnparm] = str(returndatalist[0])
                    sheetform[returnparm].font = sheetformOnestyle
                    returndatalist = []
                    returnparameter = "请求方式有问题"
                    savedate = "insert into automation_interface  (`interfaceurl`,`requestparameter`,`returnparameter`,`requesttype`,`casestatus`,`caseid`,`remark`,`createdtime`,`updatetime`,`eventid`)VALUES(\"%s\",\"%s\",\"%s\",'%s','%s','%s',\"%s\",'%s','%s','%s')" % (
                        url, datadict, returnparameter, str(row_data[3]), int(row_data[4]), int(row_data[0]),
                        str(row_data[5]),
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), eventid)
                    launchTime.MysqlConnect().saveDatatoMysql(savedate)
            else:
                print(int(row_data[0]), "用例编号：%s 设置为不执行。" % (int(row_data[0])))
                returndatalist.append("用例未执行")
                # 把读取Excel的数据存放到E2的列表格中
                returnparm = ("E%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
                sheetform[returnparm] = str(returndatalist[0])
                sheetform[returnparm].font = sheetformOnestyle
                returndatalist = []
                returnparameter = " "
                savedate = "insert into automation_interface  (`interfaceurl`,`requestparameter`,`returnparameter`,`requesttype`,`casestatus`,`caseid`,`remark`,`createdtime`,`updatetime`,`eventid`)VALUES(\"%s\",\"%s\",\"%s\",'%s','%s','%s',\"%s\",'%s','%s','%s')" % (
                    url, datadict, returnparameter, str(row_data[3]), int(row_data[4]), int(row_data[0]),
                    str(row_data[5]),
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), eventid)
                launchTime.MysqlConnect().saveDatatoMysql(savedate)
        else:
            print("表格中的接口地址错误，请填写正确的接口地址。")
            returndatalist.append("表格中的接口地址错误，请填写正确的接口地址。")
            # 把读取Excel的数据存放到E2的列表格中
            returnparm = ("E%s" % (int(excledata_sheel.row_values(i)[0]) + 1))
            sheetform[returnparm] = str(returndatalist[0])
            sheetform[returnparm].font = sheetformOnestyle
            returndatalist = []
            returnparameter = " "
            savedate = "insert into automation_interface  (`interfaceurl`,`requestparameter`,`returnparameter`,`requesttype`,`casestatus`,`caseid`,`remark`,`createdtime`,`updatetime`,`eventid`)VALUES(\"%s\",\"%s\",\"%s\",'%s','%s','%s',\"%s\",'%s','%s','%s')" % (
                url, datadict, returnparameter, str(row_data[3]), int(row_data[4]), int(row_data[0]),
                str(row_data[5]),
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), eventid)
            launchTime.MysqlConnect().saveDatatoMysql(savedate)
            break
    endtime = time.time()
    print("执行用例的总时间为：", round((endtime - starttime), 2))
    # 为创建的Excel表格命名
    excelname = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    createdcase.save('%s.xlsx' % (excelname))


# 请求接口地址并返回数据
def interfaceRequest(url, data, method):
    if method == "post":
        request = requests.post(url=url, data=data)
        return json.loads(request.text)
    else:
        request = requests.get(url=url, data=data)
        return json.loads(request.text)


readExcel()
