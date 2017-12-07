import requests
a = "a=1,b=2"
b = zip(a[0],a[1])
print(b)
x = [1, 2, 3]
y = [4, 5, 6, 7]
xy = zip(x, y)
dictlist = []
dictdata = {}
print (xy)
s = '  -----abc123++++       '
url = 'http://127.0.0.1:8000/Blog/search'
z = 'keyword = 这是, token=1512353983'
if " " in z:
    print("111111")
    z = z.replace(' ','')
    print(z)
    z = z.replace(',','=')
    print(z)
    z = z.split('=')
    print(z)
    m = z[::2]
    n = z[1::2]
    print(m)
    print(n)
    if len(m) == len(n):
        print("123")
        dictdata = dict(zip(m,n))
        print(dictdata)
        request = requests.post(url=url,data=dictdata)
        print(request.text)
    else:
        print("22")
    #print(z.replace(' ','') )
    #print(z)
else:
     print(z.split('='))
# 删除两边空字符
print(s.strip())

# 删除左边空字符
print(s.rstrip())

# 删除右边空字符
print(s.lstrip())

# 删除两边 - + 和空字符
print(s.strip().strip('-+'))