import urllib.parse
import urllib.request
import urllib.error
import urllib.robotparser
import http.cookiejar
import socket


# 打印网页的内容, urllib.request.urlopen
def print_http_content():
    response = urllib.request.urlopen('https://www.python.org')
    print(response.read().decode('utf-8'))


# 查看返回的类型: http.client.HTTPResponse
def print_http_type():
    response = urllib.request.urlopen('https://www.python.org')
    print(type(response))


# 查看返回的信息 status getheaders
def print_http_info():
    response = urllib.request.urlopen('https://www.python.org')
    print(response.status)
    print(response.getheaders())
    # print(type(response.getheaders()[0]))
    print(response.getheader('Connection'))


# urllib 的 data 参数
def print_http_data():
    data = bytes(urllib.parse.urlencode({'name':'germey'}), encoding='utf-8')
    print(type(data))
    response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
    print(response.read().decode('utf-8'))


# timeout 参数
def print_http_timeout():
    try:
        response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')


# Request 对象
def print_http_request():
    request = urllib.request.Request('https://www.baidu.com')
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))


# Request 对象
def print_http_request2():
    url = 'https://www.httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'www.httpbin.org'
    }
    dict = {'name': 'germey'}
    data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))


# 基本访问认证
def print_http_basic_access_authentication():
    username = 'admin'
    password = 'admin'
    url = 'https://ssr3.scrape.center/'

    p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    # 处理验证的 Handler 类
    auth_handler = urllib.request.HTTPBasicAuthHandler(p)
    opener = urllib.request.build_opener(auth_handler)
    try:
        result = opener.open(url)
        html = result.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        print(e.reason)


# 代理
def print_http_proxy():
    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1:7893',
        'https': 'https://127.0.0.1:7893',
    })
    opener = urllib.request.build_opener(proxy_handler)
    try:
        response = opener.open('http://www.baidu.com')
        print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(e.reason)


# cookie
def print_http_cookie_1():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    for item in cookie:
        print(item.name + " = " + item.value)


# cookie
def print_http_cookie_2():
    filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    # cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


# 读取 cookie
def print_http_read_cookie():
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('LWPcookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))


# 处理异常 URLError 是异常模块的基类
def print_http_url_error_except():
    try:
        response = urllib.request.urlopen('https://cuiqingcai.com/404')
    except urllib.error.URLError as e:
        print(e.reason)


# HTTPError 派生自 URLError, 处理 HTTP 请求错误, 有属性 code, reason, headers
def print_http_http_error_except():
    try:
        response = urllib.request.urlopen('https://cuiqingcai.com/404')
    except urllib.error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')


# 捕获异常写法
def print_http_except():
    try:
        response = urllib.request.urlopen('https://cuiqingcai.com/404')
    except urllib.error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except urllib.error.URLError as e:
        print(e.reason)
    else:
        print('Request Successfully')


# reason 属性除了为字符串, 也可能是对象
def print_http_error_reason_is_object():
    try:
        response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
    except urllib.error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')


# urlparse 实现 URL 的识别和分段
def print_http_url_parse():
    result = urllib.parse.urlparse('https://www.baidu.com/index.html;user?id=5#comment')
    print(type(result))
    print(result)


# urlparse 默认协议参数
def print_http_url_parse_default_scheme():
    result = urllib.parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
    print(result)


# urlparse 忽略 fragment
def print_http_url_parse_ignorance_fragment():
    # result = urllib.parse.urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    result = urllib.parse.urlparse('https://www.baidu.com/index.html#comment', allow_fragments=False)
    print(result)


# urlparse 返回的 ParseResult 是一个元祖
def print_http_url_parse_result():
    result = urllib.parse.urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    print(result.scheme, result[0], result.netloc, result[1], sep='\n')


# urlunparse 拼接一个 url, 参数为可迭代对象, 长度为6
def print_http_url_un_parse():
    data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(urllib.parse.urlunparse(data))


# urlsplit 同 urlparse, 只是不再分开 path 和 param
def print_http_url_split():
    result = urllib.parse.urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
    print(result)


# urlunsplit 拼接一个 url, 参数为可迭代对象, 长度为5
def print_http_url_un_split():
    data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
    print(urllib.parse.urlunsplit(data))


# urljoin 拼接 url, 提供一个 base_url 作为第一个参数, 新的链接作为第二个参数, 使用 base_url 的 scheme, netloc, path 对第二个参数进行补充
def print_http_url_join():
    print(urllib.parse.urljoin('https://www.baidu.com', 'FAQ.html'))
    print(urllib.parse.urljoin('https://www.baidu.com', 'http://cuiqingcai.com/FAQ.html'))
    print(urllib.parse.urljoin('https://www.baidu.com/about.html', 'http://cuiqingcai.com/FAQ.html'))
    print(urllib.parse.urljoin('https://www.baidu.com/about.html', 'http://cuiqingcai.com/FAQ.html?question=2'))
    print(urllib.parse.urljoin('https://www.baidu.com?wd=abc', 'http://cuiqingcai.com/index.php'))
    print(urllib.parse.urljoin('https://www.baidu.com', '?category=2#comment'))
    print(urllib.parse.urljoin('www.baidu.com', '?category=2#comment'))
    print(urllib.parse.urljoin('www.baidu.com#comment', '?category=2'))


# urlencode 构造 GET 请求参数
def print_http_url_encode():
    params = {
        'name': 'germey',
        'age': 25
    }
    base_url = 'https://www.baidu.com?'
    url = base_url + urllib.parse.urlencode(params)
    print(url)


# parse_qs 将 GET 请求参数转回字典
def print_http_parse_qs():
    query = 'name=germey&age=25'
    print(urllib.parse.parse_qs(query))


# parse_qsl 将 GET 请求参数转换为由元组组成的列表
def print_http_parse_qsl():
    query = 'name=germey&age=25'
    print(urllib.parse.parse_qsl(query))


# quote 将内容转换为 URL 编码格式
def print_http_parse_quote():
    keyword = '壁纸'
    url = 'https://www.baidu.com/s?wd=' + urllib.parse.quote(keyword)
    print(url)


# unquote 解码 URL
def print_http_parse_unquote():
    url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
    print(urllib.parse.unquote(url))


# 分析爬虫协议文件
def print_http_robot_parse():
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url('https://www.baidu.com/robots.txt')
    rp.read()
    print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
    print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
    print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))


# 使用 parse() 方法对 robots.txt 的文本进行分析
def print_http_robot_parse2():
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(urllib.request.urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
    print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
    print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
    print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))


if __name__ == '__main__':
    print_http_request()
    # print_http_robot_parse2()
    print('Done')
