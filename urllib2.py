import urllib.request, http.cookiejar

#直接请求
# TIPS:python3不能使用urllib2包，只能使用urllib包
resp = urllib.request.urlopen("http://www.baidu.com")
# print(resp.getcode())   #根据返回的状态码是否为200来判断成功与否

#读取内容
# cont = resp.read()


# 方法2
# 创建request对象
request = urllib.request.Request("https://www.baidu.com")

# 添加数据
# urllib.request.data = "shit"
# request.data = "shit"
# 添加http头信息
request.add_header('User-Agent', 'Mozilla/5.0')
# 发送数据请求结果
response = urllib.request.urlopen(request)




# 创建一个opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar))
# 给urllib安装opener
urllib.request.install_opener(opener)
# 使用带有cookie的urllib访问网页
# response1 = urllib.request.urlopen("https://www.baidu.com")

