# import bs4
# 在python安装目录下的scripts下查找是否安装了python包管理工具pip，如果存在，则直接切换至scripts目录使用命令行安装bs4包：pip install beautifulsoup4
# print(bs4)

import re
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')   #python3 缺省的编码是unicode, 再在from_encoding设置为utf8, 会被忽视掉，去掉【from_encoding="utf-8"】这一个好了

print('获取所有链接')
links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())


print('获取lacie的链接')
link_node = soup.find('a', href='http://example.com/lacie')
print(link_node.name, link_node['href'], link_node.get_text())

print('正则匹配')
link_node1 = soup.find('a', href=re.compile(r"ill"))
print(link_node1.name, link_node1['href'], link_node1.get_text())

print('获取p段落文字')
link_node2 = soup.find('p', class_="title")     #class为python关键字，所以此时为class_
print(link_node2.name, link_node2.get_text())