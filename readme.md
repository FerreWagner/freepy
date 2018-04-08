#一个由python开发的简单爬虫


----------

架构：
爬虫调度：URL管理器  ->网页下载器->网页解析器  ->价值数据

URL管理器：管理待抓取URL集合和已抓取URL集合

- 防止重复、循环抓取

		实现方式：内存：呆爬取URL集合：set()；已爬取URL集合：set()
		为何使用set？因为py中sete可以直接去除集合中重复的元素

		存储在关系型数据库中：如MySQL

		存储在缓存数据库中：如Redis（支持set数据结构，可用set）

<br/>
网页下载器：将互联网上URL对应的网页下载到本地的工具

py的网页下载器：**urllib2**->py官方基础模块，支持直接的URL下载；**requests**->第三方包




1. urllib2下载网页方法1：最简洁：urllib2.urlopen(url地址)
2. urllib2下载网页方法2：添加data、http header
3. urllib2下载网页方法3：添加特殊情景的处理器(SSL层 or COOKIE等)
4. 
