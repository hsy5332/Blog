import  xlrd
import requests
import json

#读取Excel测试用例，并请求接口
def readexcel():
    excledata = xlrd.open_workbook("one.xlsx")
    excledata_sheel = excledata.sheet_by_name('Sheet1')#获取Excel表格中的数据，为sheet1的工作间
    exclerows = excledata_sheel.nrows #获取Excel的行数
    row_list = [] #存放用例数据的列表
    datakey = [] #拆分Excel中参数栏，存放请求参数的key
    datavalues = [] #拆分Excel中参数栏，存放请求参数的values
    datadict = {} # 用于存放请求参数字段使用
    print("执行用例的总数量为：%s"%(exclerows-1))
    for i in range(1, exclerows):
        row_data = excledata_sheel.row_values(i)
        if "http" in row_data[1]:
            if 1 == int(row_data[4]):#判断Excel中设置的方式是否为执行状态
                    row_list.append(row_data)
                    datastr = row_data[2].replace(' ', '')
                    datastr = datastr.replace(',', '=')#格式化row_data[2]参数的字符串
                    datastr = datastr.split('=')
                    datakey=datastr[::2]#把key放入datakey
                    datavalues = datastr[1::2]#把values放入datavalues
                    datadict = dict(zip(datakey,datavalues))#生成请求参数字典
                    url = row_data[1]
                    if 'post' == str(row_data[3]):#判断接口请求方式是否为post
                        try :
                            print(int(row_data[0]), "接口返回数据 :", interfaceRequest(url, datadict, 'post'))
                        except:
                            print(int(row_data[0]),"请检查用例 %s 的接口地址以及参数是否有问题 ！"%(int(row_data[0])))
                    elif 'get' == str(row_data[3]):#判断接口请求方式是否为get
                        try :
                            print(int(row_data[0]),"接口返回数据 :",interfaceRequest(url,datadict,'get'))
                        except:
                            print(int(row_data[0]),"请检查用例 %s 的接口地址以及参数是否有问题 ！"%(int(row_data[0])))
                    else:#接口请求方式不为get也不为post
                        print(int(row_data[0]),"请检查用例 %s 的请求方式是否填写正确 ！" % (int(row_data[0])))
            else:
                print(int(row_data[0]),"用例编号：%s 设置为不执行。" %(int(row_data[0])))
        else:
            print("表格中的接口地址错误，请填写正确的接口地址。")
            break

#请求接口地址并返回数据
def interfaceRequest(url,data,method):
    if method == "post":
        request = requests.post(url=url,data=data)
        return json.loads(request.text)
    else:
        request = requests.get(url=url, data=data)
        return json.loads(request.text)

readexcel()